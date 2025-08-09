# Hướng dẫn tạo file ngữ pháp .astro

## Tổng quan

File ngữ pháp .astro được tạo trong thư mục `src/pages/ngu-phap/` với cấu trúc phân cấp theo trình độ:
- `so-cap/` - Sơ cấp (Beginner)
- `trung-cap/` - Trung cấp (Intermediate) 
- `cao-cap/` - Cao cấp (Advanced)

## Cấu trúc file cơ bản

```astro
---
import Layout from '../../../layouts/Layout.astro';

// Import các component ngữ pháp
import NppPageHeader from '../../../components/ngu-phap-post/NppPageHeader.astro';
import NppBasicInfoCard from '../../../components/ngu-phap-post/NppBasicInfoCard.astro';
import NppMeaningAndUsageCard from '../../../components/ngu-phap-post/NppMeaningAndUsageCard.astro';
import NppExampleCard from '../../../components/ngu-phap-post/NppExampleCard.astro';
import NppIntroductionCard from '../../../components/ngu-phap-post/NppIntroductionCard.astro';
import NppMorphologyInfoCard from '../../../components/ngu-phap-post/NppMorphologyInfoCard.astro';
import NppMorphologyUsageCard from '../../../components/ngu-phap-post/NppMorphologyUsageCard.astro';
import NppSentenceCompositionCard from '../../../components/ngu-phap-post/NppSentenceCompositionCard.astro';
import NppConstraintInfoCard from '../../../components/ngu-phap-post/NppConstraintInfoCard.astro';
import NppExtensionCard from '../../../components/ngu-phap-post/NppExtensionCard.astro';
import NppSimilarGrammarCard from '../../../components/ngu-phap-post/NppSimilarGrammarCard.astro';

// Metadata trang
const pageTitle = "Ngữ pháp Tiếng Hàn: [TÊN NGỮ PHÁP]";
const description = "Mô tả ngắn gọn về ngữ pháp";

// Export data cho trang danh sách
export const postData = {
  title: '[TÊN NGỮ PHÁP] (nghĩa tiếng Việt)',
  grammar: '[NGỮ PHÁP TIẾNG HÀN]',
  meaning: 'nghĩa tiếng Việt',
  description: 'Mô tả ngắn gọn về ngữ pháp',
  level: 'Beginner', // Beginner, Intermediate, Advanced
  category: 'Ngữ pháp',
  subcategory: 'Sơ cấp', // Sơ cấp, Trung cấp, Cao cấp
  type: 'Grammar',
  tags: ['tag1', 'tag2', 'tag3'],
  examples: 6,
  exercises: 10,
  difficulty: 1, // 1-5
  date: '2024-07-02'
};

// Dữ liệu cho các component
const headerData = { 
  title: `Ngữ pháp [TÊN NGỮ PHÁP]` 
};

// ... các data khác

**Lưu ý:** Tất cả các component đã có title mặc định được tích hợp sẵn. Bạn không cần phải truyền title vào props nữa, trừ khi muốn tùy chỉnh title.

---

<Layout title={pageTitle}>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-purple-50 to-slate-100">
    <div class="flex flex-col items-center gap-8 md:gap-10 px-4 py-12">
      
      <!-- Header -->
      <NppPageHeader title={headerData.title} />
      
      <!-- Basic Info -->
      <NppBasicInfoCard details={basicInfoData.details} />
      
      <!-- Meaning and Usage -->
      <NppMeaningAndUsageCard sections={meaningData.sections} />
      
      <!-- Examples -->
      <NppExampleCard 
        dialogueSection={exampleData.dialogueSection}
        sentenceSection={exampleData.sentenceSection}
        note={exampleData.note}
      />
      
      <!-- Introduction -->
      <NppIntroductionCard 
        dialogues={introductionData.dialogues}
        notes={introductionData.notes}
      />
      
      <!-- Morphology Info -->
      <NppMorphologyInfoCard 
        sections={morphologyInfoData.sections}
        irregularSection={morphologyInfoData.irregularSection}
      />
      
      <!-- Morphology Usage -->
      <NppMorphologyUsageCard 
        rules={morphologyUsageData.rules}
      />
      
      <!-- Sentence Composition -->
      <NppSentenceCompositionCard 
        rule={sentenceCompositionData.rule}
      />
      
      <!-- Constraints -->
      <NppConstraintInfoCard 
        rules={constraintData.rules}
      />
      
      <!-- Extensions -->
      <NppExtensionCard 
        rules={extensionData.rules}
      />
      
      <!-- Similar Grammar -->
      <NppSimilarGrammarCard 
        comparisons={similarGrammarData.comparisons}
      />
      
    </div>

    <!-- Navigation -->
    <div class="flex justify-between items-center w-full max-w-3xl mx-auto px-4 pb-8">
      <a 
        href="/ngu-phap" 
        class="inline-flex items-center gap-2 text-purple-600 hover:text-purple-700 font-medium"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
        </svg>
        Quay lại danh sách ngữ pháp
      </a>
      
      <div class="flex gap-4">
        <a 
          href="/tai-lieu" 
          class="inline-flex items-center gap-2 text-blue-600 hover:text-blue-700 font-medium"
        >
          Tài liệu
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
          </svg>
        </a>
      </div>
    </div>
  </div>
</Layout>
```

