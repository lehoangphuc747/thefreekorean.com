<!-- 30bfd3d6-1aa2-467c-ad29-d45dfdb8437b a30e3cc2-1327-413b-b13c-efd27fa1a7d3 -->
# Tạo trang Grammar cơ bản

## Tổng quan

Tạo 1 trang và 2 layout mới cho chức năng ngữ pháp, sử dụng cấu trúc tương tự Layout.astro hiện có.

## Các file cần tạo

### 1. `src/content/config.ts`

- Tạo/cập nhật file config cho Astro Content Collections
- Định nghĩa schema cho grammar collection với các field:
  - title (string)
  - meaning (string)
  - level (enum: "beginner", "intermediate", "advanced")
  - slug (string)
  - description (string)
  - tags (array of strings)
  - order (number) - Thứ tự hiển thị trong cùng level

### 2. `src/content/grammar/`

- Tạo thư mục mới để chứa các file markdown ngữ pháp
- Cấu trúc frontmatter:
```yaml
title: "N입니다"
meaning: "là N"
level: "beginner"
slug: "N입니다"
description: "..."
tags: ["giới thiệu"]
```


### 3. `src/layouts/GrammarLayout.astro`

- Layout cho trang chính grammar.astro
- Có NavBar, Footer, ScrollToTop
- Import global.css
- Có slot để chứa nội dung
- Cấu trúc tương tự `Layout.astro`

### 4. `src/layouts/GrammarPostLayout.astro`

- Layout cho các trang chi tiết bài ngữ pháp
- Có NavBar, Footer, ScrollToTop
- Import global.css
- Layout 2 cột: Sidebar bên trái + Nội dung chi tiết bên phải
- Sidebar hiển thị danh sách ngữ pháp (đọc từ content collection)
- Có nút ẩn/hiện sidebar
- Highlight ngữ pháp đang được chọn trong sidebar
- Có slot để chứa nội dung chi tiết

### 5. `src/pages/grammar.astro`

- Trang chính với tiêu đề "NGỮ PHÁP"
- Sử dụng GrammarLayout
- Layout 2 cột: Sidebar bên trái + Nội dung chính bên phải
- **SEO:** Meta tags cơ bản (title: "Ngữ pháp tiếng Hàn", description: "Danh sách ngữ pháp...")
- **Switch button 4 nút**: TẤT CẢ, SƠ CẤP, TRUNG CẤP, CAO CẤP (đặt trên ô search)
- **Switch button Grid/List**: Ở góc phải trên cùng của vùng hiển thị GrammarCard
  - Grid mode: Hiển thị GrammarCard dạng lưới (3-4 cột tùy độ rộng màn hình)
  - List mode: Hiển thị GrammarCard dạng danh sách (1 cột, full width)
  - **Preference:** Lưu lựa chọn vào localStorage
- Có khung tìm kiếm (search box) với chức năng tìm kiếm thật
- Tìm kiếm trong các file ngữ pháp từ `src/content/grammar/`
- Nội dung chính: Hiển thị các GrammarCard (mặc định hiển thị tất cả, khi search thì hiển thị kết quả)
- **Responsive:**
  - Desktop: Sidebar bên trái + GrammarCard grid/list bên phải (mặc định: grid)
  - Tablet: Giống desktop
  - Mobile: Sidebar ẩn mặc định (nút hamburger mở overlay/drawer) + GrammarCard list full width (mặc định: list)

### 6. `src/components/common/ImageViewer.astro`

- Component chung xử lý hình ảnh trong markdown
- **Chức năng:**
  - Hiển thị ảnh responsive (max-width: 100%, height: auto)
  - Caption tự động từ alt text (hiển thị dưới hình)
  - Click vào ảnh → mở lightbox/modal
  - Lightbox có: nút đóng (X), nút prev/next (nếu nhiều ảnh), zoom in/out
- **Cách sử dụng:** Tự động wrap tất cả `<img>` trong `.markdown-content` bằng JavaScript
- **Hình ảnh trong markdown:** Lưu tại `public/images/`, sử dụng cú pháp `![Alt text](/images/example.webp)`

### 7. `src/components/common/PDFGenerator.astro`

- Component riêng xử lý tạo PDF từ markdown
- **Chức năng:**
  - Render PDF trực tiếp từ markdown (không qua HTML)
  - Watermark: Logo mờ ở background (góc dưới phải, opacity 10-15%)
  - Header: Logo + "The Free Korean" + "Ngữ pháp tiếng Hàn"
  - Footer: "thefreekorean.com" + số trang
  - Tên file: `thefreekorean.com-[slug].pdf`
- **Cách sử dụng:** Import vào trang grammar post, truyền markdown content
- **Styling:** Print-friendly, brand colors, typography đẹp

### 7. `src/styles/markdown.css`

- File CSS riêng cho styling markdown content
- Chứa styling cho các element: h1, h2, h3, h4, h5, h6, p, ul, ol, li, code, pre, table, blockquote, hr, strong, em, a, img...
- **Xử lý links:**
  - Internal links: `[Text](/grammar/beginner/slug)` - link tuyệt đối, không có icon
  - External links: Tự động thêm `target="_blank"` và `rel="noopener noreferrer"` bằng JavaScript, màu giống internal link
  - Tự động phát hiện external link: bắt đầu bằng `http://` hoặc `https://`
- Styling cơ bản, dễ đọc

