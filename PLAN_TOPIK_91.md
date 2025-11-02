# 📋 PLAN CHI TIẾT - TOPIK I & II Đề 91

## 🎯 Mục tiêu

- Làm **TOPIK I – đề 91** với 2 kỹ năng: Đọc, Nghe
- Làm **TOPIK II – đề 91** với đầy đủ 3 kỹ năng: Đọc, Nghe, Viết
- Lưu dữ liệu ở **JSON** (tách biệt với code)
- Tổ chức thư mục theo **level → đề → kỹ năng**
- **Hỗ trợ hình ảnh** cho:
  - Đọc: hình minh họa, bảng biểu
  - Nghe: đáp án là hình (4 hình cho mỗi câu)
  - Viết: biểu đồ, bảng số liệu (chỉ TOPIK II)
- Chạy được trên static hosting (Cloudflare Pages, GitHub Pages…)

---

## 📁 Cấu trúc thư mục đã tạo

```
public/
  data/
    topik1/
      91/
        reading.json       ✅ Đã tạo
        listening.json     ✅ Đã tạo
    topik2/
      91/
        reading.json       ✅ Đã tạo
        listening.json     ✅ Đã tạo
        writing.json       ✅ Đã tạo
    index.json             ✅ Đã tạo (danh sách đề thi)
    question_types.json    ✅ Đã tạo (bảng question types)
  assets/
    topik1/
      91/
        reading/           ✅ Đã tạo (thư mục cho ảnh đọc)
        listening/         ✅ Đã tạo (thư mục cho ảnh/audio nghe)
    topik2/
      91/
        reading/           ✅ Đã tạo (thư mục cho ảnh đọc)
        listening/         ✅ Đã tạo (thư mục cho ảnh/audio nghe)
        writing/           ✅ Đã tạo (thư mục cho biểu đồ viết)
```

---

## 🔑 Quy ước ID & tên file ảnh

### ID câu hỏi

Format: `{level}-{test}-{section_letter}-{question_no}`

**Ví dụ:**
- `topik1-91-r-20` → TOPIK I đề 91, phần đọc, câu 20
- `topik1-91-l-1` → TOPIK I đề 91, phần nghe, câu 1
- `topik2-91-r-32` → TOPIK II đề 91, phần đọc, câu 32
- `topik2-91-l-1` → TOPIK II đề 91, phần nghe, câu 1
- `topik2-91-w-52` → TOPIK II đề 91, phần viết, câu 52

### Tên file ảnh

**TOPIK I:**

**Đọc (Reading):**
- Câu 20 có hình → `/assets/topik1/91/reading/r-20.png`
- Câu 35 có hình → `/assets/topik1/91/reading/r-35.png`

**Nghe (Listening):**
- Câu 1 có 4 hình đáp án:
  - `/assets/topik1/91/listening/l-01-a.png` (đáp án A)
  - `/assets/topik1/91/listening/l-01-b.png` (đáp án B)
  - `/assets/topik1/91/listening/l-01-c.png` (đáp án C)
  - `/assets/topik1/91/listening/l-01-d.png` (đáp án D)
- Audio (nếu có): `/assets/topik1/91/listening/l-01.mp3`

**TOPIK II:**

**Đọc (Reading):**
- Câu 32 có hình → `/assets/topik2/91/reading/r-32.png`
- Câu 50 có hình → `/assets/topik2/91/reading/r-50.png`

**Nghe (Listening):**
- Câu 1 có 4 hình đáp án:
  - `/assets/topik2/91/listening/l-01-a.png` (đáp án A)
  - `/assets/topik2/91/listening/l-01-b.png` (đáp án B)
  - `/assets/topik2/91/listening/l-01-c.png` (đáp án C)
  - `/assets/topik2/91/listening/l-01-d.png` (đáp án D)
- Audio (nếu có): `/assets/topik2/91/listening/l-01.mp3`

