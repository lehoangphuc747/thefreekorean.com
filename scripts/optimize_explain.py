"""
Script: optimize_explain
Mục đích: Chuyển trường explain từ Markdown sang HTML đơn giản trong JSON Anki (hiển thị Anki đẹp hơn).

File vào/ra: id-13-82-new.json (nằm ở thư mục gốc repo).

Chạy (từ thư mục gốc repo):
  python scripts/optimize_explain.py

Tags: anki, json, html

Lưu ý: Hàm format_explain_to_html giữ lại để tái dùng / thử pipeline HTML chi tiết; vòng lặp chính hiện dùng bước thay thế trực tiếp như bản gốc.
"""

import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = REPO_ROOT / "id-13-82-new.json"

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)


def format_explain_to_html(explain_text):
    """Chuyển đổi explain từ Markdown sang HTML với tối ưu hóa"""

    # Loại bỏ ### và tạo H3
    explain_text = explain_text.replace("### ✅ Đáp án đúng\n\n", "")

    # Tách phần correct answer và phần wrong answers
    parts = explain_text.split("### ❌ Các đáp án sai")

    correct_part = parts[0].strip() if len(parts) > 0 else ""
    wrong_part = parts[1].strip() if len(parts) > 1 else ""

    html = '<div class="explanation">\n'

    # ===== PHẦN ĐÁNG ÁN ĐÚNG =====
    html += '  <div class="correct-answer">\n'
    html += "    <h3>✅ Đáp án đúng</h3>\n"

    # Tìm và xử lý dòng đầu tiên (chứa đáp án và giải thích ngữ pháp)
    lines = correct_part.split("\n")
    if len(lines) > 0:
        first_line = lines[0].strip()
        # Format: **answer** — meaning `pattern`: description
        match = re.match(r"\*\*(.+?)\*\*\s*—\s*(.*?)`(.+?)`:\s*(.*)", first_line)
        if match:
            answer = match.group(1)
            meaning = match.group(2).strip()
            pattern = match.group(3)
            description = match.group(4)

            html += f'    <p><strong style="color: #0066cc; font-size: 1.1em;">{answer}</strong></p>\n'
            html += f"    <p><strong>Ngữ pháp:</strong> <code>{pattern}</code></p>\n"
            html += f"    <p><strong>Ý nghĩa:</strong> {meaning} - {description}</p>\n"

    # Phần ví dụ
    if len(lines) > 1:
        for line in lines[1:]:
            line = line.strip()
            if line.startswith("🗣️"):
                # Ví dụ câu
                example = line.replace("🗣️ **Ví dụ:** ", "").replace("**Ví dụ:** ", "")
                html += f'    <p style="margin-top: 10px;"><strong>📌 Ví dụ:</strong><br/><em>{example}</em></p>\n'
            elif line.startswith("📖"):
                # Dịch nghĩa
                translation = line.replace("📖 **Dịch nghĩa:** ", "").replace("**Dịch nghĩa:** ", "")
                html += f'    <p><strong>🌐 Dịch nghĩa:</strong><br/><em style="color: #333;">{translation}</em></p>\n'
            elif line.startswith("⚡"):
                # Hiểu nhanh
                quick_understand = line.replace("⚡ **Hiểu nhanh:** ", "").replace("**Hiểu nhanh:** ", "")
                html += f'    <p><strong style="color: #ff6b6b;">💡 Hiểu nhanh:</strong> {quick_understand}</p>\n'

    html += "  </div>\n\n"

    # ===== PHẦN ĐÁP ÁN SAI =====
    if wrong_part:
        html += '  <div class="wrong-answers" style="background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin-top: 15px;">\n'
        html += "    <h4>❌ Các đáp án sai</h4>\n"

        # Tách từng đáp án sai
        wrong_answers = wrong_part.split("\n- ")

        for wrong_answer in wrong_answers:
            if wrong_answer.strip():
                wrong_answer = wrong_answer.strip()
                # Format: **answer**: meaning → emoji `pattern` = description → reason
                match = re.match(
                    r"\*\*(.+?)\*\*:\s*(.*?)\s*→\s*(.*?)`(.+?)`\s*=\s*(.*?)\s*→\s*(.*)",
                    wrong_answer,
                )
                if match:
                    answer = match.group(1)
                    meaning = match.group(2).strip()
                    pattern = match.group(4)
                    pattern_explain = match.group(5).strip()
                    final_reason = match.group(6).strip()

                    html += '    <div style="margin-bottom: 12px; padding: 10px; background-color: white; border-left: 3px solid #ff6b6b;">\n'
                    html += f'      <p><strong style="color: #d63031;">{answer}:</strong> {meaning}</p>\n'
                    html += f'      <p style="margin: 5px 0; font-size: 0.95em;"><code>V-{pattern}</code> = {pattern_explain}</p>\n'
                    html += f'      <p style="margin: 5px 0; color: #666; font-size: 0.9em;">⚠️ <strong>Lý do:</strong> {final_reason}</p>\n'
                    html += "    </div>\n"

        html += "  </div>\n"

    html += "</div>\n"

    return html


# Cập nhật explain cho tất cả items
count = 0
for item in data:
    if item.get("explain"):
        # Giữ format hiện tại (markdown) nhưng tối ưu HTML
        original_explain = item["explain"]

        # Convert markdown to simple HTML for better Anki display
        new_explain = original_explain

        # Replace markdown bold to html strong
        new_explain = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", new_explain)

        # Replace headers
        new_explain = new_explain.replace(
            "### ✅ Đáp án đúng",
            '<h3 style="color: #27ae60; border-bottom: 2px solid #27ae60; padding-bottom: 5px;">✅ Đáp án đúng</h3>',
        )
        new_explain = new_explain.replace(
            "### ❌ Các đáp án sai",
            '<h3 style="color: #e74c3c; border-bottom: 2px solid #e74c3c; padding-bottom: 5px; margin-top: 20px;">❌ Các đáp án sai</h3>',
        )

        # Replace line breaks for markdown with <br/>
        new_explain = new_explain.replace("\n\n", "</p><p>")
        new_explain = "<p>" + new_explain + "</p>"

        # Replace dashes with <br/> for better readability
        new_explain = new_explain.replace("- <strong>", "<br/>→ <strong>")

        # Add css styling
        new_explain = f'<div style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">{new_explain}</div>'

        item["explain"] = new_explain
        count += 1

with open(DATA_PATH, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ Tối ưu hóa {count} explain fields!")
print("   - Chuyển đổi markdown bold sang HTML <strong>")
print("   - Cung cấp màu sắc cho đáp án đúng/sai")
print("   - Cải thiện định dạng text")
