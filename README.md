# The Free Korean - Tài liệu học tiếng Hàn miễn phí

Website tổng hợp tài liệu học tiếng Hàn miễn phí được xây dựng bằng **Astro + Tailwind CSS**.

## 🚀 Quick Start

```bash
# Cài đặt dependencies
npm install

# Chạy development server
npm run dev

# Build production
npm run build

# Preview build
npm run preview
```

Truy cập `http://localhost:4321` để xem website.

## 🏗️ Kiến trúc dự án

### 📁 Cấu trúc thư mục

```text
/
├── public/
│   ├── favicon.svg
│   └── images/                     # Hình ảnh cover của tài liệu
│       └── tieng-han-tong-hop-1.jpg
├── src/
│   ├── assets/                     # Static assets
│   │   ├── astro.svg
│   │   └── background.svg
│   ├── components/                 # Component tái sử dụng
│   │   ├── document/               # Document-specific components
│   │   │   ├── DocumentCard.astro  # Card hiển thị từng tài liệu
│   │   │   ├── DocumentGrid.astro  # Grid layout responsive
│   │   │   └── FilterSection.astro # Bộ lọc category/subcategory
│   │   ├── home/                  # Components for homepage
│   │   │   ├── HeroSection.astro
│   │   │   ├── FeaturesGrid.astro
│   │   │   ├── StatsSection.astro
│   │   │   └── ...
│   │   ├── ui/                     # UI components cơ bản
│   │   │   ├── Badge.astro         # Badge component
│   │   │   └── Button.astro        # Button component
│   │   ├── DocumentsList.jsx       # Legacy component (React)
│   │   ├── FeaturesSection.astro
│   │   ├── Footer.astro
│   │   ├── IntroSection.astro
│   │   ├── NavBar.astro
│   │   ├── RoadmapSection.astro
│   │   ├── Slides.jsx              # Legacy component (React)
│   │   └── Welcome.astro
│   ├── documents/                  # Nội dung tài liệu (MDX)
│   │   ├── anki-tieng-han-tong-hop-1-bai-1.mdx
│   │   ├── hangul-video.mdx
│   │   ├── huong-dan.mdx
│   │   ├── itopik-website.mdx
│   │   ├── seoul-korean-1a.mdx
│   │   ├── tai-lieu.mdx
│   │   ├── tieng-han-tong-hop-1.mdx
│   │   └── topik-vocabulary.mdx
│   ├── layouts/
│   │   └── Layout.astro            # Layout chung cho toàn site
│   ├── pages/                      # File-based routing
│   │   ├── documents/
│   │   │   └── [slug].astro        # Dynamic routing cho từng tài liệu
│   │   ├── index.astro             # Trang chủ
│   │   └── tai-lieu.astro          # Trang danh sách tài liệu
│   └── styles/
│       ├── global.css
│       └── navbar.css             # Dedicated NavBar styles
├── astro.config.mjs
├── tailwind.config.mjs
└── package.json
```

## 🎯 Tính năng chính

### 📚 Trang `/tai-lieu` (Rebuilt)

**Kiến trúc component-based hoàn toàn mới:**

1. **FilterSection.astro**
   - Filter theo category: Giáo trình, Website, Video, v.v.
   - Filter theo subcategory: Seoul Korean, Tiếng Hàn Tổng Hợp, v.v.
   - Dynamic UI updates với vanilla JavaScript
   - State management cho active filters

2. **DocumentGrid.astro**
   - Responsive grid: 1→5 columns tùy screen size
   - Empty state khi không có kết quả filter
   - Grid container với proper spacing

3. **DocumentCard.astro**
   - Card design đồng nhất cho mọi tài liệu
   - Cover image với fallback gradient branding
   - Badge system: category, subcategory, type, fileSize, pages
   - Hover effects với scale + shadow
   - Click anywhere để xem chi tiết

4. **Badge.astro & Button.astro**
   - UI components tái sử dụng
   - Multiple variants (primary, secondary, neutral, v.v.)
   - Size variants (sm, md, lg)
   - Consistent styling across site

### 🔄 Data Flow

```text
documents/*.mdx → Astro.glob() → Data processing → Components → UI
```

