# Layouts Documentation

Thư mục `src/layouts` chứa các bố cục (layout) cấp trang dùng để bao bọc nội dung và chia sẻ phần giao diện chung như NavBar, Footer, global styles.

## Danh sách file
- `Layout.astro`: Layout chung cho toàn site (NavBar, Footer, ScrollToTop, global.css, thẻ `<title>` mặc định).
- `TopikLayout.astro`: Layout chuyên biệt cho khu vực TOPIK (header riêng, điều hướng con, mobile menu), bọc bên trong `Layout.astro`.

## Layout.astro
- Import: `NavBar`, `Footer`, `ScrollToTop`, `../styles/global.css`.
- Cấu trúc: bọc `<slot />` giữa `NavBar` và `Footer`.
- SEO: có thẻ `<title>` mặc định: "The Free Korean - Tài liệu học tiếng Hàn miễn phí".

Cách dùng (trong trang `.astro`):
```astro
---
import Layout from '@/layouts/Layout.astro';
---

<Layout>
  <main>
    <!-- Nội dung trang -->
  </main>
</Layout>
```

## TopikLayout.astro
- Mục đích: Bố cục cho các trang thuộc khu vực TOPIK với header, điều hướng nhanh, và responsive mobile menu.
- Bao bọc: Dùng `Layout.astro` bên ngoài để giữ NavBar/Footer thống nhất.
- Props:
  - `title?: string` (mặc định: `TOPIK`)
  - `description?: string` (mặc định: `Luyện thi TOPIK - Test of Proficiency in Korean`)
  - `showBackButton?: boolean` (mặc định: `true`) – hiển thị nút "Quay lại" về `/topik`
  - `showNavigation?: boolean` (mặc định: `true`) – hiển thị điều hướng: Tổng quan, Luyện tập, Từ vựng, Đề thi
  - `class?: string` – thêm CSS classes vào wrapper chính

Lưu ý:
- `TopikLayout` tính `fullTitle` phục vụ hiển thị/SEO. Hiện `Layout.astro` thiết lập `<title>` mặc định, nên nếu cần "title động" cho trang TOPIK bạn có thể cân nhắc cập nhật `Layout.astro` để nhận và sử dụng prop `title`/`description`.

Cách dùng:
```astro
---
import TopikLayout from '@/layouts/TopikLayout.astro';
---

<TopikLayout title="TOPIK I 2023" description="Luyện đề TOPIK I 2023" showBackButton={true} showNavigation={true} class="custom-page">
  <section class="max-w-7xl mx-auto p-4">
    <!-- Nội dung trang TOPIK -->
  </section>
</TopikLayout>
```

### Điều hướng trong TopikLayout
- Desktop: hiển thị thanh điều hướng trên header.
- Mobile: có nút menu (hamburger) để toggle danh sách liên kết, kèm script xử lý toggle và tự đóng khi click ngoài.

## Thực hành tốt
- Đặt nội dung trang vào `<slot />` thay vì thêm trực tiếp vào layout.
- Với các trang TOPIK, dùng `TopikLayout.astro` để có giao diện, điều hướng, và trải nghiệm nhất quán.
- Nếu cần tuỳ biến SEO, có thể mở rộng `Layout.astro` để nhận `title`/`description` từ props, sau đó truyền từ các layout con.
