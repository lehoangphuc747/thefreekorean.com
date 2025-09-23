# Styles Documentation

Thư mục `src/styles` chứa các stylesheet toàn cục và theo khu vực.

## Danh sách file
- `global.css`: Định nghĩa style nền tảng áp dụng toàn site (reset/cơ bản) và được import trong `src/layouts/Layout.astro`.
- `navbar.css`: Style chi tiết cho thanh điều hướng (NavBar), các trạng thái, responsive.
- `korean-grammar.css`: Style dành cho trang/bài ngữ pháp (format ví dụ, bảng, nhấn mạnh, layout phần nội dung...).

## Cách sử dụng
- `global.css` đã được import tại `Layout.astro` và áp dụng trên tất cả các trang.
- `navbar.css` thường được import bởi component/khối liên quan đến điều hướng (tuỳ kiến trúc, có thể gộp vào component hoặc layout nếu cần).
- `korean-grammar.css` nên được import ở các trang/bố cục hiển thị bài ngữ pháp để tránh ảnh hưởng ngoài ý muốn.

## Thực hành tốt
- Ưu tiên utility classes (nếu dùng Tailwind) cho layout; CSS thuần để tinh chỉnh chi tiết khó biểu đạt bằng utility.
- Đặt selector đủ cụ thể để không rò rỉ style sang khu vực khác; cân nhắc prefix (vd. `.grammar-page ...`).
- Tránh !important; thay vào đó tăng tính đặc hiệu hợp lý hoặc cấu trúc lại HTML.
- Gom các biến/màu sắc dùng chung (CSS variables) tại một nơi duy nhất nếu có nhu cầu tuỳ biến theme.