1. **Data Source**: File `.mdx` trong `/documents`
2. **Processing**: Extract frontmatter, validate, transform
3. **Categories**: Auto-generate từ document metadata
4. **Filtering**: Client-side với vanilla JavaScript
5. **Rendering**: Pure Astro components (no React)

## 📝 Thêm tài liệu mới

### 1. Tạo file MDX

Tạo file trong `src/documents/` với cấu trúc frontmatter:

```yaml
---
title: "Tên tài liệu"                    # Required
date: "2024-07-10"                       # Required  
category: "Giáo trình"                   # Required: Giáo trình|Website|Video|Từ vựng
subcategory: "Seoul Korean"              # Required: Phân loại chi tiết
type: "PDF"                              # Required: PDF|Website|Video|App
description: "Mô tả ngắn gọn"            # Required

# Optional fields
cover: "/images/ten-file.jpg"            # Cover image
downloadUrl: "https://link-download"     # Link tải chính
downloadOriginal: "https://link-goc"     # Link file gốc
downloadWorkbook: "https://link-sbt"     # Link sách bài tập  
downloadAudio: "https://link-audio"      # Link file nghe
fileSize: "4.3MB"                        # Kích thước file
originalSize: "107.6MB"                  # Kích thước gốc
workbookSize: "16.3MB"                   # Kích thước SBT
audioSize: "Folder audio"                # Kích thước audio
pages: 250                               # Số trang
duration: "45 phút"                      # Thời lượng (video)
url: "https://website.com"               # URL (website)
features: ["Feature 1", "Feature 2"]    # Danh sách tính năng
---

# Nội dung tài liệu

Viết nội dung chi tiết bằng Markdown/MDX...
```

### 2. Thêm hình ảnh cover

- Đặt file vào `public/images/`
- Format: JPG, PNG, WebP
- Kích thước khuyến nghị: 300x400px (3:4 ratio)
- Tên file: `ten-tai-lieu.jpg`

### 3. Categories và Types được hỗ trợ

#### Categories
- **Giáo trình**: Sách giáo khoa, tài liệu học chính thức
- **Website**: Trang web học tiếng Hàn
- **Video**: Video YouTube, khóa học online
- **Từ vựng**: Bộ từ vựng, flashcards, Anki decks
- **Ứng dụng**: Mobile apps, web apps

#### Types  
- **PDF**: File PDF để download
- **Website**: Link tới website
- **Video**: Link YouTube/video platform
- **App**: Mobile/web application

### 4. Auto-filtering system

Hệ thống tự động:
- Extract categories từ tất cả documents
- Generate subcategories cho mỗi category
- Tạo filter UI dynamically
- Update URL params (tùy chọn)

## 🛠️ Development Guide

### Component Development

#### Tạo component mới
```bash
# Document-specific component
src/components/document/NewComponent.astro

# Reusable UI component  
src/components/ui/NewUIComponent.astro
```

#### Component Props Type Safety
```typescript
// Component props interface
export interface Props {
  title: string;
  optional?: boolean;
  items: Array<{
    id: string;
    name: string;
  }>;
}

const { title, optional = false, items } = Astro.props;
```

### Styling Guidelines

#### CSS Structure
```css
/* Component-specific styles trong .astro files */
<style>
  .component-class {
    /* Scoped styles */
  }
</style>

/* Global styles trong global.css */
.utility-class {
  /* Global utilities */
}
```

#### Tailwind Classes
- Sử dụng Tailwind cho layout, spacing, colors
- Custom CSS cho animations phức tạp
- Responsive classes: `sm:` `md:` `lg:` `xl:`

### State Management

#### Client-side filtering
```javascript
// Vanilla JS trong <script> tags
document.addEventListener('DOMContentLoaded', function() {
  // Filter logic
  // DOM manipulation
  // Event handlers
});
```

#### No React cho trang /tai-lieu
- Pure Astro components
- Vanilla JavaScript cho interactivity
- Better performance, smaller bundle

### Performance Optimization

#### Image Optimization
```astro
<!-- Lazy loading -->
<img src={cover} alt={title} loading="lazy" />

<!-- Responsive images -->
<img 
  src={cover} 
  alt={title}
  class="w-full h-full object-cover"
  loading="lazy"
/>
```

