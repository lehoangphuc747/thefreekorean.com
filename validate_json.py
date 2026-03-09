import json

print("=" * 60)
print("KIỂM TRA FILE JSON")
print("=" * 60)

try:
    with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"✅ JSON format hợp lệ")
    print(f"\n📊 Thống kê:")
    print(f"   - Tổng số items: {len(data)}")
    
    # Kiểm tra các fields
    required_fields = ['id', 'topik', 'test', 'format_type', 'question_type', 
                       'question_form', 'question_instruction', 'question', 
                       'correct', 'answer_a', 'answer_b', 'answer_c', 'answer_d', 
                       'explain', 'tag_1', 'tag_2', 'tag_3', 'tag_4']
    
    missing_fields = []
    for idx, item in enumerate(data):
        for field in required_fields:
            if field not in item:
                missing_fields.append(f"Item {idx}: {field}")
    
    if missing_fields:
        print(f"\n❌ Missing fields:")
        for mf in missing_fields[:10]:
            print(f"   - {mf}")
        if len(missing_fields) > 10:
            print(f"   ... và {len(missing_fields) - 10} trường khác")
    else:
        print(f"✅ Tất cả {len(required_fields)} fields bắt buộc đều có đầy đủ")
    
    # Kiểm tra empty fields
    empty_check = {}
    for field in required_fields:
        empty_count = 0
        for item in data:
            if not item.get(field):
                empty_count += 1
        if empty_count > 0:
            empty_check[field] = empty_count
    
    if empty_check:
        print(f"\n⚠️  Fields trống:")
        for field, count in empty_check.items():
            print(f"   - {field}: {count} items")
    else:
        print(f"✅ Không có field trống")
    
    # Kiểm tra correct values
    correct_values = set()
    for item in data:
        correct_values.add(item.get('correct'))
    print(f"\n✅ Correct values: {sorted(correct_values)}")
    
    # Kiểm tra duplicate IDs
    ids = [item['id'] for item in data]
    if len(ids) != len(set(ids)):
        print(f"❌ Có ID bị duplicate!")
    else:
        print(f"✅ Tất cả ID đều unique")
    
    # Hiển thị mẫu first item
    print(f"\n📝 Mẫu item đầu tiên:")
    first_item = data[0]
    for key in ['id', 'topik', 'test', 'format_type', 'question_type', 'correct']:
        print(f"   {key}: {first_item.get(key)}")
    
    print(f"\n{'=' * 60}")
    print(f"✅ FILE SẴN SÀNG!")
    print(f"{'=' * 60}")
    
except json.JSONDecodeError as e:
    print(f"❌ JSON format không hợp lệ: {e}")
except Exception as e:
    print(f"❌ Lỗi: {e}")
