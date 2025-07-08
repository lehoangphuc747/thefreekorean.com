# The Free Korean - Tài liệu học tiếng Hàn miễn phí

Website tổng hợp tài liệu học tiếng Hàn miễn phí được xây dựng bằng Astro.

## 🚀 Cài đặt và chạy project

```sh
npm install
npm run dev
```

Truy cập `localhost:4321` để xem website.

## 📁 Chi tiết cấu trúc Project

### 🗂️ Thư mục chính

```text
/
├── public/
│   ├── favicon.svg
│   ├── images/              # Hình ảnh cover của tài liệu
│   │   └── tieng-han-tong-hop-1.jpg
│   └── downloads/           # File tải về (nếu lưu local)
├── src/
│   ├── assets/
│   │   ├── astro.svg
│   │   └── background.svg
│   ├── components/          # Các component tái sử dụng
│   │   ├── DocumentsList.jsx        # Danh sách tài liệu động
│   │   ├── DownloadSection.astro    # Section tải về cho từng tài liệu
│   │   ├── FeaturesSection.astro    # Section tính năng
│   │   ├── Footer.astro             # Footer chung
│   │   ├── IntroSection.astro       # Section giới thiệu
│   │   ├── NavBar.astro             # Navigation bar
│   │   ├── RoadmapSection.astro     # Section lộ trình học
│   │   ├── Slides.jsx               # Slideshow tài liệu
│   │   └── Welcome.astro            # Component welcome
│   ├── documents/           # Tài liệu MDX
│   │   ├── hangul-video.mdx         # Tài liệu video Hangul
│   │   ├── huong-dan.mdx            # Hướng dẫn sử dụng
│   │   ├── itopik-website.mdx       # Website iTOPIK
│   │   ├── seoul-korean-1a.mdx      # Seoul Korean 1A
│   │   ├── tai-lieu.mdx             # Tài liệu tổng quan
│   │   ├── tieng-han-tong-hop-1.mdx # Tiếng Hàn Tổng Hợp Sơ cấp 1
│   │   └── topik-vocabulary.mdx     # Từ vựng TOPIK
│   ├── layouts/
│   │   └── Layout.astro             # Layout chung
│   ├── pages/
│   │   ├── documents/
│   │   │   └── [slug].astro         # Dynamic routing cho tài liệu
│   │   ├── index.astro              # Trang chủ
│   │   └── tai-lieu.astro           # Trang danh sách tài liệu
│   └── styles/
│       └── global.css               # CSS global
├── astro.config.mjs
├── package.json
├── tsconfig.json
└── README.md
```

## 📝 Hướng dẫn thêm tài liệu mới

### 1. Tạo file MDX cho tài liệu

Tạo file trong `src/documents/` với format:

```markdown
---
title: "Tên tài liệu"
date: 2024-05-01
category: "Giáo trình" | "Website" | "Video"
subcategory: "Phân loại chi tiết"
type: "PDF" | "Website" | "Video" 
cover: "/images/ten-file-hinh.jpg"
description: "Mô tả ngắn về tài liệu"
downloadUrl: "Link tải chính" 
downloadOriginal: "Link file gốc (optional)"
downloadWorkbook: "Link sách bài tập (optional)"
downloadAudio: "Link file nghe (optional)"
fileSize: "Kích thước file"
originalSize: "Kích thước file gốc (optional)"
workbookSize: "Kích thước SBT (optional)"
audioSize: "Kích thước audio (optional)"
pages: 250
features: ["Tính năng 1", "Tính năng 2"] # (optional)
---

# Nội dung tài liệu

Viết nội dung bằng Markdown...
```

### 2. Thêm hình ảnh cover

- Đặt file hình vào `public/images/`
- Đặt tên file trùng với slug của tài liệu
- Format: JPG, PNG, SVG
- Kích thước khuyến nghị: 300x400px

### 3. Các loại tài liệu được hỗ trợ

#### 📚 PDF (Sách/Giáo trình)
```yaml
type: "PDF"
downloadUrl: "Link file nén"      # Hiển thị với icon 📚 primary
downloadOriginal: "Link gốc"     # Hiển thị với icon 📚
downloadWorkbook: "Link SBT"     # Hiển thị với icon 📝  
downloadAudio: "Link audio"      # Hiển thị với icon 🎵
```

#### 🌐 Website
```yaml
type: "Website"
downloadUrl: "https://website.com"  # Hiển thị với icon 🌐
```

#### 📹 Video
```yaml
type: "Video" 
downloadUrl: "https://youtube.com/watch?v=..."  # Hiển thị với icon 📹
```

### 4. Component DownloadSection

- Tự động detect loại tài liệu từ `type`
- Hiển thị multiple download options
- Click vào card để tải về/truy cập
- Responsive design

### 5. Routing tự động

- File `ten-tai-lieu.mdx` → URL `/documents/ten-tai-lieu`
- Tự động tạo breadcrumb
- Dynamic routing qua `[slug].astro`

## 🎨 Customization

### Thêm category mới

1. Cập nhật filter trong `tai-lieu.astro`
2. Thêm style cho category badge
3. Cập nhật metadata trong MDX

### Thêm component mới

1. Tạo file `.astro` trong `src/components/`
2. Import vào page cần sử dụng
3. Tái sử dụng across pages

## 🚀 Deployment

### Deploy lên GitHub Pages

1. Push code lên GitHub
2. Cấu hình GitHub Pages
3. Astro tự động build

### Deploy lên Netlify/Vercel

1. Connect GitHub repo
2. Build command: `npm run build`
3. Publish directory: `dist/`

## 🔧 Development Tips

- Sử dụng `npm run dev` để live reload
- File MDX hỗ trợ JSX components
- CSS scoped tự động trong `.astro` files
- TypeScript support built-in

## 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
│   └── favicon.svg
├── src
│   ├── assets
│   │   └── astro.svg
│   ├── components
│   │   └── Welcome.astro
│   ├── layouts
│   │   └── Layout.astro
│   └── pages
│       └── index.astro
└── package.json
```

To learn more about the folder structure of an Astro project, refer to [our guide on project structure](https://docs.astro.build/en/basics/project-structure/).

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).
