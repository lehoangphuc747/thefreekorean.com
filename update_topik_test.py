import json

# Đọc file
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Cập nhật
for item in data:
    # test = giá trị cũ của topik (종결어미, 연결어미, 연습)
    item['test'] = item['topik']
    # topik = "TOPIK II" (cố định)
    item['topik'] = "TOPIK II"

# Lưu file
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Thống kê
test_types = {}
for item in data:
    test_val = item['test']
    test_types[test_val] = test_types.get(test_val, 0) + 1

print("✅ Cập nhật thành công!\n")
print(f"topik: 'TOPIK II' (tất cả {len(data)} items)")
print(f"\ntest distribution:")
for test_type, count in sorted(test_types.items()):
    print(f"  - {test_type}: {count}")