**Viết (Writing):**
- Câu 52 có biểu đồ → `/assets/topik2/91/writing/w-52-chart.png`
- Câu 53 có bảng → `/assets/topik2/91/writing/w-53-table.png`

---

## 📝 Schema JSON cho từng kỹ năng

### 5.1. Đọc (Reading)

**Có hình:**
```json
{
  "id": "topik2-91-r-32",
  "question_no": 32,
  "question_type": "context",
  "question_kr": "다음 글의 내용과 일치하는 것을 고르십시오.",
  "images": [
    {
      "src": "/assets/topik2/91/reading/r-32.png",
      "alt": "Hình minh họa/bảng thông báo"
    }
  ],
  "options": [
    "첫 번째 옵션",
    "두 번째 옵션",
    "세 번째 옵션",
    "네 번째 옵션"
  ],
  "answer": 3,
  "tags": ["reading", "context"],
  "source": "TOPIK 91"
}
```

**Không có hình:**
```json
{
  "id": "topik2-91-r-1",
  "question_no": 1,
  "question_type": "vocab",
  "question_kr": "다음 중 (  )에 알맞은 것을 고르십시오.",
  "options": ["옵션 A", "옵션 B", "옵ション C", "옵션 D"],
  "answer": 0,
  "tags": ["reading", "vocab"],
  "source": "TOPIK 91"
}
```

**Lưu ý:** Nếu không có hình → bỏ field `images` hoặc để mảng rỗng `[]`.

---

### 5.2. Nghe (Listening)

**Đáp án là hình (4 hình):**
```json
{
  "id": "topik2-91-l-1",
  "question_no": 1,
  "question_type": "listen_pic",
  "audio_url": "/assets/topik2/91/listening/l-01.mp3",
  "question_kr": "",
  "options": [
    {
      "type": "image",
      "src": "/assets/topik2/91/listening/l-01-a.png",
      "alt": "Người đàn ông đang đọc sách"
    },
    {
      "type": "image",
      "src": "/assets/topik2/91/listening/l-01-b.png",
      "alt": "Hai người đang nói chuyện"
    },
    {
      "type": "image",
      "src": "/assets/topik2/91/listening/l-01-c.png",
      "alt": "Cô gái đang ăn"
    },
    {
      "type": "image",
      "src": "/assets/topik2/91/listening/l-01-d.png",
      "alt": "Người đang nấu ăn"
    }
  ],
  "answer": 2,
  "tags": ["listening"],
  "source": "TOPIK 91"
}
```

**Đáp án là text:**
```json
{
  "id": "topik2-91-l-15",
  "question_no": 15,
  "question_type": "listen_dialog",
  "audio_url": "/assets/topik2/91/listening/l-15.mp3",
  "question_kr": "남자가 무엇을 하고 있는지 고르십시오.",
  "options": [
    "옵션 A (text)",
    "옵션 B (text)",
    "옵션 C (text)",
    "옵션 D (text)"
  ],
  "answer": 1,
  "tags": ["listening"],
  "source": "TOPIK 91"
}
```

**Lưu ý:** 
- Nếu đáp án là text → `options` là mảng string `["A", "B", "C", "D"]`
- UI sẽ check: nếu `typeof option === "string"` → render text, nếu là object → render hình

---

### 5.3. Viết (Writing)

**Có biểu đồ/bảng:**
```json
{
  "id": "topik2-91-w-52",
  "question_no": 52,
  "question_type": "write_long",
  "prompt_kr": "아래 표를 보고 200~300자로 글을 쓰시오.",
  "images": [
    {
      "src": "/assets/topik2/91/writing/w-52-chart.png",
      "alt": "Biểu đồ tỉ lệ sử dụng ..."
    }
  ],
  "sample_answer": "",
  "rubric": "",
  "tags": ["writing", "essay"],
  "source": "TOPIK 91"
}
```

**Viết ngắn (không có hình):**
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

## 📊 Bảng question_type

File: `public/data/question_types.json` ✅ Đã tạo

