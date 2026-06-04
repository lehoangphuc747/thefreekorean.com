import json
import re

# Bảng map ký tự khoanh tròn thành số nguyên đáp án
ANSWER_MAP = {
    '①': 1, '➀': 1, '❶': 1,
    '②': 2, '➁': 2, '❷': 2,
    '③': 3, '➂': 3, '❸': 3,
    '④': 4, '➃': 4, '❹': 4
}

SPEAKER_PATTERN = r'^(여자|남자|남|여|어르신|직원|의사|교사|부장|행인|강사|선생님|선생|학생)\s*:\s*(.*)'

def is_latin_digit(s):
    return bool(re.match(r'^\d+$', s))

def parse_correct_answers():
    answers = {"listening": {}, "reading": {}}
    
    with open('public/downloads/topik/TOPIK II/36/TOPIK-2-36-answers-utf8.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        
    pages = content.split("--- PAGE ")
    for page in pages:
        if not page.strip():
            continue
        parts = page.split(" ---")
        page_content = parts[1] if len(parts) > 1 else page
        
        is_listening = "영역: 듣기" in page_content
        is_reading = "영역: 읽기" in page_content
        
        lines = [line.strip() for line in page_content.split('\n') if line.strip()]
        
        for idx in range(len(lines) - 1):
            line = lines[idx]
            if is_latin_digit(line):
                q_num = int(line)
                next_line = lines[idx + 1]
                if next_line in ANSWER_MAP:
                    ans_val = ANSWER_MAP[next_line]
                    if is_listening:
                        answers["listening"][q_num] = ans_val
                    elif is_reading:
                        answers["reading"][q_num] = ans_val
                            
    return answers

correct_answers = parse_correct_answers()

def clean_dialogue_flow(lines):
    cleaned_lines = []
    current_speaker = None
    current_text = ""
    for line in lines:
        line = line.strip()
        if not line:
            continue
        match = re.match(SPEAKER_PATTERN, line)
        if match:
            if current_speaker and current_text:
                cleaned_lines.append(f"{current_speaker}: {current_text}")
            current_speaker = match.group(1)
            current_text = match.group(2).strip()
        else:
            if current_speaker:
                if current_text and not current_text.endswith(('.', ',', '?', '!')):
                    current_text += " " + line
                else:
                    current_text += line
            else:
                cleaned_lines.append(line)
    if current_speaker and current_text:
        cleaned_lines.append(f"{current_speaker}: {current_text}")
    return "\n".join(cleaned_lines)

# Robust line-by-line transcript parser
def parse_listening_transcripts_accurate():
    transcripts = {}
    with open('public/downloads/topik/TOPIK II/36/TOPIK-2-36-transcript-utf8.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    raw_lines = content.split('\n')
    lines = []
    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        if "--- PAGE" in line or "제36회" in line or "B형" in line or "듣기 통합" in line:
            continue
        lines.append(line)
        
    current_q = None
    dialogue_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        q_match = re.match(r'^(\d+)\.(.*)', line)
        if q_match:
            q_num = int(q_match.group(1))
            rest = q_match.group(2).strip()
            if 1 <= q_num <= 50:
                if current_q and dialogue_lines:
                    transcripts[current_q] = clean_dialogue_flow(dialogue_lines)
                current_q = q_num
                dialogue_lines = []
                if rest and not any(rest.startswith(c) for c in ['①', '②', '③', '④', '➀', '➁', '➂', '➃']):
                    dialogue_lines.append(rest)
                i += 1
                continue
        if current_q is not None:
            is_choice = any(line.startswith(char) for char in ['①', '②', '③', '④', '➀', '➁', '➂', '➃'])
            is_instruction = "※" in line or "다음을 듣고" in line or "다음 대화를" in line
            if is_choice or is_instruction:
                transcripts[current_q] = clean_dialogue_flow(dialogue_lines)
                current_q = None
                dialogue_lines = []
            else:
                dialogue_lines.append(line)
        i += 1
    if current_q and dialogue_lines:
        transcripts[current_q] = clean_dialogue_flow(dialogue_lines)
    return transcripts

transcripts = parse_listening_transcripts_accurate()

def clean_question_text(text, q_num):
    text = text.replace("( ........................ )에 들어갈 가장 알맞은 것을 고르십시오. (각 2점)", "")
    text = text.replace("( ........................ )에 들어갈 가장 알맞은 것을 고르십시오.", "")
    text = text.replace("다음 밑줄 친 부분과 의미가 비슷한 것을 고르십시오. (각 2점)", "")
    text = text.replace("다음 밑줄 친 부분과 의미가 비슷한 것을 고르십시오.", "")
    text = text.replace("다음은 무엇에 대한 글인지 고르십시오. (각 2점)", "")
    text = text.replace("다음은 무엇에 대한 글인지 고르십시오.", "")
    text = text.replace("다음 글 또는 도표의 내용과 같은 것을 고르십시오. (각 2점)", "")
    text = text.replace("다음 글 또는 도표의 내용과 같은 것을 고르십시오.", "")
    text = text.replace("다음 글의 내용과 같은 것을 고르십시오.", "")
    text = text.replace("다음을 순서대로 맞게 배열한 것을 고르십시오. (각 2점)", "")
    text = text.replace("다음을 순서대로 맞게 배열한 것을 고르십시오.", "")
    text = text.replace("고르십시오.(각2점)", "")
    text = text.replace("고르십시오.", "")
    
    text = text.replace("2점", "")
    text = re.sub(r'\n+', '\n', text).strip()
    return text

def parse_section_robust(raw_text_path, section_name):
    with open(raw_text_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
        
    questions = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue
            
        expected_next_id = len(questions) + 1
        q_start_match = re.match(r'^(\d+)(.*)$', line)
        
        if q_start_match and int(q_start_match.group(1)) == expected_next_id:
            q_num = expected_next_id
            q_title = q_start_match.group(2).strip()
            
            i += 1
            while i < len(lines) and (lines[i] == "2점" or not lines[i].strip()):
                i += 1
                
            prompt_lines = []
            if q_title:
                prompt_lines.append(q_title)
                
            while i < len(lines):
                next_line = lines[i].strip()
                if next_line == "1" or next_line.startswith("1Option"):
                    break
                if "Question" in next_line and "image" in next_line:
                    prompt_lines.append(f"[IMAGE_PLACEHOLDER: q{q_num}]")
                else:
                    if next_line:
                        prompt_lines.append(next_line)
                i += 1
                
            q_ko_raw = "\n".join(prompt_lines).strip()
            
            choices = []
            if i < len(lines) and lines[i].startswith("1Option"):
                for c_idx in range(1, 5):
                    if i < len(lines) and lines[i].startswith(str(c_idx)):
                        img_path = f"/images/topik/36/p003-img0{c_idx}.jpeg" if q_num == 1 else \
                                   f"/images/topik/36/p003-img0{c_idx + 4}.jpeg" if q_num == 2 else \
                                   f"/images/topik/36/p004-img0{c_idx}.jpeg" if q_num == 3 else None
                        choices.append({
                            "type": "image",
                            "text": "",
                            "image": img_path
                        })
                        i += 1
            else:
                for c_idx in range(1, 5):
                    while i < len(lines) and not lines[i].strip():
                        i += 1
                    if i < len(lines) and lines[i] == str(c_idx):
                        i += 1
                        while i < len(lines) and not lines[i].strip():
                            i += 1
                        choice_text = lines[i] if i < len(lines) else ""
                        choices.append(choice_text)
                        i += 1
            
            image_url = None
            if section_name == "reading":
                if q_num == 5:
                    image_url = "/images/topik/36/p018-img01.jpeg"
                elif q_num == 6:
                    image_url = "/images/topik/36/p018-img02.jpeg"
                elif q_num == 7:
                    image_url = "/images/topik/36/p021-img01.jpeg"
                elif q_num == 8:
                    image_url = "/images/topik/36/p021-img02.jpeg"
                elif q_num == 9:
                    image_url = "/images/topik/36/p021-img03.jpeg"
                elif q_num == 10:
                    image_url = "/images/topik/36/p021-img04.jpeg"
            
            # Form question_ko correctly
            if section_name == "listening":
                q_ko = transcripts.get(q_num, "")
            else:
                q_ko = clean_question_text(q_ko_raw, q_num)
                
            if image_url:
                q_ko = q_ko.replace(f"[IMAGE_PLACEHOLDER: q{q_num}]", "").strip()
                
            correct_ans = correct_answers[section_name].get(q_num, 1)
            
            q_dict = {
                "id": q_num,
                "question_ko": q_ko,
                "choices": choices,
                "answer": correct_ans
            }
            
            # Map group instructions dynamically to distinct ranges
            active_group = None
            active_group_vi = None
            if section_name == "listening":
                ranges = [
                    ((1,3), "다음을 듣고 알맞은 그림을 고르십시오.", "Nghe và chọn bức tranh đúng."),
                    ((4,8), "다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.", "Nghe hội thoại và chọn câu nối tiếp phù hợp."),
                    ((9,12), "다음 대화를 잘 듣고 여자가 이어서 할 행동으로 알맞은 것을 고르십시오.", "Nghe và chọn hành động tiếp theo của người phụ nữ."),
                    ((13,16), "다음을 듣고 내용과 일치하는 것을 고르십시오.", "Nghe và chọn câu đúng với nội dung."),
                    ((17,20), "다음을 듣고 남자의 중심 생각을 고르십시오.", "Nghe và chọn suy nghĩ trung tâm của nhân vật."),
                    ((21,22), "[21~22] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((23,24), "[23~24] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((25,26), "[25~26] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((27,28), "[27~28] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((29,30), "[29~30] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((31,32), "[31~32] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((33,34), "[33~34] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((35,36), "[35~36] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((37,38), "[37~38] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((39,40), "[39~40] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((41,42), "[41~42] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((43,44), "[43~44] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((45,46), "[45~46] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((47,48), "[47~48] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi."),
                    ((49,50), "[49~50] 다음을 듣고 물음에 답하십시오.", "Nghe đoạn hội thoại và trả lời các câu hỏi.")
                ]
            else:
                ranges = [
                    ((1,2), "[1~2] ( )에 들어갈 가장 알맞은 것을 고르십시오.", "Chọn đáp án đúng nhất điền vào khoảng trống."),
                    ((3,4), "[3~4] 다음 밑줄 친 부분과 의미가 비슷한 것을 고르십시오.", "Chọn câu có ý nghĩa tương đồng với phần gạch chân."),
                    ((5,8), "[5~8] 다음은 무엇에 대한 글인지 고르십시오.", "Đọc và chọn chủ đề của đoạn văn."),
                    ((9,12), "[9~12] 다음 글 또는 도표의 내용과 같은 것을 고르십시오.", "Chọn câu đúng với nội dung bài viết hoặc biểu đồ."),
                    ((13,15), "[13~15] 다음을 순서대로 맞게 배열한 것을 고르십시오.", "Sắp xếp các câu sau theo thứ tự đúng."),
                    ((16,18), "[16~18] 다음을 읽고 ( )에 들어갈 내용으로 가장 알맞은 것을 고르십시오.", "Đọc đoạn văn và chọn đáp án thích hợp nhất điền vào khoảng trống."),
                    ((19,20), "[19~20] 다음을 읽고 물음에 답하십시오.", "Đọc đoạn văn sau và trả lời câu hỏi."),
                    ((21,22), "[21~22] 다음을 읽고 물음에 답하십시오.", "Đọc đoạn văn sau và trả lời câu hỏi."),
                    ((23,24), "[23~24] 다음을 읽고 물음에 답하십시오.", "Đọc đoạn văn sau và trả lời câu hỏi."),
                    ((25,27), "[25~27] 다음은 신문 기사의 제목입니다. 가장 잘 설명한 것을 고르십시오.", "Chọn câu giải thích đúng nhất tiêu đề bài báo."),
                    ((28,31), "[28~31] 다음을 읽고 ( )에 들어갈 내용으로 가장 알맞은 것을 고르십시오.", "Đọc đoạn văn và chọn đáp án thích hợp nhất điền vào khoảng trống."),
                    ((32,34), "[32~34] 다음을 읽고 내용이 같은 것을 고르십시오.", "Đọc đoạn văn sau và chọn đáp án có nội dung đồng nhất."),
                    ((35,38), "[35~38] 다음 글의 주제로 가장 알맞은 것을 고르십시오.", "Chọn chủ đề chính của bài viết dưới đây."),
                    ((39,41), "[39~41] 주어진 문장이 들어갈 곳으로 가장 알맞은 곳을 고르십시오.", "Chọn vị trí thích hợp nhất cho câu văn đã cho."),
                    ((42,43), "[42~43] 다음을 읽고 물음에 답하십시오.", "Đọc đoạn văn sau và trả lời câu hỏi."),
                    ((44,45), "[44~45] 다음을 읽고 물음에 답하십시오.", "Đọc đoạn văn sau và trả lời câu hỏi."),
                    ((46,47), "[46~47] 다음을 읽고 물음에 답하십시오.", "Đọc đoạn văn sau và trả lời câu hỏi."),
                    ((48,50), "[48~50] 다음을 읽고 물음에 답하십시오.", "Đọc đoạn văn sau và trả lời câu hỏi.")
                ]
                
            for (start, end), ko, vi in ranges:
                if start <= q_num <= end:
                    active_group = ko
                    active_group_vi = vi
                    break
                    
            if active_group:
                q_dict["group_instruction"] = active_group
            if active_group_vi:
                q_dict["group_instruction_vi"] = active_group_vi
            if image_url:
                q_dict["image"] = image_url
                
            questions.append(q_dict)
            continue
            
        i += 1
        
    return questions

listening_questions = parse_section_robust('scripts/topik36-listening-raw.txt', "listening")
reading_questions = parse_section_robust('scripts/topik36-reading-raw.txt', "reading")

# Paired Listening questions: copy over the transcripts from odd question to even question (Q21-Q50)
for q_id in range(22, 51, 2):
    paired_q = next((q for q in listening_questions if q["id"] == q_id), None)
    base_q = next((q for q in listening_questions if q["id"] == q_id - 1), None)
    if paired_q and base_q and "question_ko" in base_q:
        paired_q["question_ko"] = base_q["question_ko"]

# Format Writing Section Answers from answers-utf8.txt
writing_questions = [
    {
      "id": 51,
      "group_instruction": "[51～52] 다음을 읽고 ㉠과 ㉡에 들어갈 말을 각각 한 문장으로 쓰십시오. (각 10점)",
      "group_instruction_vi": "Đọc đoạn văn sau và viết một câu thích hợp điền vào khoảng trống ㉠ và ㉡.",
      "question_ko": "받는 사람: 김영호 선생님\n안녕하세요? 김영호 선생님.\n한국어 교육학과 이재원입니다.\n다름이 아니라 이번 주 금요일에 선생님을 찾아뵈려고 했는데 ( ㉠ ).\n제가 그날 오후에 고향에서 부모님이 오시기 때문입니다.\n선생님, 다음 주 중에는 언제 괜찮으십니까?\n제가 ( ㉡ ).\n그럼 건강히 지내십시오.",
      "type": "short_answer",
      "points": 10,
      "choices": [],
      "answer": "",
      "model_answer": "㉠ 금요일에 뵙기 어려울 거 같습니다. / 금요일에 다른 일이 생겼습니다. / 금요일에 사정이 생겨서 찾아뵙기가 어려울 거 같습니다.\n㉡ 언제 시간이 괜찮으십니까? / 언제 시간이 되십니까? / 괜찮으신 시간을 말씀해 주시겠습니까? / 혹시 다음 주 금요일에 뵈러 가도 되겠습니까?"
    },
    {
      "id": 52,
      "group_instruction": "[51～52] 다음을 읽고 ㉠과 ㉡에 들어갈 말을 각각 한 문장으로 쓰십시오. (각 10점)",
      "group_instruction_vi": "Đọc đoạn văn sau và viết một câu thích hợp điền vào khoảng trống ㉠ và ㉡.",
      "question_ko": "기회는 어떤 사람에게 명예와 부를 안겨 준다. 기회를 통해서 평범한 사람이 유명해지기도 하고 ( ㉠ ). 이런 변화를 보고 사람들은 자신에게도 그런 기회가 찾아오기를 기다린다. 그러나 실제로 ( ㉡ ). 이렇게 기회를 잘 이용하지 못하는 것은 기회를 잡으려는 준비를 하지 않았기 때문이다.",
      "type": "short_answer",
      "points": 10,
      "choices": [],
      "answer": "",
      "model_answer": "㉠ 가난한 사람이 부자가 되기도 한다. / 부자가 되기도 한다.\n㉡ 기회가 와도 그 기회를 잘 이용하지 못한다. / 찾아온 기회를 놓치는 사람들이 많다. / 기회가 찾아오면 활용하지 못하는 사람들이 많다."
    },
    {
      "id": 53,
      "group_instruction": "최근 한국 사회에서는 1인 가구가 계속 증가하고 있습니다. 다음 자료를 참고하여 1인 가구 증가의 원인과 현황을 설명하는 글을 200∼300자로 쓰십시오. (30점)",
      "group_instruction_vi": "Viết một đoạn văn khoảng 200~300 chữ giải thích về hiện trạng và nguyên nhân tăng hộ gia đình 1 người dựa trên tài liệu sau.",
      "question_ko": "주제: 1인 가구 증가 현황 및 원인\n현황: 2000년 16% -> 2012년 26% (12년 사이 10% 증가)\n원인:\n1. 결혼관의 변화로 인한 독신자 수의 증가\n2. 노인 인구 증가\n3. 여성의 사회 진출 증가",
      "type": "essay",
      "points": 30,
      "choices": [],
      "answer": "",
      "model_answer": "최근 한국 사회에서는 1인 가구가 계속 증가하고 있다. 2000년 전체 가구 수의 16%에 불과했던 1인 가구는 꾸준히 증가하여 2012년에는 26%에 도달했다. 12년 사이에 10%가 증가한 것이다. 이러한 증가의 원인은 다음과 같다. 첫째, 결혼관의 변화로 인한 독신자 수의 증가이다. 둘째, 노인 인구가 증가하면서 1인 가구도 증가하게 되었다. 셋째, 여성의 사회 진출도 1인 가구가 증가하는 데 영향을 주었다. 이러한 원인으로 1인 가구 수는 앞으로도 지속적으로 증가할 전망이다."
    },
    {
      "id": 54,
      "group_instruction": "다음을 주제로 하여 자신의 생각을 600～700자로 글을 쓰십시오. (50점)",
      "group_instruction_vi": "Viết một bài luận khoảng 600~700 chữ trình bày suy nghĩ của bạn về chủ đề dưới đây.",
      "question_ko": "우리가 공부나 일을 할 때 동기가 분명히 있어야 더 잘 실행할 수 있습니다. 이러한 동기에는 흥미, 만족감, 자부심과 같은 내적 동기도 있고 칭찬이나 보상과 같은 외적 동기도 있습니다. '동기가 일에 미치는 영향'에 대해 아래의 내용을 중심으로 자신의 생각을 쓰십시오.\n\n1. 동기는 일의 시작 단계에서 어떠한 역할을 합니까?\n2. 동기가 일의 결과에 미치는 영향은 무엇입니까?",
      "type": "essay",
      "points": 50,
      "choices": [],
      "answer": "",
      "model_answer": "우리가 어떤 일을 진행하는 데에는 동기가 중요한 역할을 한다. 동기란 어떤 일을 하게 하는 보이지 않는 힘인데 동기에는 내적 동기와 외적 동기가 있다... (자세한 채점 기준은 모범답안 참조)"
    }
]

# Create final JSON
exam_json = {
  "meta": {
    "title": "Đề thi thử TOPIK II - Kỳ 36",
    "level": "TOPIK II",
    "duration": 180,
    "totalQuestions": 104,
    "description": "Đề thi thử TOPIK II dựa trên đề thi chính thức kỳ 36 (제36회 한국어능력시험 II)."
  },
  "sections": [
    {
      "type": "listening",
      "title": "듣기 (Nghe)",
      "duration": 60,
      "audio": "/api/topik-audio/TOPIK-2-36-audio.mp3",
      "questions": listening_questions
    },
    {
      "type": "writing",
      "title": "쓰기 (Viết)",
      "duration": 50,
      "questions": writing_questions
    },
    {
      "type": "reading",
      "title": "읽기 (Đọc)",
      "duration": 70,
      "questions": reading_questions
    }
  ]
}

# Save output
output_file = 'src/content/topik/thi-thu/topik2-thi-thu-36.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(exam_json, f, ensure_ascii=False, indent=2)

print("JSON parsed successfully with schema compliance!")
