#!/usr/bin/env python3
"""Parse TOPIK II Exam 35 Reading questions from PDF text."""
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

# Combine all text (skip cover and instructions)
full_text = '\n'.join([p['text'] for p in reading_pages[2:]])

# Parse questions by finding patterns
# Pattern: number followed by period, then text, then choices ①②③②
questions = []

# Split text into blocks by question number
# We need to find each question and its choices

# First, let's find all question numbers and their positions
question_pattern = re.compile(r'(?:^|\n)(\d+)\.\s')
question_matches = list(question_pattern.finditer(full_text))

# For each question, extract the text until the next question or end
for i, match in enumerate(question_matches):
    qid = int(match.group(1))
    if qid < 1 or qid > 50:
        continue
    
    start = match.start()
    # Find end (next question or end of text)
    if i + 1 < len(question_matches):
        end = question_matches[i + 1].start()
    else:
        end = len(full_text)
    
    block = full_text[start:end].strip()
    
    # Extract question text and choices
    # Split by ① to find choices
    choice_split = re.split(r'[①②③④]', block)
    
    if len(choice_split) >= 5:
        # First part is the question text
        question_text = choice_split[0].strip()
        # Remove the question number prefix
        question_text = re.sub(r'^\d+\.\s*', '', question_text).strip()
        
        # Extract choices
        choices = []
        for j in range(1, 5):
            choice_text = choice_split[j].strip()
            # Clean up choice text
            choice_text = choice_text.rstrip('\n').strip()
            if choice_text.startswith('－'):
                choice_text = choice_text[1:].strip()
            choices.append(choice_text)
        
        # Get group instruction
        group_ko = ""
        group_vi = ""
        for (start_range, end_range), (ko, vi) in group_instructions.items():
            if start_range <= qid <= end_range:
                group_ko = ko
                group_vi = vi
                break
        
        questions.append({
            "id": qid,
            "group_instruction": group_ko,
            "group_instruction_vi": group_vi,
            "question_ko": question_text,
            "choices": choices,
            "answer": reading_answers[qid]
        })
    else:
        # For questions with sub-questions (like 19-20, 21-22, etc.)
        # We need to handle them differently
        # The question text includes the passage
        question_text = block.strip()
        question_text = re.sub(r'^\d+\.\s*', '', question_text).strip()
        
        # Get group instruction
        group_ko = ""
        group_vi = ""
        for (start_range, end_range), (ko, vi) in group_instructions.items():
            if start_range <= qid <= end_range:
                group_ko = ko
                group_vi = vi
                break
        
        questions.append({
            "id": qid,
            "group_instruction": group_ko,
            "group_instruction_vi": group_vi,
            "question_ko": question_text[:500],  # Limit length
            "choices": [],
            "answer": reading_answers[qid]
        })

# Sort by ID
questions.sort(key=lambda x: x['id'])

# Deduplicate (some questions might be parsed multiple times)
seen_ids = set()
unique_questions = []
for q in questions:
    if q['id'] not in seen_ids:
        seen_ids.add(q['id'])
        unique_questions.append(q)

# Fill in missing questions
for qid in range(1, 51):
    if qid not in seen_ids:
        # Find group instruction
        group_ko = ""
        group_vi = ""
        for (start_range, end_range), (ko, vi) in group_instructions.items():
            if start_range <= qid <= end_range:
                group_ko = ko
                group_vi = vi
                break
        
        unique_questions.append({
            "id": qid,
            "group_instruction": group_ko,
            "group_instruction_vi": group_vi,
            "question_ko": "",
            "choices": [],
            "answer": reading_answers[qid]
        })

# Sort again
unique_questions.sort(key=lambda x: x['id'])

# Load existing JSON
with open(r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json', 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# Update reading section
exam_data['sections'][1]['questions'] = unique_questions

# Save
with open(r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json', 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"✅ Updated reading section: {len(unique_questions)} questions")
print(f"   Questions with text: {sum(1 for q in unique_questions if q['question_ko'])}")
print(f"   Questions with choices: {sum(1 for q in unique_questions if q['choices'])}")

# Show sample
for q in unique_questions[:5]:
    print(f"\nQ{q['id']}:")
    print(f"  Text: {q['question_ko'][:100]}...")
    print(f"  Choices: {q['choices'][:2] if q['choices'] else 'none'}")
    print(f"  Answer: {q['answer']}")
