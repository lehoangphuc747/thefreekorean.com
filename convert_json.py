import json

# Đọc file cũ
with open('id-13-82.json', 'r', encoding='utf-8') as f:
    old_data = json.load(f)

# Chuyển đổi
new_data = []

for q in old_data['questions']:
    new_item = {
        "id": str(q.get('id', '')),
        "topik": q.get('exam', ''),
        "test": "",
        "format_type": "",
        "question_type": "",
        "question_form": "",
        "question_instruction": "",
        "question": q.get('question_ko', ''),
        "question_image": "",
        "question_audio": "",
        "correct": q.get('answer', ''),
        "answer_a": q['choices'][0]['text'] if len(q.get('choices', [])) > 0 else "",
        "answer_b": q['choices'][1]['text'] if len(q.get('choices', [])) > 1 else "",
        "answer_c": q['choices'][2]['text'] if len(q.get('choices', [])) > 2 else "",
        "answer_d": q['choices'][3]['text'] if len(q.get('choices', [])) > 3 else "",
        "explain": q.get('explain', ''),
        "tag_1": "",
        "tag_2": "",
        "tag_3": "",
        "tag_4": ""
    }
    new_data.append(new_item)

# Lưu file mới
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(new_data, f, ensure_ascii=False, indent=2)

print(f"✅ Chuyển đổi thành công! {len(new_data)} items")
print("File mới: id-13-82-new.json")
