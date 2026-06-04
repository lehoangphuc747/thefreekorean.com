#!/usr/bin/env python3
"""Parse TOPIK II Exam 35 data from PDFs into JSON."""
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# ── Answer keys ──
listening_answers = {
    1:2, 2:4, 3:1, 4:2, 5:4, 6:3, 7:2, 8:4, 9:1, 10:3,
    11:1, 12:3, 13:4, 14:4, 15:3, 16:3, 17:1, 18:1, 19:2, 20:1,
    21:2, 22:2, 23:4, 24:3, 25:4, 26:2, 27:2, 28:4, 29:1, 30:3,
    31:4, 32:2, 33:1, 34:2, 35:4, 36:4, 37:2, 38:4, 39:2, 40:1,
    41:3, 42:3, 43:1, 44:3, 45:3, 46:1, 47:1, 48:2, 49:4, 50:3
}

reading_answers = {
    1:3, 2:4, 3:1, 4:1, 5:1, 6:2, 7:1, 8:3, 9:4, 10:1,
    11:2, 12:3, 13:1, 14:4, 15:4, 16:2, 17:3, 18:3, 19:2, 20:4,
    21:1, 22:2, 23:1, 24:3, 25:3, 26:1, 27:4, 28:3, 29:4, 30:4,
    31:1, 32:2, 33:4, 34:4, 35:2, 36:2, 37:4, 38:4, 39:2, 40:3,
    41:3, 42:1, 43:2, 44:2, 45:3, 46:2, 47:3, 48:2, 49:1, 50:4
}

# ── Load raw data ──
with open(r'D:\A Web\the-free-korean\scripts\topik35-transcript-raw.json', 'r', encoding='utf-8') as f:
    transcript_pages = json.load(f)

with open(r'D:\A Web\the-free-korean\scripts\topik35-reading-raw.json', 'r', encoding='utf-8') as f:
    reading_pages = json.load(f)

