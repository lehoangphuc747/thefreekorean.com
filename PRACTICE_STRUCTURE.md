# 📚 Cấu trúc Luyện tập theo dạng đề

## 🎯 Cách hoạt động

### 1. **Cấu trúc dữ liệu hiện tại (ĐÃ CÓ)**
Mỗi question trong JSON đã có field `question_type`:
```json
{
  "id": "topik2-91-r-1",
  "question_type": "vocab",  // ← Dùng để filter
  "question_no": 1,
  ...
}
```

### 2. **Helper Functions để query (ĐÃ TẠO)**

#### Client-side: `src/utils/topik-practice-loader.ts`
```typescript
// Lọc TOPIK II - Reading - vocab
const questions = await filterQuestionsByType('topik2', 'reading', 'vocab');

// Lấy danh sách dạng đề có sẵn
const types = await getAvailableQuestionTypes('topik2', 'reading');
// Returns: [{ type: 'vocab', count: 12, label: 'Từ vựng' }, ...]
```

#### Server-side: `src/utils/topik-practice-loader-server.ts`
```typescript
// Cho Astro getStaticPaths
const questions = filterQuestionsByTypeServer('topik2', 'reading', 'vocab');
const types = getAvailableQuestionTypesServer('topik2', 'reading');
```

---

## 📋 Flow: User chọn dạng đề

```
Step 1: User vào /topik/practice
  ↓
Step 2: Chọn TOPIK II
  ↓
Step 3: Chọn Reading
  ↓
Step 4: Hiển thị danh sách dạng đề:
  - Từ vựng (vocab) - 12 câu
  - Ngữ pháp (grammar) - 8 câu
  - Hiểu mạch văn (context) - 15 câu
  ...
  ↓
Step 5: User chọn "Từ vựng"
  ↓
Step 6: Load và hiển thị 12 câu vocab
```

---

## 🔍 Query theo dạng đề

### Ví dụ: TOPIK II - Reading - vocab

**Code:**
```typescript
import { filterQuestionsByType } from '@/utils/topik-practice-loader';

const vocabQuestions = await filterQuestionsByType('topik2', 'reading', 'vocab');
// Returns: Tất cả questions có question_type = "vocab" từ tất cả đề TOPIK II
```

**Kết quả:**
```javascript
[
  { id: "topik2-91-r-1", question_type: "vocab", question_no: 1, ... },
  { id: "topik2-91-r-2", question_type: "vocab", question_no: 2, ... },
  { id: "topik2-90-r-1", question_type: "vocab", question_no: 1, ... },
  // ... từ tất cả đề TOPIK II
]
```

---

## 📝 Ví dụ: Lọc theo nhóm (câu 1-4)

Bạn đề cập "đề đọc sẽ có dạng 1 (câu 1-4)" - có 2 cách:

### Cách 1: Tính từ question_no (Không cần thêm field)
```typescript
// Mỗi nhóm 4 câu
const groupNo = Math.ceil(question_no / 4);

// Filter nhóm 1 (câu 1-4)
const group1Questions = questions.filter(q => 
  Math.ceil(q.question_no / 4) === 1
);
```

### Cách 2: Thêm field `question_group` vào JSON
```json
{
  "id": "topik2-91-r-1",
  "question_no": 1,
  "question_group": 1,  // Nhóm 1 (câu 1-4)
  "question_type": "vocab",
  ...
}
```

**Filter:**
```typescript
const group1Questions = questions.filter(q => q.question_group === 1);
```

---

## 🎨 Trang Practice Structure

### Option A: URL Pattern
```
/topik/practice/topik2/reading/vocab
/topik/practice/topik2/listening/listen_pic
/topik/practice/topik1/reading/grammar
```

### Option B: Query Parameters
```
/topik/practice?level=topik2&section=reading&type=vocab
```

---

## 💻 Example Code

### Page: `/topik/practice/[level]/[section]/[type].astro`

```astro
---
import { filterQuestionsByTypeServer } from '../../../utils/topik-practice-loader-server';
import TopikQuestion from '../../../components/topik/TopikQuestion.astro';

export async function getStaticPaths() {
  const paths = [];
  
  const levels = ['topik1', 'topik2'];
  const sections = ['reading', 'listening', 'writing'];
  
  for (const level of levels) {
    for (const section of sections) {
      // Get available types
      const types = getAvailableQuestionTypesServer(level, section);
      
      for (const typeInfo of types) {
        paths.push({
          params: {
            level,
            section,
            type: typeInfo.type
          },
          props: {
            questions: filterQuestionsByTypeServer(level, section, typeInfo.type),
            typeInfo
          }
        });
      }
    }
  }
  
  return paths;
}

const { questions, typeInfo } = Astro.props;
---

<h1>Luyện tập: {typeInfo.label}</h1>
<p>{typeInfo.count} câu hỏi</p>

{questions.map((question, index) => (
  <TopikQuestion
    question={question}
    questionNumber={index + 1}
  />
))}
```

---

## ✅ Tóm tắt

**Cấu trúc đã có sẵn:**
- ✅ Mỗi question có `question_type` trong JSON
- ✅ Helper functions để filter
- ✅ Có thể query theo level, section, question_type

**Cách query:**
1. `loadAllQuestions(level, section)` - Load tất cả questions
2. `filterQuestionsByType(level, section, type)` - Filter theo type
3. `getAvailableQuestionTypes(level, section)` - Lấy danh sách types có sẵn

**Cho nhóm câu hỏi:**
- Option 1: Tính từ `question_no` (không cần thêm field)
- Option 2: Thêm `question_group` vào JSON (nếu cần phân loại phức tạp hơn)