#### CSS Optimization  
```css
/* Smooth transitions */
.document-card {
  transition: all 0.2s ease-in-out;
}

/* Hardware acceleration */
.hover-effect {
  transform: translateZ(0);
  will-change: transform;
}
```

## 🔧 Advanced Configuration

### Astro Config
```javascript
// astro.config.mjs
export default defineConfig({
  integrations: [
    mdx(),
    react(),
    tailwind()
  ],
  output: 'static', // hoặc 'server'
});
```

### TypeScript Support
- Strict type checking enabled
- Component props validation
- Auto-completion trong VS Code
- Error catching tại build time

### Build Optimization
```bash
# Development
npm run dev          # Fast reload, no optimization

# Production  
npm run build        # Minified, optimized bundle
npm run preview      # Test production build locally
```

## 🚀 Deployment

### Static Site Generation (SSG)
```bash
npm run build
# Output: dist/ folder
```

### Supported Platforms
- **Netlify**: Auto-deploy from Git
- **Vercel**: Zero-config deployment  
- **GitHub Pages**: Static hosting
- **Cloudflare Pages**: Edge deployment

### Environment Variables
```bash
# .env
PUBLIC_SITE_URL=https://your-domain.com
PRIVATE_API_KEY=your-secret-key
```

## 🧪 Testing & QA

### Manual Testing Checklist
- [ ] Filter functionality (category + subcategory)
- [ ] Responsive design (mobile → desktop)
- [ ] Document card hover effects
- [ ] Empty state display
- [ ] Document detail pages
- [ ] Image loading (cover + fallback)
- [ ] Performance (Lighthouse score)

### Browser Support
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers

## 📖 Learning Resources

