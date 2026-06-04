import json
import re

def parse_section(text_lines, section_type, start_q, end_q):
    questions = []
    
    current_q = None
    group_instruction = ""
    group_instruction_vi = ""
    
    i = 0
    while i < len(text_lines):
        line = text_lines[i].strip()
        if not line:
            i += 1
            continue
            
        # Match group instructions like "※ [1~2] ( )에 들어갈 가장 알맞은 것을 고르십시오."
        group_match = re.match(r'※?\s*\[(\d+)~(\d+)\]\s*(.+)', line)
        if group_match:
            group_instruction = group_match.group(3).strip()
            # Vietnamese placeholder
            group_instruction_vi = ""
            i += 1
            continue
            
        # Match question number "1", "2", "50"
        if line.isdigit():
            q_num = int(line)
            if start_q <= q_num <= end_q:
                # New Question
                if current_q:
                    questions.append(current_q)
                
                current_q = {
                    "id": q_num,
                    "group_instruction": group_instruction if group_instruction else None,
                    "group_instruction_vi": group_instruction_vi if group_instruction_vi else None,
                    "question_ko": "",
                    "choices": [],
                    "correct_answer": 1 # To be filled or ignored for simulation
                }
                
                # Next line is usually instruction again
                i += 1
                if i < len(text_lines):
                    instr_line = text_lines[i].strip()
                    if "고르십시오" in instr_line or instr_line == "2점":
                        # Skip
                        i += 1
                        if i < len(text_lines) and text_lines[i].strip() == "2점":
                            i += 1
                
                # Now we collect the question text until we see choice "1"
                q_text = []
                while i < len(text_lines) and text_lines[i].strip() != "1":
                    # Check if it mentions an image
                    if "Question" in text_lines[i] and "image" in text_lines[i]:
                        q_text.append(f"[IMAGE_PLACEHOLDER: q{q_num}]")
                    else:
                        q_text.append(text_lines[i].strip())
                    i += 1
                
                current_q["question_ko"] = "\n".join(q_text).strip()
                
                # Now collect 4 choices
                for choice_num in range(1, 5):
                    if i < len(text_lines) and text_lines[i].strip() == str(choice_num):
                        i += 1
                        choice_text = ""
                        if i < len(text_lines):
                            if "Option" in text_lines[i] and "for Q" in text_lines[i]:
                                choice_text = f"[IMAGE_CHOICE_PLACEHOLDER: q{q_num}_c{choice_num}]"
                            else:
                                choice_text = text_lines[i].strip()
                        current_q["choices"].append({
                            "type": "text" if "IMAGE_" not in choice_text else "image",
                            "text": choice_text if "IMAGE_" not in choice_text else "",
                            "image": choice_text if "IMAGE_" in choice_text else None
                        })
                        i += 1
                continue
                
        i += 1
        
    if current_q:
        questions.append(current_q)
        
    return questions

# 1. Parse Reading
with open('scripts/topik36-reading-raw.txt', 'r', encoding='utf-8') as f:
    reading_lines = f.readlines()
reading_questions = parse_section(reading_lines, "reading", 1, 50)

# 2. Parse Listening
with open('scripts/topik36-listening-raw.txt', 'r', encoding='utf-8') as f:
    listening_lines = f.readlines()
listening_questions = parse_section(listening_lines, "listening", 1, 50)

# Shift reading ID from 1-50 to 1-50 but listening is 1-50 too, let's keep them as is 
# because in TOPIK II, Reading is Q1-Q50 of the reading section.

# 3. Build the final JSON structure
exam_json = {
  "meta": {
    "title": "Đề thi thử TOPIK II - Kỳ 36",
    "level": "TOPIK II",
    "duration": 110,
    "totalQuestions": 104,
    "description": "Đề thi thử TOPIK II dựa trên kỳ thi chính thức 36."
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
      "questions": [
        {
          "id": 51,
          "question_ko": "[Writing Question 51 Placeholder]",
          "type": "short_answer",
          "points": 10
        },
        {
          "id": 52,
          "question_ko": "[Writing Question 52 Placeholder]",
          "type": "short_answer",
          "points": 10
        },
        {
          "id": 53,
          "question_ko": "[Writing Question 53 Placeholder]",
          "type": "essay",
          "points": 30
        },
        {
          "id": 54,
          "question_ko": "[Writing Question 54 Placeholder]",
          "type": "essay",
          "points": 50
        }
      ]
    },
    {
      "type": "reading",
      "title": "읽기 (Đọc)",
      "duration": 70,
      "questions": reading_questions
    }
  ]
}

# 4. Save to content directory
output_file = 'src/content/topik/thi-thu/topik2-thi-thu-36.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(exam_json, f, ensure_ascii=False, indent=2)

print(f"Successfully generated JSON for TOPIK 36 with {len(listening_questions)} listening and {len(reading_questions)} reading questions.")
print(f"File saved to {output_file}")