# ── Parse listening questions from transcript ──
def parse_listening(transcript_pages):
    """Parse listening questions from transcript pages."""
    questions = []
    
    # Combine all transcript text
    full_text = '\n'.join([p['text'] for p in transcript_pages])
    
    # Group instructions mapping
    group_instructions = {
        (1, 3): ("다음을 듣고 알맞은 그림을 고르십시오.", "Nghe và chọn tranh phù hợp."),
        (4, 8): ("다음 대화를 잘 듣고 이어질 수 있는 말을 고르십시오.", "Nghe hội thoại và chọn câu nói có thể tiếp theo."),
        (9, 12): ("다음 대화를 잘 듣고 여자가 이어서 할 행동으로 알맞은 것을 고르십시오.", "Nghe hội thoại và chọn hành động tiếp theo của nữ."),
        (13, 16): ("다음을 듣고 내용과 일치하는 것을 고르십시오.", "Nghe và chọn nội dung khớp."),
        (17, 20): ("다음을 듣고 남자의 중심 생각을 고르십시오.", "Nghe và chọn suy nghĩ trung tâm của nam."),
        (21, 22): ("다음을 듣고 물음에 답하십시오.", "Nghe và trả lời câu hỏi."),
        (23, 24): ("다음을 듣고 물음에 답하십시오.", "Nghe và trả lời câu hỏi."),
        (25, 26): ("다음을 듣고 물음에 답하십시오.", "Nghe và trả lời câu hỏi."),
        (27, 28): ("다음을 듣고 물음에 답하십시오.", "Nghe và trả lời câu hỏi."),
        (29, 30): ("다음을 듣고 물음에 답하십시오.", "Nghe và trả lời câu hỏi."),
        (31, 32): ("다음을 듣고 물음에 답하십시오.", "Nghe và trả lời câu hỏi."),
        (33, 34): ("다음을 듣고 물음에답하십시오.", "Nghe và trả lời câu hỏi."),
        (35, 36): ("다음을 듣고 물음에 답하십시오.", "Nghe và trả lời câu hỏi."),
        (37, 38): ("다음은 교양 프로그램입니다. 잘 듣고 물음에 답하십시오.", "Đây là chương trình giáo dục. Nghe kỹ và trả lời câu hỏi."),
        (39, 40): ("다음은 대담입니다. 잘 듣고 물음에답하십시오.", "Đây là cuộc tọa đàm. Nghe kỹ và trả lời câu hỏi."),
        (41, 42): ("다음은 강연입니다. 잘 듣고 물음에 답하십시오.", "Đây là bài giảng. Nghe kỹ và trả lời câu hỏi."),
        (43, 44): ("다음은 다큐멘터리입니다. 잘 듣고 물음에 답하십시오.", "Đây là phim tài liệu. Nghe kỹ và trả lời câu hỏi."),
        (45, 46): ("다음은 강연입니다. 잘 듣고 물음에 답하십시오.", "Đây là bài giảng. Nghe kỹ và trả lời câu hỏi."),
        (47, 48): ("다음은 대담입니다. 잘 듣고 물음에답하십시오.", "Đây là cuộc tọa đàm. Nghe kỹ và trả lời câu hỏi."),
        (49, 50): ("다음은 강연입니다. 잘 듣고 물음에 답하십시오.", "Đây là bài giảng. Nghe kỹ và trả lời câu hỏi."),
    }
    
    # Parse each question from transcript
    # Questions are separated by number pattern like "1. 여자:" or "21. 남자:"
    # Some questions have sub-questions (21-22, 23-24, etc.)
    
    # Split by question numbers
    lines = full_text.split('\n')
    
    current_question_num = None
    current_text_lines = []
    all_question_texts = {}
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Check for question number at start
        match = re.match(r'^(\d+)\.\s', line)
        if match:
            if current_question_num and current_text_lines:
                all_question_texts[current_question_num] = '\n'.join(current_text_lines)
            current_question_num = int(match.group(1))
            current_text_lines = [line]
        elif current_question_num:
            # Check if this line is a choice (starts with ①②③④)
            if re.match(r'^[①②③④]', line):
                continue
            # Check if this is a sub-question line (like "21. 남자의 중심 생각...")
            sub_match = re.match(r'^(\d+)\.\s', line)
            if sub_match and int(sub_match.group(1)) != current_question_num:
                # Save current and start new
                if current_text_lines:
                    all_question_texts[current_question_num] = '\n'.join(current_text_lines)
                current_question_num = int(sub_match.group(1))
                current_text_lines = [line]
            else:
                current_text_lines.append(line)
    
    if current_question_num and current_text_lines:
        all_question_texts[current_question_num] = '\n'.join(current_text_lines)
    
    # Now build the questions list
    for qid in range(1, 51):
        # Get group instruction
        group_ko = ""
        group_vi = ""
        for (start, end), (ko, vi) in group_instructions.items():
            if start <= qid <= end:
                group_ko = ko
                group_vi = vi
                break
        
        # Get question text from transcript
        question_text = all_question_texts.get(qid, "")
        
        # Clean up question text - remove the number prefix and choices
        question_lines = []
        for line in question_text.split('\n'):
            line = line.strip()
            # Remove question number prefix
            line = re.sub(r'^\d+\.\s*(여자|남자):\s*', '', line)
            if line and not re.match(r'^[①②③④]', line) and not re.match(r'^\d+$', line):
                question_lines.append(line)
        
        question_ko = '\n'.join(question_lines)
        
        # For questions with sub-questions (21-22, 23-24, etc.), extract the actual question
        if qid in [21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]:
            # These are the first of paired questions
            # Extract the question text that comes before the numbered sub-questions
            parts = question_ko.split(f'\n{qid+1}.')
            if len(parts) > 1:
                question_ko = parts[0].strip()
        
        # Build choices (text choices for most, image choices for 1-3)
        if qid <= 3:
            choices = [
                {"type": "image", "text": "①", "image": f"/images/topik/35/page3-img{(qid-1)*4+1}.jpeg"},
                {"type": "image", "text": "②", "image": f"/images/topik/35/page3-img{(qid-1)*4+2}.jpeg"},
                {"type": "image", "text": "③", "image": f"/images/topik/35/page3-img{(qid-1)*4+3}.jpeg"},
                {"type": "image", "text": "④", "image": f"/images/topik/35/page3-img{(qid-1)*4+4}.jpeg"},
            ]
        else:
            choices = ["", "", "", ""]  # Will be filled from reading/listening PDF
        
        questions.append({
            "id": qid,
            "group_instruction": group_ko,
            "group_instruction_vi": group_vi,
            "question_ko": question_ko,
            "choices": choices,
            "answer": listening_answers[qid]
        })
    
    return questions

