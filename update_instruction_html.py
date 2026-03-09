import json

# Đọc file
with open('id-13-82-new.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# HTML format
question_instruction_html = """<h3>🚀 Mẹo giải nhanh Dạng 1 (Ngữ pháp điền khuyết)</h3>
<p><strong>⏱️ Tối ưu thời gian:</strong> Mục tiêu giải nhanh &lt; 30 giây/câu.</p>
<p><strong>🎯 Trọng tâm:</strong> Xác định chính xác mối quan hệ ngữ pháp (Điều kiện, nguyên nhân, lựa chọn...) giữa hai vế câu.</p>
<p><strong>💡 Các bước làm nhanh:</strong></p>
<ol>
  <li><strong>Phân tích:</strong> Chỉ cần đọc và xem từ loại (động từ/tính từ) ngay trước khoảng trống và hành động/kết quả ở vế sau.</li>
  <li><strong>Loại trừ (Tense/Rule):</strong> Bỏ ngay các cấu trúc sai về thì (quá khứ/hiện tại) hoặc sai về nguyên tắc chia (dùng cho A/V).</li>
  <li><strong>Kiểm tra:</strong> Dịch nhẩm nhanh để đảm bảo cấu trúc đã chọn mang lại ý nghĩa logic cho cả câu.</li>
</ol>"""

# Cập nhật
for item in data:
    item['question_instruction'] = question_instruction_html

# Lưu file
with open('id-13-82-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Cập nhật {len(data)} items sang HTML format!")
print(f"   Sử dụng: <h3>, <strong>, <p>, <ol>, <li>")