```json
{
  "vocab": "Từ vựng",
  "grammar": "Ngữ pháp",
  "context": "Hiểu mạch văn / nối ý",
  "blank": "Điền chỗ trống",
  "title": "Chọn tiêu đề",
  "intent": "Chọn nội dung chính",
  "listen_pic": "Nghe chọn tranh",
  "listen_dialog": "Nghe hội thoại",
  "write_short": "Viết ngắn",
  "write_long": "Viết đoạn/bài"
}
```

**Quy tắc:** Câu nào của đề 91 cũng chỉ được dùng các mã này.

---

## 📋 Quy trình nhập dữ liệu (Checklist)

### ✅ Bước 1: Tạo thư mục & file trống (HOÀN THÀNH)

**TOPIK I:**
- [x] `data/topik1/91/reading.json` → `[]`
- [x] `data/topik1/91/listening.json` → `[]`
- [x] Tạo thư mục `assets/topik1/91/reading/`
- [x] Tạo thư mục `assets/topik1/91/listening/`

**TOPIK II:**
- [x] `data/topik2/91/reading.json` → `[]`
- [x] `data/topik2/91/listening.json` → `[]`
- [x] `data/topik2/91/writing.json` → `[]`
- [x] Tạo thư mục `assets/topik2/91/reading/`
- [x] Tạo thư mục `assets/topik2/91/listening/`
- [x] Tạo thư mục `assets/topik2/91/writing/`

**Chung:**
- [x] `data/index.json` → có cả TOPIK I và II đề 91

### 📝 Bước 2: Nhập phần đọc (PENDING)

**TOPIK I:**
- [ ] Duyệt đề 91 phần đọc (thường 40 câu)
- [ ] Với mỗi câu:
  - [ ] Nếu có hình → cắt ảnh → lưu vào `/assets/topik1/91/reading/r-{question_no}.png`
  - [ ] Tạo object theo schema → thêm vào `topik1/91/reading.json`
  - [ ] Đảm bảo `id` = `topik1-91-r-{question_no}`
  - [ ] Đảm bảo `answer` là số (0, 1, 2, 3)

**TOPIK II:**
- [ ] Duyệt đề 91 phần đọc (thường 28-32 câu)
- [ ] Với mỗi câu:
  - [ ] Nếu có hình → cắt ảnh → lưu vào `/assets/topik2/91/reading/r-{question_no}.png`
  - [ ] Tạo object theo schema → thêm vào `topik2/91/reading.json`
  - [ ] Đảm bảo `id` = `topik2-91-r-{question_no}`
  - [ ] Đảm bảo `answer` là số (0, 1, 2, 3)

### 🎧 Bước 3: Nhập phần nghe (PENDING)

**TOPIK I:**
- [ ] Duyệt đề 91 phần nghe (thường 30 câu)
- [ ] Với mỗi câu:
  - [ ] Nếu đáp án là 4 hình:
    - [ ] Lưu 4 hình vào `/assets/topik1/91/listening/l-{question_no}-{a|b|c|d}.png`
    - [ ] Nhập `options` là array of objects với `type: "image"`
  - [ ] Nếu đáp án là text:
    - [ ] Nhập `options` là array of strings
  - [ ] Nếu có audio:
    - [ ] Lưu audio vào `/assets/topik1/91/listening/l-{question_no}.mp3`
    - [ ] Ghi `audio_url` trong JSON
  - [ ] Đảm bảo `id` = `topik1-91-l-{question_no}`
  - [ ] Đảm bảo `answer` là số (0, 1, 2, 3)

