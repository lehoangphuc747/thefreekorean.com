import json

# Đọc file
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Cập nhật: thay \n bằng <br/>
for item in data:
    if 'question_instruction' in item and item['question_instruction']:
        # Thay \n bằng <br/>
        item['question_instruction'] = item['question_instruction'].replace('\n', '<br/>')
    
    if 'explain' in item and item['explain']:
        # Thay \n bằng <br/> trong explain
        item['explain'] = item['explain'].replace('\n', '<br/>')

# Lưu file
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Thay thế \\n bằng <br/> trong tất cả {len(data)} items!")
print(f"   - question_instruction fields")
print(f"   - explain fields")
