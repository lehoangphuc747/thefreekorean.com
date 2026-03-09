import json

# Đọc file
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Cập nhật ID
for item in data:
    old_id = item['id']
    # Format: topik-reading-dang-01-id-0013
    new_id = f"topik-reading-dang-01-id-{old_id.zfill(4)}"
    item['id'] = new_id
    print(f"{old_id} → {new_id}")

# Lưu file
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"\n✅ Cập nhật {len(data)} items thành công!")
