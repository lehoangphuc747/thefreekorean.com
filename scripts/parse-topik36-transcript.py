import json
import re

# Common speaker patterns in TOPIK transcripts
SPEAKER_PATTERN = r'^(여자|남자|남|여|어르신|직원|의사|교사|부장|행인|강사|선생님|선생|학생)\s*:\s*(.*)'

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

def parse_transcripts_line_by_line():
    transcripts = {}
    
    with open('public/downloads/topik/TOPIK II/36/TOPIK-2-36-transcript-utf8.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Standardize spaces and split into lines, ignoring page borders
    raw_lines = content.split('\n')
    lines = []
    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        if "--- PAGE" in line or "제36회" in line or "B형" in line or "듣기 통합" in line:
            continue
        lines.append(line)
        
    # We want to iterate and find:
    # "1.", "2.", "3." up to "50."
    # Everything after "X." until we hit choice marks "①" or instruction "※" or next question number
    # belongs to question X's dialogue.
    
    current_q = None
    dialogue_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Match question start like "21.남자의..." or just "21."
        q_match = re.match(r'^(\d+)\.(.*)', line)
        if q_match:
            q_num = int(q_match.group(1))
            rest = q_match.group(2).strip()
            
            if 1 <= q_num <= 50:
                # Save previous question dialogue
                if current_q and dialogue_lines:
                    transcripts[current_q] = clean_dialogue_flow(dialogue_lines)
                
                current_q = q_num
                dialogue_lines = []
                if rest and not any(rest.startswith(c) for c in ['①', '②', '③', '④', '➀', '➁', '➂', '➃']):
                    dialogue_lines.append(rest)
                i += 1
                continue
                
        # If we are collecting dialogue for current_q
        if current_q is not None:
            # Stop if we hit choices or instruction
            is_choice = any(line.startswith(char) for char in ['①', '②', '③', '④', '➀', '➁', '➂', '➃'])
            is_instruction = "※" in line or "다음을 듣고" in line or "다음 대화를" in line
            
            if is_choice or is_instruction:
                # Save current and reset
                transcripts[current_q] = clean_dialogue_flow(dialogue_lines)
                current_q = None
                dialogue_lines = []
            else:
                dialogue_lines.append(line)
                
        i += 1
        
    if current_q and dialogue_lines:
        transcripts[current_q] = clean_dialogue_flow(dialogue_lines)
        
    return transcripts

# Run parser
transcripts = parse_transcripts_line_by_line()
print("Extracted transcripts count:", len(transcripts))
print("Sample Q4 transcript:\n", transcripts.get(4))
print("Sample Q5 transcript:\n", transcripts.get(5))

# Merge transcripts into the main JSON
json_path = 'src/content/topik/thi-thu/topik2-thi-thu-36.json'
with open(json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# Update listening questions with transcripts
listening_sec = next(s for s in exam_data["sections"] if s["type"] == "listening")
for q in listening_sec["questions"]:
    q_id = q["id"]
    if q_id in transcripts:
        q["question_ko"] = transcripts[q_id]
    else:
        # If missing, it means it's a paired question (e.g. Q22, Q24...)
        # We will handle pairing below
        pass

# Listening pairings mapping (Q21-50 are paired, sharing the same transcript)
for q_id in range(22, 51, 2):
    paired_q = next((q for q in listening_sec["questions"] if q["id"] == q_id), None)
    base_q = next((q for q in listening_sec["questions"] if q["id"] == q_id - 1), None)
    if paired_q and base_q and "question_ko" in base_q:
        paired_q["question_ko"] = base_q["question_ko"]

# Save updated JSON
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print(f"Successfully integrated formatted transcripts into {json_path}")
