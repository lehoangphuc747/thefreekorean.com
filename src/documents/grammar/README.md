# Thư mục Ngữ pháp tiếng Hàn

Thư mục này chứa các file MDX về ngữ pháp tiếng Hàn, được tổ chức theo cấp độ và chủ đề.

## 📁 Cấu trúc thư mục

```
grammar/
├── README.md                    # File này
├── ngu-phap-sample.mdx         # File mẫu
├── beginner/                   # Ngữ pháp sơ cấp
│   ├── ly-do.mdx              # Cách diễn tả lý do
│   ├── thoi-gian.mdx          # Biểu hiện thời gian
│   └── ...
├── intermediate/               # Ngữ pháp trung cấp
└── advanced/                  # Ngữ pháp cao cấp
```

## 📝 Quy tắc đặt tên file

- Format: `[chu-de].mdx`
- Sử dụng tiếng Việt có dấu, lowercase, cách nhau bằng gạch ngang
- Ví dụ: `ly-do.mdx`, `thoi-gian.mdx`, `dieu-kien.mdx`

## 🏷️ Cấu trúc frontmatter bắt buộc

```yaml
---
title: "Tiêu đề ngữ pháp"              # Required
date: "YYYY-MM-DD"                     # Required
category: "Ngữ pháp"                   # Required: cố định
subcategory: "Sơ cấp|Trung cấp|Cao cấp" # Required
type: "Grammar"                        # Required: cố định
level: "Beginner|Intermediate|Advanced" # Required
grammarPattern: "-기 때문에"            # Required: cấu trúc chính
meaning: "Bởi vì, do"                  # Required: ý nghĩa
description: "Mô tả ngắn"              # Required
tags: ["tag1", "tag2"]                 # Optional: các từ khóa
examples: 3                            # Optional: số ví dụ
exercises: 5                           # Optional: số bài tập
cover: "/images/grammar-*.jpg"         # Optional: ảnh cover
difficulty: 1-5                        # Optional: độ khó (1-5)
---
```

## 📖 Cấu trúc nội dung chuẩn

### 1. Tiêu đề chính
```markdown
# {grammarPattern}: {meaning}
```

### 2. Các section bắt buộc
- **📝 Ý nghĩa**: Giải thích nghĩa và cách dùng
- **📚 Cấu trúc ngữ pháp**: Cách chia và biến đổi
- **💡 Ví dụ**: Ít nhất 3 ví dụ với cả tiếng Hàn và tiếng Việt
- **⚠️ Lưu ý**: Các điểm quan trọng cần nhớ

### 3. Các section tùy chọn
- **🔄 Cấu trúc tương tự**: So sánh với ngữ pháp khác
- **📝 Bài tập**: Bài tập thực hành
- **💭 Đáp án**: Đáp án cho bài tập
- **🔗 Ngữ pháp liên quan**: Link đến các bài khác

## 💡 Hướng dẫn viết nội dung

### Format ví dụ
```markdown
### Ví dụ 1
**한국어:** Câu tiếng Hàn  
**Tiếng Việt:** Câu dịch tiếng Việt
```

### Format bảng so sánh
```markdown
| Cấu trúc | Ý nghĩa | Ví dụ |
|----------|---------|--------|
| -아/어서 | Vì, do | 아파서 못 가요 |
```

### Format bài tập
```markdown
### Bài tập 1: Loại bài tập
1. Câu hỏi
   - a) Đáp án A
   - b) Đáp án B
   - c) Đáp án C
```

## 🎯 Tags được khuyến nghị

### Theo chức năng
- "Lý do", "Thời gian", "Điều kiện", "Giả định"
- "Trạng từ", "Tính từ", "Động từ", "Danh từ"
- "Formal", "Informal", "Honorific"

### Theo cấp độ
- "Sơ cấp", "Trung cấp", "Cao cấp"
- "TOPIK I", "TOPIK II"

### Theo chủ đề
- "Giao tiếp", "Viết", "Đọc", "Nghe"
- "Hàng ngày", "Công việc", "Du lịch"

## 🔧 Tích hợp với hệ thống

Các file ngữ pháp sẽ được:
1. Tự động phát hiện và hiển thị trên trang `/ngu-phap`
2. Phân loại theo level và tags
3. Tìm kiếm theo pattern và meaning
4. Liên kết với nhau qua "Ngữ pháp liên quan"

## 📋 Checklist cho file mới

- [ ] Frontmatter đầy đủ và đúng format
- [ ] Ít nhất 3 ví dụ có dịch tiếng Việt
- [ ] Có section "Lưu ý" với các điểm quan trọng
- [ ] Bài tập và đáp án (nếu có)
- [ ] Links đến ngữ pháp liên quan
- [ ] Đặt tên file đúng quy tắc
- [ ] Kiểm tra chính tả tiếng Hàn và tiếng Việt

## 🚀 Tương lai

Các tính năng sẽ được thêm:
- Tìm kiếm nâng cao theo pattern
- Quiz tự động từ bài tập
- Hệ thống tracking progress
- AI chat bot giải thích ngữ pháp
- Ôn tập spaced repetition 