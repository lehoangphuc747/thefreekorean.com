import json
import re

print("🔧 Sửa lỗi JSON...\n")

# Đọc file raw để kiểm tra
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Kiểm tra dấu phẩy dư thừa trước }
# Loại bỏ dấu phẩy dư thừa trước `},`
content = re.sub(r',(\s*}(?:\s*,|\s*\]))', r'\1', content)

# Loại bỏ dấu phẩy dư thừa trước ]
content = re.sub(r',(\s*\])', r'\1', content)

# Loại bỏ ký tự sau ]
content = re.sub(r'\]([^\s])', r']\1', content)

# Thử load JSON để kiểm tra
try:
    data = json.loads(content)
    print("✅ JSON format hợp lệ sau khi sửa!")
    print(f"   Items: {len(data)}")
    
    # Lưu file đã sửa
    with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("\n✅ File đã được lưu!")
    
except json.JSONDecodeError as e:
    print(f"❌ Lỗi JSON: {e}")
    print(f"Position: {e.pos}")
    print(f"Line: {e.lineno}, Column: {e.colno}")
