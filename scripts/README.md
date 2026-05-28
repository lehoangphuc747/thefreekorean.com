# Scripts tiện ích

Thư mục này chứa script chạy tay (Python) phục vụ chỉnh sửa dữ liệu Anki/JSON, không dùng trong build Astro.

## Tra cứu nhanh

| Script | Việc làm | Lệnh chạy (từ thư mục gốc repo) |
|--------|----------|----------------------------------|
| `update_question_instruction.py` | Gán một `question_instruction` cố định cho toàn bộ item trong `id-13-82-new.json` | `python scripts/update_question_instruction.py` |
| `optimize_explain.py` | Đổi `explain` từ Markdown sang HTML đơn giản trong `id-13-82-new.json` | `python scripts/optimize_explain.py` |
| `csv_vocab_seoul_1b_sheet9_to_json.py` | CSV từ vựng Anki/SpreadsheetImportPlus → JSON (`pandas`) | `pip install -r scripts/requirements-tools.txt` rồi `python scripts/csv_vocab_seoul_1b_sheet9_to_json.py` |

Hoặc dùng npm (Windows/macOS/Linux nếu `python` có trong PATH):

- `npm run tool:update-question-instruction`
- `npm run tool:optimize-explain`
- `npm run tool:vocab-csv-to-json`

**Phụ thuộc Python:** các script dùng `pandas` cần cài một lần: `pip install -r scripts/requirements-tools.txt`.

## Metadata máy đọc được

File `manifest.json` liệt kê cùng nội dung dạng JSON (id, tag, input/output) — tiện cho tool hoặc tìm kiếm nhanh trong editor.

## Ghi chú

- Các script resolve đường dẫn JSON theo **thư mục gốc repo** (cha của `scripts/`), nên có thể chạy từ bất kỳ đâu: `python path/to/repo/scripts/...` vẫn trỏ đúng file ở root.
- Nếu chưa có `id-13-82-new.json` ở root, script sẽ báo lỗi khi chạy — đặt file hoặc sửa tên file trong code cho khớp bài làm của bạn.

## Metadata trong từng file

Mỗi script Python có khối docstring đầu file mô tả mục đích, file vào/ra và lệnh chạy — mở file là thấy ngay, không cần nhớ hết README.
