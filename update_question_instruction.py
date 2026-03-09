import json

# Đọc file
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Cập nhật
question_instruction = """🚀 Mẹo giải nhanh Dạng 1 (Ngữ pháp điền khuyết)
⏱️ Tối ưu thời gian: Mục tiêu giải nhanh < 30 giây/câu.
🎯 Trọng tâm: Xác định chính xác mối quan hệ ngữ pháp (Điều kiện, nguyên nhân, lựa chọn...) giữa hai vế câu.
💡 Các bước làm nhanh: 
1. Phân tích: Chỉ cần đọc và xem từ loại (động từ/tính từ) ngay trước khoảng trống và hành động/kết quả ở vế sau. 
2. Loại trừ (Tense/Rule): Bỏ ngay các cấu trúc sai về thì (quá khứ/hiện tại) hoặc sai về nguyên tắc chia (dùng cho A/V). 
3. Kiểm tra: Dịch nhẩm nhanh để đảm bảo cấu trúc đã chọn mang lại ý nghĩa logic cho cả câu."""

for item in data:
    item['question_instruction'] = question_instruction

# Lưu file
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Cập nhật {len(data)} items!")
print(f"   question_instruction: (Mẹo giải nhanh Dạng 1)")
