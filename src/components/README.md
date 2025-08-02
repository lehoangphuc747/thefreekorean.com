# Components Documentation

## Cấu trúc thư mục components

```
src/components/
├── README.md                    # Tài liệu này
├── NavBar.astro                 # Navigation bar chính
├── Footer.astro                 # Footer của trang
├── ScrollToTop.astro            # Nút scroll lên đầu trang
├── DownloadSection.astro        # Section download tài liệu
├── SearchComponent.astro        # Component tìm kiếm
├── document/                    # Components cho trang tài liệu
│   ├── DocumentCard.astro       # Card hiển thị document
│   ├── DocumentGrid.astro       # Grid layout cho documents
│   └── FilterSection.astro      # Section lọc documents
├── home/                        # Components cho trang chủ
│   ├── HeroSection.astro        # Hero section trang chủ
│   ├── FeaturesGrid.astro       # Grid tính năng
│   ├── StatsSection.astro       # Thống kê
│   ├── DocumentsPreview.astro   # Preview documents
│   ├── TestimonialsSection.astro # Phần đánh giá
│   ├── CTASection.astro         # Call to action

└── ui/                          # UI components cơ bản
    ├── Badge.astro              # Badge component
    ├── Button.astro             # Button component
    └── LanguageToggle.astro     # Toggle ngôn ngữ
```

## Components được sử dụng

### 🏠 Layout & Navigation
- **NavBar.astro** - Navigation bar chính (được sử dụng trong Layout.astro)
- **Footer.astro** - Footer trang web
- **ScrollToTop.astro** - Nút scroll lên đầu trang

### 📄 Document System
- **DownloadSection.astro** - Hiển thị phần download trong trang chi tiết document
- **SearchComponent.astro** - Component tìm kiếm trong trang tài liệu
- **document/DocumentCard.astro** - Card hiển thị từng document
- **document/DocumentGrid.astro** - Grid layout cho danh sách documents
- **document/FilterSection.astro** - Phần lọc documents theo category

### 🏠 Homepage
- **home/HeroSection.astro** - Hero section trang chủ
- **home/FeaturesGrid.astro** - Grid hiển thị tính năng
- **home/StatsSection.astro** - Phần thống kê
- **home/DocumentsPreview.astro** - Preview documents mới nhất
- **home/TestimonialsSection.astro** - Phần đánh giá từ người dùng
- **home/CTASection.astro** - Call to action


### 🎨 UI Components
- **ui/Badge.astro** - Badge component cơ bản
- **ui/Button.astro** - Button component cơ bản
- **ui/LanguageToggle.astro** - Toggle chuyển đổi ngôn ngữ

### 📄 Other Components
- **Không có components khác ở root level**

## Components đã xoá (không sử dụng)

- ❌ **FeaturesSection.astro** - Section hiển thị tính năng (trùng với home/FeaturesGrid.astro)
- ❌ **IntroSection.astro** - Section giới thiệu (không được sử dụng)
- ❌ **TailwindDemo.astro** - Demo Tailwind CSS (không được sử dụng)
- ❌ **Welcome.astro** - Component welcome mặc định của Astro
- ❌ **RoadmapSection.astro** - Roadmap section cũ (đã có roadmap/ folder)
- ❌ **roadmap/** - Toàn bộ thư mục roadmap components (không cần thiết)
- ❌ **LearningStats.jsx** - Stats component (không được sử dụng)
- ❌ **QuickReview.jsx** - Quick review component (không được sử dụng)
- ❌ **unused/** - Toàn bộ thư mục unused

## Ghi chú

### React vs Astro Components
- **Astro components (.astro)**: Cho static content, SSR
- **React components (.jsx/.tsx)**: Cho interactive content, cần client-side functionality

### Component Organization
- Components được tổ chức theo chức năng (home/, document/, ui/)
- Components tái sử dụng được đặt ở root level
- UI components cơ bản trong thư mục ui/

### Usage Guidelines
1. Kiểm tra xem component có tồn tại trước khi tạo mới
2. Đặt tên component theo PascalCase
3. Thêm comment mô tả chức năng ở đầu file
4. Tổ chức theo thư mục chức năng
