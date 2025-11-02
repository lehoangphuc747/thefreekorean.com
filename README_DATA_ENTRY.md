# 📝 Hướng dẫn nhập dữ liệu TOPIK 91

Tài liệu này hướng dẫn chi tiết cách nhập dữ liệu cho TOPIK I & II đề 91.

## 📋 Mục lục

1. [Cấu trúc thư mục](#cấu-trúc-thư-mục)
2. [Quy ước ID và tên file](#quy-ước-id-và-tên-file)
3. [Schema JSON chi tiết](#schema-json-chi-tiết)
4. [Quy trình nhập dữ liệu](#quy-trình-nhập-dữ-liệu)
5. [Validation và kiểm tra](#validation-và-kiểm-tra)
6. [FAQ](#faq)

---

## 📁 Cấu trúc thư mục

```
public/
  data/
    topik1/91/
      reading.json       ← Nhập câu hỏi đọc TOPIK I
      listening.json     ← Nhập câu hỏi nghe TOPIK I
    topik2/91/
      reading.json       ← Nhập câu hỏi đọc TOPIK II
      listening.json     ← Nhập câu hỏi nghe TOPIK II
      writing.json       ← Nhập câu hỏi viết TOPIK II
  assets/
    topik1/91/
      reading/           ← Lưu ảnh đọc TOPIK I
      listening/         ← Lưu ảnh/audio nghe TOPIK I
    topik2/91/
      reading/           ← Lưu ảnh đọc TOPIK II
      listening/         ← Lưu ảnh/audio nghe TOPIK II
      writing/           ← Lưu biểu đồ viết TOPIK II
```

---

## 🔑 Quy ước ID và tên file

### ID câu hỏi

Format: `{level}-{test}-{section_letter}-{question_no}`

**Ví dụ:**
- `topik1-91-r-1` → TOPIK I, đề 91, đọc, câu 1
- `topik1-91-l-15` → TOPIK I, đề 91, nghe, câu 15
- `topik2-91-r-32` → TOPIK II, đề 91, đọc, câu 32
- `topik2-91-w-52` → TOPIK II, đề 91, viết, câu 52

**Quy tắc:**
- `level`: `topik1` hoặc `topik2`
- `test`: Số đề thi (91)
- `section_letter`: `r` (reading), `l` (listening), `w` (writing)
- `question_no`: Số thứ tự câu hỏi (không có số 0 đứng trước, trừ khi < 10 thì format: `01`, `02`...)

### Tên file ảnh

**Đọc:**
- `/assets/topik1/91/reading/r-20.png`
- `/assets/topik2/91/reading/r-32.png`

**Nghe (đáp án hình):**
- `/assets/topik1/91/listening/l-01-a.png` (đáp án A)
- `/assets/topik1/91/listening/l-01-b.png` (đáp án B)
- `/assets/topik1/91/listening/l-01-c.png` (đáp án C)
- `/assets/topik1/91/listening/l-01-d.png` (đáp án D)

**Nghe (audio):**
- `/assets/topik1/91/listening/l-01.mp3`

**Viết (biểu đồ/bảng):**
- `/assets/topik2/91/writing/w-52-chart.png`
- `/assets/topik2/91/writing/w-53-table.png`

---

## 📝 Schema JSON chi tiết

### 1. Đọc (Reading)

**Cấu trúc cơ bản:**

```json
{
  "id": "topik1-91-r-1",
  "question_no": 1,
  "question_type": "vocab",
  "question_kr": "다음 중 (  )에 알맞은 것을 고르십시오.",
  "options": ["옵션 A", "옵션 B", "옵션 C", "옵션 D"],
  "answer": 0,
  "tags": ["reading", "vocab"],
  "source": "TOPIK I 91"
}
```

**Có hình ảnh:**

```json
{
  "id": "topik2-91-r-32",
  "question_no": 32,
  "question_type": "context",
  "question_kr": "다음 글의 내용과 일치하는 것을 고르십시오.",
  "images": [
    {
      "src": "/assets/topik2/91/reading/r-32.png",
      "alt": "Mô tả hình ảnh"
    }
  ],
  "options": ["옵션 A", "옵션 B", "옵션 C", "옵션 D"],
  "answer": 3,
  "tags": ["reading", "context"],
  "source": "TOPIK 91"
}
```

**Lưu ý:**
- Nếu không có hình → bỏ field `images` hoặc để `[]`
- `answer`: 0 = A, 1 = B, 2 = C, 3 = D
- `question_type`: xem trong `question_types.json`

---

### 2. Nghe (Listening)

**Đáp án là hình (4 hình):**

```json
{
  "id": "topik1-91-l-1",
  "question_no": 1,
  "question_type": "listen_pic",
  "audio_url": "/assets/topik1/91/listening/l-01.mp3",
  "question_kr": "",
  "options": [
    {
      "type": "image",
      "src": "/assets/topik1/91/listening/l-01-a.png",
      "alt": "Mô tả hình A"
    },
    {
      "type": "image",
      "src": "/assets/topik1/91/listening/l-01-b.png",
      "alt": "Mô tả hình B"
    },
    {
      "type": "image",
      "src": "/assets/topik1/91/listening/l-01-c.png",
      "alt": "Mô tả hình C"
    },
    {
      "type": "image",
      "src": "/assets/topik1/91/listening/l-01-d.png",
      "alt": "Mô tả hình D"
    }
  ],
  "answer": 2,
  "tags": ["listening"],
  "source": "TOPIK I 91"
}
```

**Đáp án là text:**

```json
{
  "id": "topik1-91-l-15",
  "question_no": 15,
  "question_type": "listen_dialog",
  "audio_url": "/assets/topik1/91/listening/l-15.mp3",
  "question_kr": "남자가 무엇을 하고 있는지 고르십시오.",
  "options": [
    "옵션 A",
    "옵션 B",
    "옵션 C",
    "옵션 D"
  ],
  "answer": 1,
  "tags": ["listening"],
  "source": "TOPIK I 91"
}
```

**Lưu ý:**
- Nếu đáp án là hình → `options` là array of objects với `type: "image"`
- Nếu đáp án là text → `options` là array of strings
- `audio_url`: có thể để trống nếu chưa có file audio

---

### 3. Viết (Writing)

**Có biểu đồ:**

```json
{
  "id": "topik2-91-w-52",
  "question_no": 52,
  "question_type": "write_long",
  "prompt_kr": "아래 표를 보고 200~300자로 글을 쓰시오.",
  "images": [
    {
      "src": "/assets/topik2/91/writing/w-52-chart.png",
      "alt": "Biểu đồ..."
    }
  ],
  "sample_answer": "",
  "rubric": "",
  "tags": ["writing", "essay"],
  "source": "TOPIK 91"
}
```

**Không có hình:**

```json
{
  "id": "topik2-91-w-51",
  "question_no": 51,
  "question_type": "write_short",
  "prompt_kr": "다음을 읽고 150~300자로 글을 쓰시오.",
  "sample_answer": "",
  "rubric": "",
  "tags": ["writing", "short"],
  "source": "TOPIK 91"
}
```

---

## 🔄 Quy trình nhập dữ liệu

### Bước 1: Chuẩn bị

1. Mở file JSON tương ứng (ví dụ: `public/data/topik1/91/reading.json`)
2. Xem file `.example.json` để tham khảo cấu trúc
3. Chuẩn bị ảnh/audio (nếu có)

### Bước 2: Nhập từng câu hỏi

1. Tạo object theo schema
2. Đảm bảo `id` đúng format
3. Điền đầy đủ các field bắt buộc
4. Lưu file

### Bước 3: Validation

Chạy script validation:

```bash
node scripts/validate-topik-data.js
```

Script sẽ:
- Kiểm tra cấu trúc JSON
- Validate ID format
- Kiểm tra các field bắt buộc
- Báo lỗi nếu có

### Bước 4: Test trên trình duyệt

1. Chạy dev server: `npm run dev`
2. Truy cập: `http://localhost:4321/topik/tests/topik1-91` hoặc `topik2-91`
3. Kiểm tra hiển thị câu hỏi, ảnh, audio

---

## ✅ Checklist nhập dữ liệu

### TOPIK I

**Đọc:**
- [ ] Câu 1-40: Nhập vào `topik1/91/reading.json`
- [ ] Ảnh (nếu có): Lưu vào `assets/topik1/91/reading/`

**Nghe:**
- [ ] Câu 1-30: Nhập vào `topik1/91/listening.json`
- [ ] Ảnh đáp án (nếu có): Lưu vào `assets/topik1/91/listening/`
- [ ] Audio: Lưu vào `assets/topik1/91/listening/`

### TOPIK II

**Đọc:**
- [ ] Câu 1-28 (hoặc 32): Nhập vào `topik2/91/reading.json`
- [ ] Ảnh (nếu có): Lưu vào `assets/topik2/91/reading/`

**Nghe:**
- [ ] Câu 1-24 (hoặc 28): Nhập vào `topik2/91/listening.json`
- [ ] Ảnh đáp án (nếu có): Lưu vào `assets/topik2/91/listening/`
- [ ] Audio: Lưu vào `assets/topik2/91/listening/`

**Viết:**
- [ ] Câu 51, 52: Nhập vào `topik2/91/writing.json`
- [ ] Biểu đồ/bảng (nếu có): Lưu vào `assets/topik2/91/writing/`

---

## 🧪 Validation và kiểm tra

### Chạy validation script

```bash
node scripts/validate-topik-data.js
```

### Kiểm tra thủ công

1. **Format JSON**: Mở file bằng editor có JSON syntax highlighting
2. **ID duy nhất**: Đảm bảo không có ID trùng
3. **Đường dẫn ảnh**: Kiểm tra ảnh có tồn tại không
4. **Đáp án**: Đảm bảo `answer` là 0, 1, 2, hoặc 3

### Test trên trình duyệt

1. Mở `/topik/tests/topik1-91` hoặc `/topik/tests/topik2-91`
2. Kiểm tra:
   - ✅ Câu hỏi hiển thị đúng
   - ✅ Ảnh load được
   - ✅ Audio phát được
   - ✅ Đáp án có thể chọn
   - ✅ Navigation hoạt động

---

## ❓ FAQ

**Q: Làm sao biết câu nào có hình?**  
A: Xem đề gốc. Nếu đề có hình/bảng/biểu đồ thì thêm vào `images` array.

**Q: Audio có bắt buộc không?**  
A: Không, nhưng khuyến khích thêm để người dùng có thể nghe.

**Q: Có thể để trống `options` không?**  
A: Không, với reading/listening phải có 4 options. Với writing thì không cần.

**Q: ID bị sai format thì sao?**  
A: Script validation sẽ báo lỗi. Sửa lại theo format: `{level}-{test}-{section}-{no}`

**Q: Câu hỏi có thể có nhiều hình không?**  
A: Có, thêm nhiều object vào `images` array.

**Q: Làm sao biết đáp án đúng?**  
A: Xem đáp án gốc của đề. Đếm từ 0: A=0, B=1, C=2, D=3.

---

## 📞 Hỗ trợ

Nếu gặp vấn đề:
1. Xem lại file `.example.json` để tham khảo
2. Chạy validation script để kiểm tra lỗi
3. Xem lại `PLAN_TOPIK_91.md` để biết chi tiết

---

**Chúc bạn nhập dữ liệu thành công! 🎉**