# ── Parse reading questions ──
def parse_reading(reading_pages):
    """Parse reading questions from reading PDF pages."""
    questions = []
    
    # Combine all reading text (skip first 2 pages - cover and instructions)
    full_text = '\n'.join([p['text'] for p in reading_pages[2:]])
    
    # Group instructions
    group_instructions = {
        (1, 2): ("[1～2] ( )에 들어갈 가장 알맞은 것을 고르십시오.", "[1～2] Chọn đáp án phù hợp nhất vào chỗ trống."),
        (3, 4): ("[3～4] 다음 밑줄 친 부분과 의미가 비슷한 것을 고르십시오.", "[3～4] Chọn đáp án có nghĩa tương tự với phần gạch chân."),
        (5, 8): ("[5～8] 다음은 무엇에 대한 글인지 고르십시오.", "[5～8] Chọn bài viết nói về điều gì."),
        (9, 12): ("[9～12] 다음 글 또는 도표의 내용과 같은 것을 고르십시오.", "[9～12] Chọn nội dung khớp với bài viết hoặc biểu đồ."),
        (13, 15): ("[13～15] 다음을 순서대로 맞게 배열한 것을 고르십시오.", "[13～15] Chọn cách sắp xếp đúng thứ tự."),
        (16, 18): ("[16～18] 다음을 읽고 ( )에 들어갈 내용으로 가장 알맞은 것을 고르십시오.", "[16～18] Đọc và chọn nội dung phù hợp nhất vào chỗ trống."),
        (19, 20): ("[19～20] 다음을 읽고 물음에 답하십시오.", "[19～20] Đọc và trả lời câu hỏi."),
        (21, 22): ("[21～22] 다음을 읽고 물음에 답하십시오.", "[21～22] Đọc và trả lời câu hỏi."),
        (23, 24): ("[23～24] 다음을 읽고 물음에 답하십시오.", "[23～24] Đọc và trả lời câu hỏi."),
        (25, 27): ("[25～27] 다음은 신문 기사의 제목입니다. 가장 잘 설명한 것을 고르십시오.", "[25～27] Đây là tiêu đề bài báo. Chọn lời giải thích đúng nhất."),
        (28, 31): ("[28～31] 다음을 읽고 ( )에 들어갈 내용으로 가장 알맞은 것을 고르십시오.", "[28～31] Đọc và chọn nội dung phù hợp nhất vào chỗ trống."),
        (32, 34): ("[32～34] 다음을 읽고 내용이 같은 것을 고르십시오.", "[32～34] Đọc và chọn nội dung giống nhau."),
        (35, 37): ("[35～37] 다음을 읽고 물음에 답하십시오.", "[35～37] Đọc và trả lời câu hỏi."),
        (38, 40): ("[38～40] 다음을 읽고 ( )에 들어갈 내용으로 가장 알맞은 것을 고르십시오.", "[38～40] Đọc và chọn nội dung phù hợp nhất vào chỗ trống."),
        (41, 41): ("[41] 다음 글의 주제로 가장 알맞은 것을 고르십시오.", "[41] Chọn chủ đề phù hợp nhất cho bài viết."),
        (42, 43): ("[42～43] 다음을 읽고 물음에답하십시오.", "[42～43] Đọc và trả lời câu hỏi."),
        (44, 45): ("[44～45] 다음을 읽고 물음에 답하십시오.", "[44～45] Đọc và trả lời câu hỏi."),
        (46, 47): ("[46～47] 다음을 읽고 물음에 답하십시오.", "[46～47] Đọc và trả lời câu hỏi."),
        (48, 50): ("[48～50] 다음을 읽고 물음에 답하십시오.", "[48～50] Đọc và trả lời câu hỏi."),
    }
    
    # For reading questions, we need to extract from the reading PDF
    # The structure is complex with passages and multiple questions per passage
    # Let's create a simplified version that captures the key info
    
    for qid in range(1, 51):
        group_ko = ""
        group_vi = ""
        for (start, end), (ko, vi) in group_instructions.items():
            if start <= qid <= end:
                group_ko = ko
                group_vi = vi
                break
        
        questions.append({
            "id": qid,
            "group_instruction": group_ko,
            "group_instruction_vi": group_vi,
            "question_ko": "",  # Will be filled manually or from more detailed parsing
            "choices": ["", "", "", ""],
            "answer": reading_answers[qid]
        })
    
    return questions

