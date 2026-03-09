import json

# Đọc file
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Cập nhật
question_form = "( )에 들어갈 가장 알맞은 것을 고르십시오."
for item in data:
    item['question_form'] = question_form

# Lưu file
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Cập nhật {len(data)} items!")
print(f"   question_form: '{question_form}'")
