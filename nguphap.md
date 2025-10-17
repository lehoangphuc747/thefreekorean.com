Tôi sẽ phân tích cấu trúc trang ngữ pháp và các component liên kết với nhau. Hãy để tôi khám phá codebase để hiểu rõ hơn.


[6 tools called]

Dựa trên việc phân tích codebase, tôi sẽ tạo một sơ đồ để minh họa cấu trúc trang ngữ pháp và cách các component liên kết với nhau:


[1 tool called]

Tôi sẽ tạo một sơ đồ bằng text để minh họa cấu trúc trang ngữ pháp:

## 📚 Cấu trúc trang ngữ pháp The Free Korean

### 🏗️ **Kiến trúc tổng thể**

```
📁 src/pages/ngu-phap/
├── 📄 ngu-phap.astro (Trang danh sách chính)
├── 📄 [slug].astro (Dynamic route - hiện tại disabled)
└── 📁 so-cap/ (Sơ cấp)
    ├── 📄 고-싶다.astro
    ├── 📄 -(스)ㅂ니다.astro
    └── 📄 으면서.astro
```

### 🔗 **Các component liên kết**

#### **1. Trang danh sách ngữ pháp (`/ngu-phap`)**

```
📄 ngu-phap.astro
├── 🎯 Layout.astro (Layout chung)
├── 🔍 GrammarFilter.astro (Bộ lọc)
└── 📋 GrammarGrid.astro (Lưới hiển thị)
```

**Template structure:**
```astro
---
// Import components
import Layout from '../layouts/Layout.astro';
import GrammarFilter from '../components/grammar/GrammarFilter.astro';
import GrammarGrid from '../components/grammar/GrammarGrid.astro';

// Import tất cả file ngữ pháp bằng Vite glob
const grammarFiles = import.meta.glob(['./ngu-phap/**/*.astro', '!./ngu-phap/[slug].astro'], { 
  eager: true,
  import: 'postData' 
});

// Xử lý dữ liệu
const grammarList = Object.entries(grammarFiles)
  .map(([path, postData]) => ({ ...postData, slug: ... }))
  .filter(item => item && item.title);
---

<Layout title="Ngữ pháp tiếng Hàn">
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-purple-50 to-slate-100">
    <!-- Header Section -->
    <header>...</header>
    
    <!-- Grammar Filter Section -->
    <GrammarFilter grammarList={grammarList} />
    
    <!-- Grammar Grid -->
    <GrammarGrid grammarList={grammarList} />
  </div>
</Layout>
```

#### **2. Trang chi tiết ngữ pháp (`/ngu-phap/so-cap/고-싶다`)**

```
📄 고-싶다.astro
├── 🎯 Layout.astro
└── 📦 11 components ngữ pháp:
    ├── 📄 00_Header.astro (Tiêu đề chính)
    ├── 📄 01_ThongTin.astro (Thông tin cơ bản - Từ loại, TOPIK, CEFR)
    ├── 📄 02_Ynghia.astro (Ý nghĩa và cách dùng)
    ├── 📄 03_ViDu.astro (Ví dụ)
    ├── 📄 04_DanNhap.astro (Dẫn nhập)
    ├── 📄 05_HinhThai.astro (Thông tin hình thái)
    ├── 📄 06_CachDung.astro (Cách dùng)
    ├── 📄 07_CauTruc.astro (Cấu trúc câu)
    ├── 📄 08_LuuY.astro (Lưu ý)
    ├── 📄 09_MoRong.astro (Mở rộng)
    └── 📄 10_TuongDong.astro (Tương đồng)
```