# ── Build final JSON ──
listening_questions = parse_listening(transcript_pages)
reading_questions = parse_reading(reading_pages)

# Writing questions from answers PDF
writing_questions = [
    {
        "id": 51,
        "question_ko": "무료로 드립니다\n\n저는 유학생인데 공부를 마치고 다음 주에 고향으로 돌아갑니다. 그래서 지금 ( ㉠ ). 책상, 의자, 컴퓨터, 경영학 전공 책 등이 있습니다. 이번 주 금요일까지 방을 비워 줘야 합니다. ( ㉡ ). 제 전화번호는 010-1234-5678입니다.",
        "question_vi": "Cho miễn phí\n\nTôi là du học sinh, tuần sau tôi về quê. Vì vậy bây giờ ( ㉠ ). Có bàn, ghế, máy tính, sách chuyên ngành quản trị kinh doanh v.v. Tôi cần dọn phòng trước thứ Sáu tuần này. ( ㉡ ). Số điện thoại của tôi là 010-1234-5678.",
        "choices": [],
        "answer": "",
        "model_answer": "㉠ 그동안 사용했던 제 물건들을 정리하려고 합니다\n㉡ 그러니까 물건이 필요하신 분들은 금요일 전까지 연락해 주시기 바랍니다",
        "points": 10
    },
    {
        "id": 52,
        "question_ko": "퍼즐은 여러 개의 조각을 모두 제 위치에 놓아야 하나의 그림이 완성된다. 그런데 만일 ( ㉠ ). 사회와 개인의 관계도 마찬가지이다. 사회를 구성하는 모든 개인도 있어야 할 자리에 있어야 한다. 그래야 ( ㉡ ).",
        "question_vi": "Tranh ghép hình phải đặt tất cả các mảnh vào đúng vị trí thì bức tranh mới hoàn thành. Nhưng nếu ( ㉠ ). Quan hệ giữa xã hội và cá nhân cũng tương tự. Tất cả các cá nhân tạo thành xã hội cũng phải ở đúng vị trí của mình. Như vậy thì ( ㉡ ).",
        "choices": [],
        "answer": "",
        "model_answer": "㉠ 퍼즐 조각이 제 자리에 놓이지 않으면 그림은 완성되지 않는다\n㉡ 비로소 사회가 하나로 돌아가기 때문이다",
        "points": 10
    },
    {
        "id": 53,
        "question_ko": "30대와 60대 성인 남녀 500명을 대상으로 '필요하다고 생각하는 공공시설'에 대해 설문 조사를 하였다.\n\n다음 그래프를 보고, 연령대에 따라 필요하다고 생각하는 공공시설이 무엇인지 비교하여 그에 대한 자신의 생각을 200～300자로 쓰십시오.",
        "question_vi": "Cuộc khảo sát đã được thực hiện trên 500 người trưởng thành nam nữ ở độ tuổi 30 và 60 về 'cơ sở công cộng cần thiết'.\n\nNhìn biểu đồ sau, so sánh các cơ sở công cộng cần thiết theo độ tuổi và viết suy nghĩ của bạn trong 200-300 chữ.",
        "choices": [],
        "answer": "",
        "model_answer": "30대와 60대 성인 남녀를 대상으로 필요하다고 생각하는 공공시설에 대한 설문조사를 실시하였다. 조사 결과 30대의 경우 공연장·문화센터가 40%로 가장 높게 나타났으며 병원·약국이 28%로 그 뒤를 이었다. 반면에 60대는 병원·약국이 전체의 절반 수준인 50%로 가장 높게 나타났으며 공연장·문화센터가 23%로 조사되었다. 공원 시설의 필요성에 대한 견해는 30대와 60대가 22%로 동일하게 나타났다. 이상의 설문 조사 결과를 통해 자신의 나이와 직접적으로 관계가 있는 공공시설에 대한 요구가 상대적으로 크다는 사실을 알 수 있다.",
        "points": 30,
        "minChars": 200,
        "maxChars": 300
    },
    {
        "id": 54,
        "question_ko": "사람들은 다양한 경제 수준의 삶을 살고 있으며 그러한 삶에 대해 느끼는 각자의 만족도도 다양하다. 그러나 경제적 여유와 행복 만족도가 꼭 비례한다고는 할 수 없다. 경제적 여유가 행복에 미치는 영향에 대해 아래의 내용을 중심으로 자신의 생각을 600～700자로 쓰십시오.\n\n∙사람들이 생각하는 행복한 삶이란 무엇인가?\n∙경제적 조건과 행복 만족도의 관계는 어떠한가?\n∙행복 만족도를 높이기 위해 어떠한 노력이 필요한가?",
        "question_vi": "Mọi người sống ở nhiều mức kinh tế khác nhau và mức độ hài lòng về cuộc sống cũng khác nhau. Tuy nhiên, sự dư dả kinh tế và mức độ hài lòng về hạnh phúc không nhất thiết tỷ lệ thuận. Hãy viết suy nghĩ của bạn về tác động của sự dư dả kinh tế đến hạnh phúc trong 600-700 chữ, tập trung vào các nội dung sau:\n\n∙Cuộc sống hạnh phúc theo mọi người là gì?\n∙Mối quan hệ giữa điều kiện kinh tế và mức độ hài lòng về hạnh phúc như thế nào?\n∙Cần nỗ lực gì để nâng cao mức độ hài lòng về hạnh phúc?",
        "choices": [],
        "answer": "",
        "model_answer": "일반적으로 사람들은 경제적으로 여유가 있으면 다른 사람들보다 더 행복할 것이라고 생각한다. 그러나 반드시 그러한 것은 아니다. 굴지의 기업 총수라고 해서 특별히 더 행복해 보이지 않는 것만 보더라도 그 사실을 잘 알 수 있다. 경제적 여유가 정신적 안정과 만족을 가져오는 것은 아니다.\n\n물론 행복해지려면 어느 정도의 경제적인 조건은 요구된다. 사람에게 필수적인 의식주가 해결되지 않은 상황에서는 행복의 크기가 경제력과 비례 관계에 있다고 볼 수도 있다. 그러나 의식주가 큰 문제가 되지 않는 요즈음, '먹고 살 걱정'에서 놓여난 다음 잉여의 경제력을 어떻게 처리하느냐의 문제를 두고 고민할 필요가 있다. 배고픈 예술가가 행복할 것이라고 여기는 사람은 별로 없을 것이다. 그렇다고 해서 배만 부른 부자가 되기를 원하는 사람도 별로 없다. 결국 행복이란 안락한 생활과 스스로 만족하는 삶에서 느낄 수 있는 것이다.\n\n행복해지기 위해서",
        "points": 50,
        "minChars": 600,
        "maxChars": 700
    }
]

# Build the final exam JSON
exam_data = {
    "meta": {
        "title": "Đề thi thử TOPIK II - Kỳ 35",
        "level": "TOPIK II",
        "duration": 110,
        "totalQuestions": 54,
        "description": "Đề thi thử TOPIK II dựa trên kỳ thi lần thứ 35 (제35회)"
    },
    "sections": [
        {
            "type": "listening",
            "title": "듣기 (Nghe)",
            "duration": 60,
            "audio": "/audio/topik/TOPIK-2-35-audio.mp3",
            "questions": listening_questions
        },
        {
            "type": "reading",
            "title": "읽기 (Đọc)",
            "duration": 50,
            "questions": reading_questions
        },
        {
            "type": "writing",
            "title": "쓰기 (Viết)",
            "duration": 50,
            "questions": writing_questions
        }
    ]
}

# Save to file
output_path = r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"✅ Saved to {output_path}")
print(f"   Listening: {len(listening_questions)} questions")
print(f"   Reading: {len(reading_questions)} questions")
print(f"   Writing: {len(writing_questions)} questions")
print(f"   Total: {len(listening_questions) + len(reading_questions) + len(writing_questions)} questions")
