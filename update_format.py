import json

# Đọc file
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Cập nhật
for item in data:
    item['format_type'] = "ĐỌC"
    item['question_type'] = "DẠNG 01"

# Lưu file
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Cập nhật {len(data)} items!")
print(f"   format_type: 'ĐỌC'")
print(f"   question_type: 'DẠNG 01'")
