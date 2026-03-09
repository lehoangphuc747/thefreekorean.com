import json

# Đọc file
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Mapping
mapping = {1: 'A', 2: 'B', 3: 'C', 4: 'D'}

# Cập nhật
for item in data:
    old_correct = item['correct']
    if old_correct in mapping:
        item['correct'] = mapping[old_correct]

# Lưu file
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Cập nhật {len(data)} items!")
print(f"   Mapping: 1→A, 2→B, 3→C, 4→D")