## Cấu trúc dữ liệu chi tiết cho từng component

### 1. BasicInfoCard

```typescript
const basicInfoData = {
  details: [ 
    { label: 'Ngữ pháp', value: '[NGỮ PHÁP]', color: 'text-purple-600' }, 
    { label: 'Từ loại', value: '표현', color: 'text-blue-600' }, 
    { label: 'TOPIK', value: '초급', color: 'text-green-600' }, 
    { label: 'CEFR', value: 'A1', color: 'text-orange-500' } 
  ]
};
```

### 2. MeaningAndUsageCard

```typescript
const meaningData = {
  sections: [ 
    { subtitle: 'Ý nghĩa chính', icon: 'lightbulb', content: 'Mô tả ý nghĩa chính.' }, 
    { subtitle: 'Cách dùng chi tiết', icon: 'pencil', content: 'Mô tả cách dùng chi tiết.' } 
  ]
};
```

**Lưu ý:** `icon` chỉ nhận giá trị: `'lightbulb'` hoặc `'pencil'`

### 3. ExampleCard

```typescript
const exampleData = {
  dialogueSection: {
    subtitle: 'Ví dụ hội thoại',
    examples: [
      { q_ko: 'Câu hỏi tiếng Hàn', q_vi: 'Câu hỏi tiếng Việt', a_ko: 'Câu trả lời tiếng Hàn', a_vi: 'Câu trả lời tiếng Việt' }
    ]
  },
  sentenceSection: {
    subtitle: 'Ví dụ câu',
    examples: [
      { ko: 'Câu tiếng Hàn', vi: 'Câu tiếng Việt' }
    ]
  },
  note: {
    subtitle: 'Lưu ý',
    content_vi: 'Nội dung lưu ý bằng tiếng Việt'
  }
};
```

### 4. IntroductionCard

```typescript
const introductionData = {
  dialogues: [
    { 
      id: 1, 
      lines: [ 
        { speaker: '교사', text_ko: 'Tiếng Hàn', text_vi: 'Tiếng Việt'}, 
        { speaker: '학생 1', text_ko: 'Tiếng Hàn', text_vi: 'Tiếng Việt'} 
      ] 
    }
  ],
  notes: [
    { note_ko: 'Ghi chú tiếng Hàn', note_vi: 'Ghi chú tiếng Việt' }
  ]
};
```

### 5. MorphologyInfoCard

```typescript
const morphologyInfoData = {
  sections: [
    { 
      id: 1, 
      title: 'Tiêu đề section', 
      rule: 'Quy tắc', 
      examples: [ 
        { before: 'Trước', after: 'Sau' } 
      ], 
      note: 'Ghi chú (có thể null)' 
    }
  ],
  irregularSection: {
    title: 'Bất quy tắc',
    examples: [
      { stem: 'Gốc từ:', example: 'Ví dụ' }
    ]
  }
};
```

**Lưu ý quan trọng:** 
- `note` phải là `string` hoặc `null`, không được là `undefined`
- Nếu không có ghi chú, đặt `note: null`

### 6. MorphologyUsageCard

```typescript
const morphologyUsageData = {
  rules: [
    { condition: 'Điều kiện', rule: 'Quy tắc', examples: ['Ví dụ 1', 'Ví dụ 2'] }
  ]
};
```

### 7. SentenceCompositionCard

```typescript
const sentenceCompositionData = {
  rule: {
    id: 1,
    description: 'Mô tả quy tắc',
    examples: ['Ví dụ 1', 'Ví dụ 2']
  }
};
```

