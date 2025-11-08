# Hướng dẫn kiểm tra SEO nhanh cho các trang TOPIK

## 🔍 Công cụ kiểm tra SEO MIỄN PHÍ

### 1. **Google Search Console** (Quan trọng nhất)
- **Link**: https://search.google.com/search-console
- **Cách dùng**:
  1. Đăng nhập bằng tài khoản Google
  2. Thêm property website của bạn
  3. Verify ownership (dùng HTML tag hoặc Google Analytics)
  4. Submit sitemap: `https://thefreekorean.com/sitemap.xml`
  5. Kiểm tra "Coverage" để xem trang nào đã được index
  6. Kiểm tra "Performance" để xem từ khóa nào đang rank

### 2. **Google Rich Results Test** (Kiểm tra Structured Data)
- **Link**: https://search.google.com/test/rich-results
- **Cách dùng**:
  1. Paste URL trang TOPIK vào (ví dụ: `https://thefreekorean.com/tai-lieu/textbooks/topik-2-96`)
  2. Click "Test URL"
  3. Kiểm tra xem có lỗi nào không
  4. Xem preview cách Google hiển thị

### 3. **Meta Tags Preview** (Kiểm tra Open Graph)
- **Link**: https://metatags.io/
- **Cách dùng**:
  1. Paste URL vào
  2. Xem preview Facebook, Twitter, Google
  3. Kiểm tra title, description, image hiển thị đúng chưa

### 4. **PageSpeed Insights** (Kiểm tra tốc độ)
- **Link**: https://pagespeed.web.dev/
- **Cách dùng**:
  1. Paste URL vào
  2. Chọn "Mobile" hoặc "Desktop"
  3. Xem điểm số và Core Web Vitals
  4. Sửa các vấn đề được đề xuất

### 5. **Schema Markup Validator** (Kiểm tra JSON-LD)
- **Link**: https://validator.schema.org/
- **Cách dùng**:
  1. Paste URL hoặc code JSON-LD
  2. Kiểm tra lỗi syntax
  3. Xem preview structured data

## ✅ Checklist SEO cho mỗi trang TOPIK

### Meta Tags (Đã có trong code)
- ✅ Title tag (50-60 ký tự) - **Đã có**
- ✅ Meta description (150-160 ký tự) - **Đã có**
- ✅ Keywords - **Đã có**
- ✅ Canonical URL - **Đã có**
- ✅ Open Graph tags - **Đã có**
- ✅ Twitter Cards - **Đã có**

### Structured Data (Đã có trong code)
- ✅ Schema.org EducationalMaterial - **Đã có**
- ✅ Date published - **Đã có**
- ✅ Author/Publisher - **Đã có**
- ✅ Image - **Đã có**
- ✅ Description - **Đã có**

### Technical SEO
- ✅ HTML lang="vi" - **Đã có**
- ✅ Mobile responsive - **Đã có**
- ✅ HTTPS - Cần kiểm tra trên hosting
- ✅ XML Sitemap - Cần thêm TOPIK pages vào sitemap

## 🚀 Cách kiểm tra nhanh (5 phút)

### Bước 1: Kiểm tra meta tags
1. Mở trang TOPIK trên browser
2. Right-click → "View Page Source"
3. Tìm `<title>` và `<meta name="description">`
4. Kiểm tra xem có đúng không

### Bước 2: Kiểm tra structured data
1. View Source
2. Tìm `<script type="application/ld+json">`
3. Copy JSON và paste vào https://validator.schema.org/
4. Kiểm tra lỗi

### Bước 3: Kiểm tra Open Graph
1. Paste URL vào https://metatags.io/
2. Xem preview Facebook/Twitter
3. Kiểm tra image, title, description

### Bước 4: Submit lên Google
1. Vào Google Search Console
2. Dùng "URL Inspection" tool
3. Paste URL và click "Request Indexing"

## 📊 Từ khóa mục tiêu

### Primary Keywords (Từ khóa chính)
- `đề thi TOPIK 96`
- `TOPIK 96`
- `đáp án TOPIK 96`
- `luyện thi TOPIK 96`

### Long-tail Keywords (Từ khóa dài)
- `tải đề thi TOPIK 96 miễn phí`
- `đề thi TOPIK 96 PDF`
- `TOPIK 96 đáp án`
- `luyện thi TOPIK 96`

## 💡 Tips để SEO tốt hơn

### 1. **Nội dung chất lượng**
- Thêm section "Giới thiệu" với 200-300 từ
- Mô tả chi tiết nội dung đề thi
- Hướng dẫn cách sử dụng tài liệu

### 2. **Internal Linking**
- Link đến các kỳ thi TOPIK khác
- Link đến các bài viết liên quan
- Link đến trang chủ

### 3. **Tối ưu hình ảnh**
- Thêm alt text mô tả
- Compress images (giảm kích thước)
- Sử dụng WebP format (nếu có thể)

### 4. **Tốc độ tải trang**
- Optimize images
- Minify CSS/JS
- Use CDN (nếu có)

### 5. **Backlinks**
- Share trên social media
- Submit lên các directory
- Guest posting (nếu có thể)

## 🔗 URLs để test

Sau khi deploy, test các URL này:
- https://thefreekorean.com/tai-lieu/textbooks/topik-2-96
- https://thefreekorean.com/tai-lieu/textbooks/topik-91
- https://thefreekorean.com/tai-lieu/textbooks/topik-83
- https://thefreekorean.com/tai-lieu/textbooks/topik-64
- https://thefreekorean.com/tai-lieu/textbooks/topik-60
- https://thefreekorean.com/tai-lieu/textbooks/topik-52

## 📝 Checklist trước khi deploy

- [ ] Tất cả meta tags đã có
- [ ] Structured data không có lỗi
- [ ] Open Graph tags đúng
- [ ] Images có alt text
- [ ] URLs thân thiện với SEO
- [ ] Sitemap.xml đã cập nhật
- [ ] Robots.txt cho phép crawl
- [ ] Mobile responsive
- [ ] Tốc độ tải < 3 giây

## 🎯 Kết quả mong đợi

Sau 2-4 tuần:
- ✅ Trang được index trên Google
- ✅ Xuất hiện khi search "đề thi TOPIK [kỳ]"
- ✅ Rich snippets hiển thị (nếu structured data đúng)
- ✅ Click-through rate tốt từ search results

## ⚠️ Lưu ý quan trọng

1. **Đừng spam keywords**: Đặt từ khóa tự nhiên, không nhồi nhét
2. **Content is king**: Nội dung chất lượng quan trọng hơn SEO tricks
3. **Patience**: SEO cần thời gian, không có kết quả ngay lập tức
4. **Monitor**: Theo dõi Google Search Console thường xuyên
5. **Update**: Cập nhật nội dung định kỳ để Google biết trang còn active

