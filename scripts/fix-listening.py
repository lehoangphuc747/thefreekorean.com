#!/usr/bin/env python3
"""Fix listening questions choices from transcript."""
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load transcript
with open(r'D:\A Web\the-free-korean\scripts\topik35-transcript-raw.json', 'r', encoding='utf-8') as f:
    transcript_pages = json.load(f)

# Combine all transcript text
full_text = '\n'.join([p['text'] for p in transcript_pages])

# Answer key
listening_answers = {
    1:2, 2:4, 3:1, 4:2, 5:4, 6:3, 7:2, 8:4, 9:1, 10:3,
    11:1, 12:3, 13:4, 14:4, 15:3, 16:3, 17:1, 18:1, 19:2, 20:1,
    21:2, 22:2, 23:4, 24:3, 25:4, 26:2, 27:2, 28:4, 29:1, 30:3,
    31:4, 32:2, 33:1, 34:2, 35:4, 36:4, 37:2, 38:4, 39:2, 40:1,
    41:3, 42:3, 43:1, 44:3, 45:3, 46:1, 47:1, 48:2, 49:4, 50:3
}

# Group instructions
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
    (31, 32): ("다음을 듣고 물음에답하십시오.", "Nghe và trả lời câu hỏi."),
    (33, 34): ("다음을 듣고 물음에 답하십시오.", "Nghe và trả lời câu hỏi."),
    (35, 36): ("다음을 듣고 물음에 답하십시오.", "Nghe và trả lời câu hỏi."),
    (37, 38): ("다음은 교양 프로그램입니다. 잘 듣고 물음에 답하십시오.", "Đây là chương trình giáo dục. Nghe kỹ và trả lời câu hỏi."),
    (39, 40): ("다음은 대담입니다. 잘 듣고 물음에답하십시오.", "Đây là cuộc tọa đàm. Nghe kỹ và trả lời câu hỏi."),
    (41, 42): ("다음은 강연입니다. 잘 듣고 물음에 답하십시오.", "Đây là bài giảng. Nghe kỹ và trả lời câu hỏi."),
    (43, 44): ("다음은 다큐멘터리입니다. 잘 듣고 물음에 답하십시오.", "Đây là phim tài liệu. Nghe kỹ và trả lời câu hỏi."),
    (45, 46): ("다음은 강연입니다. 잘 듣고 물음에 답하십시오.", "Đây là bài giảng. Nghe kỹ và trả lời câu hỏi."),
    (47, 48): ("다음은 대담입니다. 잘 듣고 물음에답하십시오.", "Đây là cuộc tọa đàm. Nghe kỹ và trả lời câu hỏi."),
    (49, 50): ("다음은 강연입니다. 잘 듣고 물음에 답하십시오.", "Đây là bài giảng. Nghe kỹ và trả lời câu hỏi."),
}

# Parse each question block
# Pattern: "N. " followed by dialogue, then blank line, then choices ①②③④
questions = []

# Split by question numbers at start of line
q_blocks = re.split(r'\n(\d+)\.\s', full_text)

# q_blocks[0] is before first question, then alternating: number, content
for i in range(1, len(q_blocks), 2):
    qid = int(q_blocks[i])
    if qid < 1 or qid > 50:
        continue
    
    content = q_blocks[i+1] if i+1 < len(q_blocks) else ""
    
    # Split content into dialogue and choices
    # Choices start with ①②③④
    choice_match = re.search(r'[①②③④]', content)
    
    if choice_match:
        # Get dialogue (before choices)
        dialogue = content[:choice_match.start()].strip()
        
        # Get choices
        choice_text = content[choice_match.start():]
        choice_parts = re.split(r'[①②③④]', choice_text)
        
        # Clean up choices
        choices = []
        for part in choice_parts[1:5]:  # Skip first empty part, take 4 choices
            clean = part.strip().rstrip('\n').strip()
            if clean.startswith('－'):
                clean = clean[1:].strip()
            choices.append(clean)
        
        # If we have image questions (Q1-3), keep as image choices
        if qid <= 3:
            # These will be handled separately with images
            choices = [
                {"type": "image", "text": "①", "image": f"/images/topik/35/page3-img{(qid-1)*4+1}.jpeg"},
                {"type": "image", "text": "②", "image": f"/images/topik/35/page3-img{(qid-1)*4+2}.jpeg"},
                {"type": "image", "text": "③", "image": f"/images/topik/35/page3-img{(qid-1)*4+3}.jpeg"},
                {"type": "image", "text": "④", "image": f"/images/topik/35/page3-img{(qid-1)*4+4}.jpeg"},
            ]
    else:
        # No choices found - might be image questions
        dialogue = content.strip()
        if qid <= 3:
            choices = [
                {"type": "image", "text": "①", "image": f"/images/topik/35/page3-img{(qid-1)*4+1}.jpeg"},
                {"type": "image", "text": "②", "image": f"/images/topik/35/page3-img{(qid-1)*4+2}.jpeg"},
                {"type": "image", "text": "③", "image": f"/images/topik/35/page3-img{(qid-1)*4+3}.jpeg"},
                {"type": "image", "text": "④", "image": f"/images/topik/35/page3-img{(qid-1)*4+4}.jpeg"},
            ]
        else:
            choices = []
    
    # Clean up dialogue
    dialogue = re.sub(r'^\d+\.\s*', '', dialogue).strip()
    # Remove "여자:" or "남자:" prefix if present
    dialogue = re.sub(r'^(여자|남자):\s*', '', dialogue)
    
    # Get group instruction
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
        "question_ko": dialogue,
        "choices": choices,
        "answer": listening_answers[qid]
    })

# Sort by ID
questions.sort(key=lambda x: x['id'])

# Fill missing questions
for qid in range(1, 51):
    if qid not in [q['id'] for q in questions]:
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
            "question_ko": "",
            "choices": [],
            "answer": listening_answers[qid]
        })

questions.sort(key=lambda x: x['id'])

# Load existing JSON
with open(r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json', 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# Update listening section
exam_data['sections'][0]['questions'] = questions

# Save
with open(r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json', 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

# Also copy to public
import shutil
shutil.copy(
    r'D:\A Web\the-free-korean\src\content\topik\thi-thu\topik2-thi-thu-35.json',
    r'D:\A Web\the-free-korean\public\topik2-thi-thu-35.json'
)

print(f"✅ Updated listening section!")
print(f"   Total: {len(questions)} questions")
print(f"   With choices: {sum(1 for q in questions if q['choices'])}")

# Show sample
for q in questions[3:6]:  # Q4-6
    print(f"\nQ{q['id']}:")
    print(f"  dialogue: {q['question_ko'][:80]}...")
    print(f"  choices: {q['choices'][:2]}...")
