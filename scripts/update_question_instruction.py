"""
Script: update_question_instruction
Mục đích: Ghi đồng loạt trường question_instruction cho mọi item trong JSON Anki.

File vào/ra: id-13-82-new.json (nằm ở thư mục gốc repo, cùng cấp với thư mục scripts/).

Chạy (từ thư mục gốc repo):
  python scripts/update_question_instruction.py

Tags: anki, json, batch
"""

import json
from pathlib import Path

# Thư mục gốc repo = cha của thư mục scripts/ — để chạy script ở đâu cũng tìm đúng JSON
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = REPO_ROOT / "id-13-82-new.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# Nội dung hướng dẫn giải nhanh gán cho tất cả item
question_instruction = """🚀 Mẹo giải nhanh Dạng 1 (Ngữ pháp điền khuyết)
⏱️ Tối ưu thời gian: Mục tiêu giải nhanh < 30 giây/câu.
🎯 Trọng tâm: Xác định chính xác mối quan hệ ngữ pháp (Điều kiện, nguyên nhân, lựa chọn...) giữa hai vế câu.
💡 Các bước làm nhanh: 
1. Phân tích: Chỉ cần đọc và xem từ loại (động từ/tính từ) ngay trước khoảng trống và hành động/kết quả ở vế sau. 
2. Loại trừ (Tense/Rule): Bỏ ngay các cấu trúc sai về thì (quá khứ/hiện tại) hoặc sai về nguyên tắc chia (dùng cho A/V). 
3. Kiểm tra: Dịch nhẩm nhanh để đảm bảo cấu trúc đã chọn mang lại ý nghĩa logic cho cả câu."""

for item in data:
    item["question_instruction"] = question_instruction

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Cập nhật {len(data)} items!")
print("   question_instruction: (Mẹo giải nhanh Dạng 1)")
