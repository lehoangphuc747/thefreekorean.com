#!/usr/bin/env python3
"""Parse TOPIK II Exam 35 Reading questions - improved version."""
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load raw reading data
with open(r'D:\A Web\the-free-korean\scripts\topik35-reading-raw.json', 'r', encoding='utf-8') as f:
    reading_pages = json.load(f)

# Answer key
reading_answers = {
    1:3, 2:4, 3:1, 4:1, 5:1, 6:2, 7:1, 8:3, 9:4, 10:1,
    11:2, 12:3, 13:1, 14:4, 15:4, 16:2, 17:3, 18:3, 19:2, 20:4,
    21:1, 22:2, 23:1, 24:3, 25:3, 26:1, 27:4, 28:3, 29:4, 30:4,
    31:1, 32:2, 33:4, 34:4, 35:2, 36:2, 37:4, 38:4, 39:2, 40:3,
    41:3, 42:1, 43:2, 44:2, 45:3, 46:2, 47:3, 48:2, 49:1, 50:4
}

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
    (35, 38): ("[35～38] 다음 글의 주제로 가장 알맞은 것을 고르십시오.", "[35～38] Chọn chủ đề phù hợp nhất cho bài viết."),
    (39, 41): ("[39～41] 다음 글에서 <보기>의 문장이 들어가기에 가장 알맞은 곳을 고르십시오.", "[39～41] Chọn vị trí phù hợp nhất cho câu trong phần <보기>."),
    (42, 43): ("[42～43] 다음을 읽고 물음에 답하십시오.", "[42～43] Đọc và trả lời câu hỏi."),
    (44, 45): ("[44～45] 다음을 읽고 물음에 답하십시오.", "[44～45] Đọc và trả lời câu hỏi."),
    (46, 47): ("[46～47] 다음을 읽고 물음에 답하십시오.", "[46～47] Đọc và trả lời câu hỏi."),
    (48, 50): ("[48～50] 다음을 읽고 물음에답하십시오.", "[48～50] Đọc và trả lời câu hỏi."),
}

# Manually define question blocks for complex cases
# These are questions that share passages or have special formats
question_blocks = {
    # Q5-8: "다음은 무엇에 대한 글인지" - need to find the passage text
    # Q9-12: "다음 글 또는 도표의 내용과 같은 것을" - need passage
    # Q19-20: share a passage about fruit
    # Q21-22: share a passage about choices
    # Q23-24: share a passage about company
    # Q42-43: share a passage about diving
    # Q44-45: share a passage about emissions
    # Q46-47: share a passage about merger
    # Q48-50: share a passage about privacy
}

# Combine all text
full_text = '\n'.join([p['text'] for p in reading_pages[2:]])

# Parse all questions
questions = {}

# Find all question numbers
q_pattern = re.compile(r'(?:^|\n)(\d+)\.\s')
q_matches = list(q_pattern.finditer(full_text))

for i, match in enumerate(q_matches):
    qid = int(match.group(1))
    if qid < 1 or qid > 50:
        continue
    
    start = match.start()
    if i + 1 < len(q_matches):
        end = q_matches[i + 1].start()
    else:
        end = len(full_text)
    
    block = full_text[start:end].strip()
    
    # Get group instruction
    group_ko = ""
    group_vi = ""
    for (sr, er), (ko, vi) in group_instructions.items():
        if sr <= qid <= er:
            group_ko = ko
            group_vi = vi
            break
    
    # Parse choices
    choice_parts = re.split(r'[①②③④]', block)
    
    if len(choice_parts) >= 5:
        # Has 4 choices
        q_text = re.sub(r'^\d+\.\s*', '', choice_parts[0]).strip()
        choices = [part.strip().rstrip('\n').strip() for part in choice_parts[1:5]]
        
        questions[qid] = {
            "id": qid,
            "group_instruction": group_ko,
            "group_instruction_vi": group_vi,
            "question_ko": q_text,
            "choices": choices,
            "answer": reading_answers[qid]
        }
    else:
        # No clear choices - might be a passage or sub-question
        q_text = re.sub(r'^\d+\.\s*', '', block).strip()
        
        # Check if this is a sub-question (like 19, 20, 21, 22, etc.)
        # These often have a passage followed by the actual question
        if qid in [19, 20, 21, 22, 23, 24, 42, 43, 44, 45, 46, 47, 48, 49, 50]:
            # Find the actual question within the passage
            # Look for patterns like "19.(" or "21.("
            sub_match = re.search(rf'{qid}\.\s*[\(（]', q_text)
            if sub_match:
                # The question text starts after the passage
                passage = q_text[:sub_match.start()].strip()
                q_text = q_text[sub_match.start():].strip()
                
                # Now extract choices from q_text
                sub_choices = re.split(r'[①②③④]', q_text)
                if len(sub_choices) >= 5:
                    q_text = re.sub(r'^\d+\.\s*', '', sub_choices[0]).strip()
                    choices = [part.strip() for part in sub_choices[1:5]]
                else:
                    choices = []
                
                questions[qid] = {
                    "id": qid,
                    "group_instruction": group_ko,
                    "group_instruction_vi": group_vi,
                    "question_ko": q_text,
                    "choices": choices,
                    "answer": reading_answers[qid]
                }
            else:
                # Just store the whole text
                questions[qid] = {
                    "id": qid,
                    "group_instruction": group_ko,
                    "group_instruction_vi": group_vi,
                    "question_ko": q_text[:500],
                    "choices": [],
                    "answer": reading_answers[qid]
                }
        else:
            questions[qid] = {
                "id": qid,
                "group_instruction": group_ko,
                "group_instruction_vi": group_vi,
                "question_ko": q_text[:500],
                "choices": [],
                "answer": reading_answers[qid]
            }

# Fill in missing questions
for qid in range(1, 51):
    if qid not in questions:
        group_ko = ""
        group_vi = ""
        for (sr, er), (ko, vi) in group_instructions.items():
            if sr <= qid <= er:
                group_ko = ko
                group_vi = vi
                break
        
        questions[qid] = {
            "id": qid,
            "group_instruction": group_ko,
            "group_instruction_vi": group_vi,
            "question_ko": "",
            "choices": [],
            "answer": reading_answers[qid]
        }

# Convert to sorted list
questions_list = [questions[qid] for qid in sorted(questions.keys())]

# Load existing JSON
with open(r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json', 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# Update reading section
exam_data['sections'][1]['questions'] = questions_list

# Save
with open(r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json', 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"✅ Updated reading section: {len(questions_list)} questions")
print(f"   Questions with text: {sum(1 for q in questions_list if q['question_ko'])}")
print(f"   Questions with choices: {sum(1 for q in questions_list if q['choices'])}")

# Show questions without text
empty = [q['id'] for q in questions_list if not q['question_ko']]
if empty:
    print(f"   Empty questions: {empty}")