### 8. ConstraintInfoCard

```typescript
const constraintData = {
  rules: [
    {
      id: 1,
      description: 'Mô tả hạn định',
      examples: [
        { text: 'Câu ví dụ', isCorrect: true },
        { text: 'Câu ví dụ sai', isCorrect: false }
      ],
      note: 'Ghi chú (có thể undefined)'
    }
  ]
};
```

### 9. ExtensionCard

```typescript
const extensionData = {
  rules: [
    {
      id: 1,
      description: 'Mô tả mở rộng',
      examples: ['Ví dụ 1', 'Ví dụ 2'],
      note: 'Ghi chú (có thể null)'
    }
  ]
};
```

**Lưu ý quan trọng:** 
- `note` phải là `string` hoặc `null`, không được là `undefined`

### 10. SimilarGrammarCard

```typescript
const similarGrammarData = {
  comparisons: [
    {
      id: 1,
      title: 'So sánh ngữ pháp A vs B',
      g1: {
        name: 'Ngữ pháp A',
        points: [
          { description: 'Điểm 1', example: 'Ví dụ 1' },
          { description: 'Điểm 2', example: 'Ví dụ 2' }
        ]
      },
      g2: {
        name: 'Ngữ pháp B',
        points: [
          { description: 'Điểm 1', example: 'Ví dụ 1' },
          { description: 'Điểm 2', example: 'Ví dụ 2' }
        ]
      },
      note: 'Ghi chú (có thể null)'
    }
  ]
};
```

**Lưu ý quan trọng:** 
- `note` phải là `string` hoặc `null`, không được là `undefined`

## Quy tắc đặt tên file

1. **Tên file:** Sử dụng tên ngữ pháp tiếng Hàn, ví dụ: `고-싶다.astro`, `으면서.astro`
2. **Đường dẫn:** `src/pages/ngu-phap/[level]/[tên-file].astro`
3. **Ví dụ:** `src/pages/ngu-phap/so-cap/고-싶다.astro`

## Các lỗi thường gặp và cách khắc phục

### 1. Lỗi TypeScript với MorphologyInfoCard
```typescript
// SAI - note có thể undefined
{ id: 1, title: '...', rule: '...', examples: [...], note: undefined }

// ĐÚNG - note phải là string hoặc null
{ id: 1, title: '...', rule: '...', examples: [...], note: null }
```

### 2. Lỗi TypeScript với ExtensionCard
```typescript
// SAI - note có thể undefined
{ id: 1, description: '...', examples: [...], note: undefined }

// ĐÚNG - note phải là string hoặc null
{ id: 1, description: '...', examples: [...], note: null }
```

### 3. Lỗi TypeScript với SimilarGrammarCard
```typescript
// SAI - note có thể undefined
{ id: 1, title: '...', g1: {...}, g2: {...}, note: undefined }

// ĐÚNG - note phải là string hoặc null
{ id: 1, title: '...', g1: {...}, g2: {...}, note: null }
```

## Checklist khi tạo file ngữ pháp mới

- [ ] Import đầy đủ các component cần thiết
- [ ] Đặt metadata trang (pageTitle, description)
- [ ] Export postData với đầy đủ thông tin
- [ ] Tạo dữ liệu cho tất cả component
- [ ] Kiểm tra kiểu dữ liệu cho các trường `note` (phải là `string` hoặc `null`)
- [ ] Đặt tên file theo quy tắc
- [ ] Test trang để đảm bảo không có lỗi lint
- [ ] Kiểm tra hiển thị trên trang danh sách ngữ pháp

## Ví dụ hoàn chỉnh

Xem các file mẫu:
- `src/pages/ngu-phap/so-cap/고-싶다.astro` - Ngữ pháp sơ cấp
- `src/pages/ngu-phap/so-cap/으면서.astro` - Ngữ pháp sơ cấp

## Lưu ý quan trọng

1. **Kiểu dữ liệu:** Luôn đảm bảo kiểu dữ liệu chính xác theo interface của component
2. **Null vs Undefined:** Các trường `note` phải là `string` hoặc `null`, không được `undefined`
3. **Tên file:** Sử dụng tên ngữ pháp tiếng Hàn làm tên file
4. **Cấu trúc:** Tuân thủ cấu trúc thư mục theo trình độ
5. **Metadata:** Điền đầy đủ thông tin trong `postData` để hiển thị đúng trên trang danh sách