**Template structure:**
```astro
---
import Layout from '../../../layouts/Layout.astro';

// Import tất cả components ngữ pháp với tên mới
import Header from '../../../components/ngu-phap-post/00_Header.astro';
import ThongTin from '../../../components/ngu-phap-post/01_ThongTin.astro';
import Ynghia from '../../../components/ngu-phap-post/02_Ynghia.astro';
import ViDu from '../../../components/ngu-phap-post/03_ViDu.astro';
import DanNhap from '../../../components/ngu-phap-post/04_DanNhap.astro';
import HinhThai from '../../../components/ngu-phap-post/05_HinhThai.astro';
import CachDung from '../../../components/ngu-phap-post/06_CachDung.astro';
import CauTruc from '../../../components/ngu-phap-post/07_CauTruc.astro';
import LuuY from '../../../components/ngu-phap-post/08_LuuY.astro';
import MoRong from '../../../components/ngu-phap-post/09_MoRong.astro';
import TuongDong from '../../../components/ngu-phap-post/10_TuongDong.astro';

// Export data cho trang danh sách
export const postData = {
  title: '-고 싶다 (muốn)',
  grammar: '-고 싶다',
  meaning: 'muốn, mong muốn',
  // ... các thuộc tính khác
};

// Dữ liệu cho từng component
const headerData = { title: `Ngữ pháp -고 싶다` };
const basicInfoData = { 
  details: [
    { label: 'Từ loại', value: '종결어미 (Vĩ tố kết thúc câu)', color: 'text-blue-600' },
    { label: 'TOPIK', value: '초급', color: 'text-green-600' },
    { label: 'CEFR', value: 'A1', color: 'text-orange-500' }
  ]
};
const meaningAndUsageData = { /* ... */ };
// ... dữ liệu cho các component khác
---

<Layout title={pageTitle}>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 via-purple-50 to-slate-100">
    <div class="max-w-4xl mx-auto px-4 py-8">
      
      <!-- Page Header (hiển thị tên ngữ pháp) -->
      <Header title={headerData.title} />
      
      <!-- Basic Info Card (Từ loại, TOPIK, CEFR - không bao gồm tên ngữ pháp) -->
      <ThongTin details={basicInfoData.details} />
      
      <!-- Meaning and Usage Card -->
      <Ynghia sections={meaningAndUsageData.sections} />
      
      <!-- Example Card -->
      <ViDu 
        dialogueSection={exampleData.dialogueSection}
        sentenceSection={exampleData.sentenceSection}
        note={exampleData.note}
      />
      
      <!-- Introduction Card -->
      <DanNhap 
        dialogues={introductionData.dialogues}
        notes={introductionData.notes}
      />
      
      <!-- Morphology Info Card -->
      <HinhThai 
        title={morphologyInfoData.title}
        rules={morphologyInfoData.rules}
      />
      
      <!-- Morphology Usage Card -->
      <CachDung 
        title={morphologyUsageData.title}
        rules={morphologyUsageData.rules}
      />
      
      <!-- Sentence Composition Card -->
      <CauTruc 
        title={sentenceCompositionData.title}
        rule={sentenceCompositionData.rule}
      />
      
      <!-- Constraint Info Card -->
      <LuuY 
        title={constraintData.title}
        rules={constraintData.rules}
      />
      
      <!-- Extension Card -->
      <MoRong 
        title={extensionData.title}
        rules={extensionData.rules}
      />
      
      <!-- Similar Grammar Card -->
      <TuongDong 
        title={similarGrammarData.title}
        comparisons={similarGrammarData.comparisons}
      />
      
    </div>
  </div>
</Layout>
```

### 🎨 **Template Pattern**

#### **1. Trang danh sách (`ngu-phap.astro`)**
- **Layout**: `Layout.astro` với background gradient
- **Header**: Tiêu đề + mô tả + thống kê
- **Filter**: `GrammarFilter.astro` với JavaScript filtering
- **Grid**: `GrammarGrid.astro` hiển thị cards

#### **2. Trang chi tiết (`so-cap/고-싶다.astro`)**
- **Layout**: `Layout.astro` với background gradient
- **Container**: `max-w-4xl mx-auto px-4 py-8`
- **Components**: 11 components ngữ pháp được sắp xếp theo thứ tự:
  1. `00_Header.astro` - Tiêu đề chính
  2. `01_ThongTin.astro` - Thông tin cơ bản (Từ loại, TOPIK, CEFR)
  3. `02_Ynghia.astro` - Ý nghĩa và cách dùng
  4. `03_ViDu.astro` - Ví dụ
  5. `04_DanNhap.astro` - Dẫn nhập
  6. `05_HinhThai.astro` - Thông tin hình thái
  7. `06_CachDung.astro` - Cách dùng
  8. `07_CauTruc.astro` - Cấu trúc câu
  9. `08_LuuY.astro` - Lưu ý
  10. `09_MoRong.astro` - Mở rộng
  11. `10_TuongDong.astro` - Tương đồng

### 🔄 **Luồng dữ liệu**

```
1. Vite Glob Import → Import tất cả file .astro trong /ngu-phap/
2. Extract postData → Lấy metadata từ mỗi file
3. Process Data → Xử lý và chuẩn hóa dữ liệu
4. Pass to Components → Truyền dữ liệu vào GrammarFilter & GrammarGrid
5. User Interaction → Filtering, searching, navigation
6. Dynamic Routing → Chuyển đến trang chi tiết
7. Component Rendering → Hiển thị 11 components với dữ liệu cụ thể
```

### 🎯 **Đặc điểm nổi bật**

1. **Static Generation**: Sử dụng Vite glob import thay vì dynamic routing
2. **Component-based**: Mỗi phần nội dung là một component riêng biệt
3. **Data-driven**: Tất cả dữ liệu được export từ `postData`
4. **Responsive**: Sử dụng Tailwind CSS với responsive design
5. **Interactive**: JavaScript filtering và searching
6. **SEO-friendly**: Mỗi trang có metadata riêng

### 📝 **Quy tắc phát triển**

- **File naming**: `kebab-case` cho file Astro
- **Component naming**: `[số]_[TênTiếngViệt].astro` cho components ngữ pháp
- **Data structure**: Luôn export `postData` từ mỗi file
- **Component props**: TypeScript interfaces cho type safety
- **Styling**: Tailwind CSS với custom classes
- **Thứ tự components**: Đánh số từ 00-10 theo thứ tự hiển thị
- **Khối thông tin**: Chỉ hiển thị Từ loại, TOPIK, CEFR (không bao gồm tên ngữ pháp)
- **Tên ngữ pháp**: Hiển thị ở Header component, không lặp lại ở khối thông tin

Cấu trúc này cho phép dễ dàng thêm ngữ pháp mới bằng cách tạo file `.astro` mới trong thư mục tương ứng và export `postData` với đầy đủ thông tin.