# Components Documentation

## Cấu trúc thư mục `src/components`

```
src/components/
├── README.md                     # Tài liệu này
├── NavBar.astro                  # Thanh điều hướng chính
├── NavBar.astro.bak              # Bản sao lưu NavBar cũ (không dùng trong build)
├── Footer.astro                  # Footer trang web
├── ScrollToTop.astro             # Nút cuộn lên đầu trang
├── DownloadSection.astro         # Khu vực tải tài liệu trong bài viết
├── SearchComponent.astro         # Component tìm kiếm tài liệu
├── grammar/                      # Components cho mục Ngữ pháp tổng quan
│   ├── GrammarFilter.astro       # Bộ lọc ngữ pháp
│   └── GrammarGrid.astro         # Lưới hiển thị danh sách ngữ pháp
├── ngu-phap-post/                # Components cho trang chi tiết bài ngữ pháp
│   ├── NppBasicInfoCard.astro            # Thông tin cơ bản (tên mẫu, cấp độ, loại)
│   ├── NppConstraintInfoCard.astro       # Các ràng buộc/khi nào KHÔNG dùng
│   ├── NppExampleCard.astro              # Ví dụ minh hoạ có dịch
│   ├── NppExtensionCard.astro            # Mở rộng/biến thể của mẫu ngữ pháp
│   ├── NppIntroductionCard.astro         # Giới thiệu tổng quan mẫu ngữ pháp
│   ├── NppMeaningAndUsageCard.astro      # Ý nghĩa và cách dùng chi tiết
│   ├── NppMorphologyInfoCard.astro       # Thông tin hình thái (biến đổi, kết hợp)
│   ├── NppMorphologyUsageCard.astro      # Cách dùng theo hình thái, lưu ý đặc thù
│   ├── NppPageHeader.astro               # Header trang, tiêu đề + meta
│   ├── NppSentenceCompositionCard.astro  # Cấu tạo câu, trật tự thành phần
│   └── NppSimilarGrammarCard.astro       # So sánh/Ngữ pháp tương tự dễ nhầm
├── home/
│   └── HeroSection.astro         # Hero section trang chủ
├── tai-lieu/                     # Components cho hệ thống tài liệu
│   ├── DocumentCard.astro               # Thẻ hiển thị thông tin 1 tài liệu
│   ├── DocumentGrid.astro               # Lưới danh sách tài liệu
│   ├── FilterSection.astro              # Bộ lọc theo category/level/format
│   ├── PDFPreview.astro                 # Xem trước nội dung PDF
│   ├── PostHero.astro                   # Hero của trang chi tiết tài liệu
│   ├── TextbooksDownloader.astro        # Tải giáo trình/multiple files
│   └── TextbooksHeader.astro            # Header trang/section giáo trình
├── topik/                        # Components cho mục TOPIK
│   ├── TopikCard.astro                  # Thẻ đề thi/bài luyện tập TOPIK
│   ├── TopikFilter.astro                # Bộ lọc theo cấp/đề/năm
│   ├── TopikGrid.astro                  # Lưới danh sách đề/series
│   ├── TopikQuiz.astro                  # Bài luyện tập/quiz tương tác
│   ├── TopikTestCard.astro              # Thẻ hiển thị thông tin đề thi
│   └── TopikTimer.astro                 # Đồng hồ đếm ngược khi làm bài
├── roadmap/
│   └── RoadmapSelector.tsx       # Bộ chọn lộ trình (React)
└── ui/                           # UI components cơ bản
    ├── Badge.astro                      # Nhãn đánh dấu ngắn gọn
    ├── Button.astro                     # Nút bấm tiêu chuẩn
    ├── LanguageToggle.astro             # Chuyển đổi ngôn ngữ giao diện
    ├── ReadingProgress.astro            # Thanh tiến độ đọc bài
    ├── SkeletonCard.astro               # Placeholder card khi loading
    ├── SkeletonFilter.astro             # Placeholder filter khi loading
    └── TableOfContents.astro            # Mục lục bài viết/section
```

## Components theo khu vực chức năng

### Layout & Điều hướng
- **NavBar.astro**: Thanh điều hướng chính (dùng trong `src/layouts/Layout.astro` và layout liên quan)
- **Footer.astro**: Footer trang web
- **ScrollToTop.astro**: Nút cuộn lên đầu trang

### Tài liệu (Documents)
- **DownloadSection.astro**: Khu vực tải tài liệu trong trang chi tiết
- **SearchComponent.astro**: Tìm kiếm trong khu vực tài liệu
- Thư mục `tai-lieu/`: Card, Grid, Filter, PDF preview, Header và downloader cho giáo trình

### Ngữ pháp (Grammar)
- Thư mục `grammar/`: Lọc và hiển thị lưới các mẫu ngữ pháp
- Thư mục `ngu-phap-post/`: Các thẻ thông tin chi tiết cho một bài ngữ pháp (giới thiệu, ý nghĩa/cách dùng, hình thái, ví dụ, cấu tạo câu, so sánh, ràng buộc...)

### TOPIK
- Thư mục `topik/`: Lưới đề, bộ lọc, thẻ đề thi, bộ đếm giờ và quiz luyện tập

### Trang chủ
- **home/HeroSection.astro**: Phần Hero của trang chủ

### Lộ trình (Roadmap)
- **roadmap/RoadmapSelector.tsx**: Component React chọn lộ trình học (nhúng kiểu Island khi cần interactivity)

### UI cơ bản
- Thư mục `ui/`: Badge, Button, LanguageToggle, ReadingProgress, Skeletons, TableOfContents

## Ghi chú sử dụng

### Astro vs React
- **.astro**: Nội dung tĩnh/SSR, tương thích tốt với Astro Islands
- **.tsx/.jsx**: Khi cần tương tác client-side; thêm chỉ thị client (`client:load`, `client:idle`, ...) khi nhúng vào `.astro`

### Quy ước & Tổ chức
1. Đặt tên component theo PascalCase
2. Tái sử dụng component ở `ui/` khi có thể trước khi tạo mới
3. Tách theo domain: `grammar/`, `ngu-phap-post/`, `tai-lieu/`, `topik/`, `home/`, `roadmap/`
4. Viết mô tả ngắn ở đầu file nếu component phức tạp

### Lưu ý khác
- `NavBar.astro.bak` là file sao lưu, không import trong runtime
- Đảm bảo đường dẫn import thống nhất với cấu hình module alias của dự án
