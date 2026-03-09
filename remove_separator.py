import json

# Đọc file
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Loại bỏ --- separator
for item in data:
    if 'explain' in item and item['explain']:
        # Loại bỏ các pattern của dấu ---
        item['explain'] = item['explain'].replace('<p>---</p>', '')
        item['explain'] = item['explain'].replace('<p>---<br/></p>', '')
        item['explain'] = item['explain'].replace('<p><br/>---</p>', '')
        item['explain'] = item['explain'].replace('<p><br/>---<br/></p>', '')
        # Loại bỏ thừa <p></p> rỗng
        item['explain'] = item['explain'].replace('<p></p>', '')

# Lưu file
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Loại bỏ --- separator trong tất cả {len(data)} items!")
print(f"   Phần '❌ Các đáp án sai' với màu đỏ đã đủ để phân biệt")
