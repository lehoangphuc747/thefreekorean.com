import json

# Đọc file
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Cập nhật tags
for item in data:
    # Thay thế dấu cách bằng dấu gạch dưới
    topik_tag = item['topik'].replace(' ', '_')
    test_tag = item['test'].replace(' ', '_')
    format_tag = item['format_type'].replace(' ', '_')
    question_tag = item['question_type'].replace(' ', '_')
    
    # Gán vào từng tag
    item['tag_1'] = topik_tag
    item['tag_2'] = test_tag
    item['tag_3'] = format_tag
    item['tag_4'] = question_tag

# Lưu file
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Hiển thị mẫu
print(f"✅ Cập nhật {len(data)} items!")
print(f"\nFormat: tag_1::tag_2::tag_3::tag_4")
print(f"Ví dụ:")
print(f"  tag_1: {data[0]['tag_1']}")
print(f"  tag_2: {data[0]['tag_2']}")
print(f"  tag_3: {data[0]['tag_3']}")
print(f"  tag_4: {data[0]['tag_4']}")