### 7. `src/pages/grammar/[level]/[slug].astro`

- Trang chi tiết ngữ pháp (route mới với level trong URL)
- URL structure: `/grammar/beginner/[slug]`, `/grammar/intermediate/[slug]`, `/grammar/advanced/[slug]`
- Sử dụng GrammarPostLayout
- Import `src/styles/markdown.css`
- Đọc nội dung từ content collection theo slug
- **SEO:** Meta tags (title, description, keywords) lấy từ frontmatter
- **Breadcrumb Navigation:** Hiển thị ở đầu trang (trên nút "Quay lại")
  - Format: Home > Ngữ pháp > [Level] > [Title]
  - Ví dụ: Home > Ngữ pháp > Sơ cấp > N입니다
- **Nút "Quay lại":** Icon mũi tên + text "Quay lại" → link về `/grammar`
  - Vị trí: Ở đầu bài viết (dưới Breadcrumb, trên Grammar Info) và ở cuối bài viết
- **Share Button:** Dưới Grammar Info
  - Copy link bài viết
  - Chia sẻ lên Facebook, Messenger, Instagram, Threads
- **Print-friendly CSS:** Thêm CSS cho in ấn bài viết
  - Ẩn navbar, footer, sidebar, TOC, tất cả buttons khi in
  - Tối ưu typography cho in ấn
  - Nút "In bài viết" (mở print dialog)
- **Nút "Tải PDF":** Bên cạnh nút "In bài viết" (cùng hàng)
  - Render PDF trực tiếp từ markdown (không qua HTML)
  - Tạo PDF có styling đẹp (giống trang web)
  - Chỉ nội dung markdown (không có navbar, sidebar, TOC...)
  - **Watermark:** Logo mờ ở background (góc dưới phải, opacity 10-15%)
  - **Header:** Logo + "The Free Korean" + "Ngữ pháp tiếng Hàn"
  - **Footer:** "thefreekorean.com" + số trang
  - Tên file: `thefreekorean.com-[slug].pdf` (ví dụ: `thefreekorean.com-N입니다.pdf`)
- Hiển thị Grammar Info ở đầu bài viết (sau nút quay lại, trước nội dung markdown):
  - Dạng header lớn với title
  - Các badge hiển thị: level, tags (từ frontmatter)
  - Hiển thị meaning, description
- **TOC (Table of Contents):**
  - Desktop: Layout 3 cột - Sidebar (trái) + Content (giữa) + TOC (phải), sticky sidebar, tự động generate từ headings, có nút ẩn/hiện TOC
  - Mobile: Hiển thị ở đầu bài viết, khi scroll xuống → nút floating góc phải → click mở sidebar trượt từ phải
- Render markdown content trong container có class markdown
- Wrap content: `<div class="markdown-content">...</div>`
- **Nút "Tiếp theo/Trước đó":** Ở cuối nội dung markdown (trước "Ngữ pháp liên quan")
  - Chỉ hiển thị nút "← Trước" và "Tiếp →"
  - Logic: Sắp xếp theo level (beginner → intermediate → advanced), trong mỗi level sắp xếp theo order
  - Ví dụ: Beginner order 3 → Tiếp → Beginner order 4; Beginner cuối → Tiếp → Intermediate order 1
- **Ngữ pháp liên quan:** Hiển thị sau nút "Tiếp theo/Trước đó"
  - Hiển thị 3 ngữ pháp liên quan
  - Lấy dựa trên: Cùng tags (ưu tiên) → Cùng level
  - Hiển thị dạng list đơn giản: title + meaning

### 7. GrammarCard Component

- Component hiển thị thông tin ngữ pháp (title + meaning)
- Click vào card chuyển đến `/grammar/[slug]`
- Styling cơ bản, responsive

### 8. Sidebar Component

- Hiển thị danh sách ngữ pháp theo cấp độ được chọn từ switch button
- Mỗi item hiển thị: title + meaning (từ frontmatter)
- Click vào item sẽ chuyển đến `/grammar/[slug]`
- Danh sách sắp xếp theo thứ tự

### 8. Component tìm kiếm

- Tạo component search cơ bản tương tự SearchComponent.astro
- Đọc dữ liệu từ content collection
- **Logic tìm kiếm:** Tìm trong title (tiếng Hàn) + meaning (tiếng Việt) + tags
  - Ví dụ: Gõ "입니다" → tìm trong title
  - Ví dụ: Gõ "muốn" → tìm trong meaning
  - Ví dụ: Gõ "giới thiệu" → tìm trong tags
- Hiển thị kết quả dạng GrammarCard (grid/list tùy chế độ đang chọn)
- Tích hợp với switch button để lọc theo cấp độ
- Hiển thị số lượng kết quả tìm thấy

### 9. Sitemap

- Tạo sitemap.xml tự động cho các trang grammar
- Bao gồm: `/grammar`, `/grammar/beginner/[slug]`, `/grammar/intermediate/[slug]`, `/grammar/advanced/[slug]`

### 10. Xóa các file cũ

- Xóa tất cả file .astro trong `src/pages/ngu-phap/` (sau khi tạo xong content collection)

## Lưu ý

- Chỉ tạo sườn cơ bản, không thêm chức năng ngoài yêu cầu
- Không cần styling phức tạp
- Sử dụng các component có sẵn (NavBar, Footer, ScrollToTop)