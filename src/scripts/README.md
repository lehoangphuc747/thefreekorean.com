# Scripts Documentation

Thư mục `src/scripts` chứa các script trợ giúp phát triển/biên tập dữ liệu nội dung.

## Danh sách script
- `validateGrammar.ts`: (đang khởi tạo) Dự kiến dùng để kiểm tra cấu trúc dữ liệu/ngữ pháp trong các bài viết ngữ pháp (slug, trường bắt buộc, liên kết nội bộ, v.v.).

## Định hướng triển khai `validateGrammar.ts`
- Đầu vào: duyệt qua `src/pages/ngu-phap/**` hoặc nguồn dữ liệu tương ứng.
- Kiểm tra:
  - Tồn tại các trường bắt buộc (tiêu đề, slug, mô tả, thẻ, cấp độ...).
  - Tính hợp lệ của liên kết ảnh/PDF (điểm vào `public/`).
  - Tính nhất quán của slug với cấu trúc thư mục.
- Đầu ra: in báo cáo ra console (summary + chi tiết lỗi/warn).

## Cách chạy script (gợi ý)
Dự án dùng TypeScript, có thể chạy bằng `tsx` hoặc `ts-node`.

```bash
# Chạy tạm bằng npx tsx (không cần cài global)
npx tsx src/scripts/validateGrammar.ts

# Hoặc dùng ts-node
npx ts-node src/scripts/validateGrammar.ts
```

Gợi ý thêm vào `package.json`:
```json
{
  "scripts": {
    "validate:grammar": "tsx src/scripts/validateGrammar.ts"
  }
}
```

## Lưu ý
- Script không nên sửa file nội dung khi chưa có cờ (flag) xác nhận (ví dụ `--fix`).
- Tránh phụ thuộc vào component/runtime; chỉ thao tác với file dữ liệu/nội dung.