### Astro
- [Astro Documentation](https://docs.astro.build)
- [Astro Components](https://docs.astro.build/en/core-concepts/astro-components/)
- [MDX Integration](https://docs.astro.build/en/guides/integrations-guide/mdx/)

### Tailwind CSS
- [Tailwind Documentation](https://tailwindcss.com/docs)
- [Responsive Design](https://tailwindcss.com/docs/responsive-design)
- [Component Examples](https://tailwindui.com/components)

## 🤝 Contributing

### Development Workflow
1. Fork repository
2. Create feature branch
3. Make changes với proper TypeScript types
4. Test thoroughly (manual + automated)
5. Submit pull request

### Code Style
- Use TypeScript for type safety
- Follow Astro component conventions
- Consistent naming conventions:
  - Components: PascalCase (e.g., `DocumentCard.astro`)
  - File names: kebab-case (e.g., `global.css`)
  - Document files: Follow the pattern `[type]-[series]-[level]-[lesson].mdx` (e.g., `anki-tieng-han-tong-hop-1-bai-1.mdx`)
  - Variables: camelCase (e.g., `documentsList`)
- Comment complex logic
- Keep components focused and reusable

### Document File Naming Convention

For all document files in the `/src/documents/` directory, use the following naming pattern:

```
[type]-[series]-[level]-[lesson].mdx
```

Examples:
- `anki-tieng-han-tong-hop-1-bai-1.mdx` - Anki deck for Tiếng Hàn Tổng Hợp 1, Bài 1
- `pdf-tieng-han-tong-hop-1-bai-2.mdx` - PDF document for Tiếng Hàn Tổng Hợp 1, Bài 2
- `video-hangul-lesson-1.mdx` - Video lesson about Hangul, Lesson 1

This convention ensures consistency and makes it easier to identify content types at a glance.

### Recent Modernization Changes

The website has undergone significant modernization in July 2025:

1. **Updated UI Components**
   - Modern, responsive NavBar with dropdowns and mobile menu
   - Improved document cards with type-specific displays (e.g., card count for Anki decks)
   - Enhanced filtering and categorization system

2. **Better Code Organization**
   - Componentized architecture (UI components, document-specific components, etc.)
   - Styles organized in dedicated CSS files (global.css, navbar.css)
   - Standardized file naming conventions

3. **Content Updates**
   - Added Anki deck resources for Tiếng Hàn Tổng Hợp 1 (Bài 1-3)
   - Properly categorized content types

4. **Performance Improvements**
   - Fixed layout issues for better responsiveness
   - Optimized component rendering

## 📋 CHANGELOG

### Phiên bản 1.1.0 (10 tháng 7, 2025)

#### Đã thêm

- Thanh điều hướng hiện đại, tương tác với menu thả xuống và hỗ trợ di động
- Tài liệu Anki deck mới cho Tiếng Hàn Tổng Hợp 1 (Bài 1-12) - đầy đủ 12 bài
- File navbar.css bên ngoài để tổ chức style tốt hơn
- Tài liệu hóa quy tắc đặt tên file tài liệu
- Logic sắp xếp số học (numeric sorting) cho phần "File Anki liên quan"
- Hệ thống liên kết tự động giữa giáo trình và Anki decks qua field `relatedTo`

#### Đã thay đổi
- Cập nhật thẻ tài liệu để hiển thị số lượng thẻ cho loại Anki deck
- Di chuyển style của NavBar sang file CSS riêng để dễ bảo trì
- Sửa padding của body để phù hợp với thanh điều hướng cố định
- Chuẩn hóa cấu trúc đặt tên file cho tất cả tài liệu
- Cải thiện tài liệu README với thông tin chi tiết về logic "File Anki liên quan"
- Tối ưu hóa nội dung SEO cho trang Tiếng Hàn Tổng Hợp 1

#### Đã sửa

- Sửa lỗi cú pháp Tailwind CSS trong component NavBar
- Sửa lỗi padding trùng lặp trong Layout.astro
- Sửa hiển thị loại tài liệu cho Anki decks
- Sửa lỗi sắp xếp thứ tự bài học (1, 2, 3... thay vì 1, 10, 11, 12, 2, 3...)

#### Hệ thống File Anki liên quan

**Logic hoạt động:**
- Tự động tìm các Anki deck có `relatedTo` trùng với slug của trang hiện tại
- Sắp xếp theo thứ tự số bài học (numeric sorting) thay vì string sorting
- Hiển thị dạng grid với thông tin chi tiết: title, description, fileSize, số cards
- Động (dynamic) - hoạt động với mọi giáo trình, không hardcode

**Cấu trúc frontmatter cần thiết:**
```yaml
# File Anki deck
type: "Anki Deck"
relatedTo: "slug-cua-giao-trinh"  # VD: "tieng-han-tong-hop-1"
title: "Anki - Tên giáo trình - Bài X"
fileSize: "X.XMB"
cards: 100
```

**Ví dụ thực tế:**
- Trang `/documents/tieng-han-tong-hop-1` → hiển thị 12 Anki decks (bài 1-12)
- Trang `/documents/seoul-korean-1a` → hiển thị Anki decks của Seoul Korean (nếu có)
- Hệ thống scalable, dễ mở rộng cho các giáo trình khác

---

**Built with ❤️ using Astro, Tailwind CSS, and TypeScript**

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

Here's the current structure of the project:

```text
/
├── public/
│   └── favicon.svg
├── src/
│   ├── assets/
│   │   ├── astro.svg
│   │   └── background.svg
│   ├── components/
│   │   ├── document/              # Components for document pages
│   │   │   ├── DocumentCard.astro
│   │   │   ├── DocumentGrid.astro
│   │   │   └── FilterSection.astro
│   │   ├── home/                  # Components for homepage
│   │   │   ├── HeroSection.astro
│   │   │   ├── FeaturesGrid.astro
│   │   │   ├── StatsSection.astro
│   │   │   └── ...
│   │   ├── ui/                    # Reusable UI components
│   │   │   ├── Badge.astro
│   │   │   └── Button.astro
│   │   ├── Footer.astro
│   │   ├── NavBar.astro
│   │   └── ...
│   ├── documents/                 # MDX document files
│   │   ├── anki-tieng-han-tong-hop-1-bai-1.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-2.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-3.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-4.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-5.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-6.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-7.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-8.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-9.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-10.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-11.mdx
│   │   ├── anki-tieng-han-tong-hop-1-bai-12.mdx
│   │   ├── tieng-han-tong-hop-1.mdx
│   │   └── ...
│   ├── layouts/
│   │   └── Layout.astro
│   ├── pages/
│   │   ├── index.astro            # Homepage
│   │   └── tai-lieu.astro         # Documents listing page
│   └── styles/
│       ├── global.css
│       └── navbar.css             # Dedicated NavBar styles
├── astro.config.mjs
├── tailwind.config.mjs
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