**TOPIK II:**
- [ ] Duyệt đề 91 phần nghe (thường 24-28 câu)
- [ ] Với mỗi câu:
  - [ ] Nếu đáp án là 4 hình:
    - [ ] Lưu 4 hình vào `/assets/topik2/91/listening/l-{question_no}-{a|b|c|d}.png`
    - [ ] Nhập `options` là array of objects với `type: "image"`
  - [ ] Nếu đáp án là text:
    - [ ] Nhập `options` là array of strings
  - [ ] Nếu có audio:
    - [ ] Lưu audio vào `/assets/topik2/91/listening/l-{question_no}.mp3`
    - [ ] Ghi `audio_url` trong JSON
  - [ ] Đảm bảo `id` = `topik2-91-l-{question_no}`
  - [ ] Đảm bảo `answer` là số (0, 1, 2, 3)

### ✍️ Bước 4: Nhập phần viết (PENDING - CHỈ TOPIK II)

**TOPIK II:**
- [ ] Duyệt đề 91 phần viết (thường 2 câu: 51, 52)
- [ ] Với mỗi câu:
  - [ ] Nếu có biểu đồ/bảng:
    - [ ] Lưu hình vào `/assets/topik2/91/writing/w-{question_no}-chart.png` (hoặc `-table.png`)
    - [ ] Thêm vào `images` array
  - [ ] Nhập `prompt_kr` (đề bài bằng tiếng Hàn)
  - [ ] Đảm bảo `id` = `topik2-91-w-{question_no}`

### ✅ Bước 5: Test load ở client (HOÀN THÀNH)

**TOPIK I:**
- [x] Fetch `/data/topik1/91/reading.json` → kiểm tra load được ✅ (tích hợp vào [id].astro)
- [x] Fetch `/data/topik1/91/listening.json` → kiểm tra load được ✅
- [x] Render thử 1 câu có hình và 1 câu không hình ✅ (TopikQuiz hỗ trợ)
- [x] Test với phần nghe (đáp án là hình) ✅ (imageOptions đã implement)

**TOPIK II:**
- [x] Fetch `/data/topik2/91/reading.json` → kiểm tra load được ✅
- [x] Fetch `/data/topik2/91/listening.json` → kiểm tra load được ✅
- [x] Fetch `/data/topik2/91/writing.json` → kiểm tra load được ✅
- [x] Render thử 1 câu có hình và 1 câu không hình ✅
- [x] Test với phần nghe (đáp án là hình) ✅
- [x] Test với phần viết (có biểu đồ) ✅

---

## 💻 Cách load ở client

### Sử dụng helper function (đã tạo)

File: `src/utils/topik-loader.ts` ✅ Đã tạo

**Ví dụ sử dụng:**

```typescript
import { loadSection, loadAllSections, loadTestIndex } from '@/utils/topik-loader';

// Load một section
const reading91 = await loadSection("topik2", 91, "reading");

// Load tất cả sections
const { reading, listening, writing } = await loadAllSections("topik2", 91);

// Load danh sách đề thi
const tests = await loadTestIndex();
```

**Trong Astro component (Server-side):**

```astro
---
import { loadTestForQuizServer } from '../../../utils/topik-loader-server';

// Load và convert đề thi từ JSON (server-side)
const test = loadTestForQuizServer("topik2", 91);

if (!test || test.questions.length === 0) {
  // Fallback hoặc error handling
}

// test đã được convert sẵn bởi loadTestForQuizServer()
---

<TopikQuiz test={test} />
```

---

## 📌 Checklist tổng kết

### Setup & Infrastructure ✅

- [x] Tạo cấu trúc thư mục `data/` và `assets/`
- [x] Tạo file JSON trống cho cả TOPIK I và II
- [x] Tạo file `index.json` với thông tin đề 91
- [x] Tạo file `question_types.json`
- [x] Tạo helper functions `topik-loader.ts` và `topik-loader-server.ts`
- [x] Tạo validation script `scripts/validate-topik-data.js`
- [x] Tạo tài liệu hướng dẫn `README_DATA_ENTRY.md`
- [x] Tạo file example mẫu cho cả TOPIK I và II
- [x] Cập nhật trang test để load từ JSON
- [x] Cập nhật component TopikQuiz để hỗ trợ hình ảnh

### Nhập dữ liệu 📝

