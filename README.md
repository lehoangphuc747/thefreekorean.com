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
│   │   └── tai-lieu.astro          # Trang danh sách tài liệu (REBUILT)
│   └── styles/
│       └── global.css              # Global CSS + component styles
├── .vscode/
│   └── tasks.json                  # VS Code tasks
├── astro.config.mjs                # Astro configuration
├── package.json
├── tsconfig.json                   # TypeScript configuration
└── tailwind.config.mjs             # Tailwind CSS configuration
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
- Consistent naming (camelCase, PascalCase)
- Comment complex logic
- Keep components focused và reusable

---

**Built with ❤️ using Astro, Tailwind CSS, and TypeScript**
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