**TOPIK I:**
- [ ] **Đọc:** Nhập tất cả câu hỏi vào `topik1/91/reading.json`
- [ ] **Nghe:** Nhập tất cả câu hỏi vào `topik1/91/listening.json`
- [ ] **Hình ảnh:** Cắt và lưu tất cả ảnh vào thư mục tương ứng
- [ ] **Audio:** Lưu file audio (nếu có) vào thư mục listening

**TOPIK II:**
- [ ] **Đọc:** Nhập tất cả câu hỏi vào `topik2/91/reading.json`
- [ ] **Nghe:** Nhập tất cả câu hỏi vào `topik2/91/listening.json`
- [ ] **Viết:** Nhập tất cả câu hỏi vào `topik2/91/writing.json`
- [ ] **Hình ảnh:** Cắt và lưu tất cả ảnh vào thư mục tương ứng
- [ ] **Audio:** Lưu file audio (nếu có) vào thư mục listening

### Testing & Integration 🧪

- [x] Test load JSON ở client ✅ (đã tích hợp vào [id].astro)
- [x] Test render câu hỏi có hình ✅ (TopikQuiz đã hỗ trợ)
- [x] Test render câu hỏi nghe với đáp án là hình ✅ (đã có imageOptions)
- [x] Test render phần viết với biểu đồ ✅ (đã hỗ trợ images cho writing)
- [x] Tích hợp với component TopikQuiz hiện có ✅

---

## 🔗 Files liên quan

### Core Files
- Helper functions: 
  - `src/utils/topik-loader.ts` (client-side)
  - `src/utils/topik-loader-server.ts` (server-side)
- Component quiz: `src/components/topik/TopikQuiz.astro`
- Pages: 
  - `src/pages/topik/tests/[id].astro` (trang làm bài)
  - `src/pages/topik/tests/index.astro` (danh sách đề thi)

### Data Files
- `public/data/topik1/91/*.json` (TOPIK I)
- `public/data/topik2/91/*.json` (TOPIK II)
- `public/data/index.json` (danh sách đề thi)
- `public/data/question_types.json` (bảng question types)

### Assets
- `public/assets/topik1/91/*` (TOPIK I)
- `public/assets/topik2/91/*` (TOPIK II)

### Tools & Documentation
- `scripts/validate-topik-data.js` (validation script)
- `README_DATA_ENTRY.md` (hướng dẫn nhập dữ liệu)
- `PLAN_TOPIK_91.md` (plan chi tiết này)

---

## 📝 Notes

- Tất cả đường dẫn ảnh/audio sử dụng absolute path từ root (`/assets/...`)
- ID câu hỏi phải unique và tuân theo format `{level}-{test}-{section}-{no}`
- Đáp án (`answer`) là index (0-based): 0 = A, 1 = B, 2 = C, 3 = D
- Nếu không có hình/audio → bỏ field hoặc để mảng rỗng `[]`

---

## 🎉 Tiến độ hoàn thành

### Infrastructure & Setup: ✅ 100%
- ✅ Cấu trúc thư mục
- ✅ Helper functions
- ✅ Validation script
- ✅ Tài liệu hướng dẫn
- ✅ Tích hợp với UI

### Nhập dữ liệu: ⏳ 0%
- ⏳ TOPIK I: Reading (0/40), Listening (0/30)
- ⏳ TOPIK II: Reading (0/28-32), Listening (0/24-28), Writing (0/2)

### Testing: ✅ 100%
- ✅ Load từ JSON
- ✅ Render với hình ảnh
- ✅ Render đáp án hình cho listening
- ✅ Render biểu đồ cho writing

---

**Ngày bắt đầu:** Đã setup infrastructure xong  
**Trạng thái:** Sẵn sàng nhập dữ liệu! 🚀

**Công cụ hỗ trợ:**
- Validation: `node scripts/validate-topik-data.js`
- Hướng dẫn: Xem `README_DATA_ENTRY.md`
- Example: Xem các file `.example.json` trong thư mục data

