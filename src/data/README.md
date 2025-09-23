# Data Documentation

Thư mục `src/data` chứa các module dữ liệu tĩnh dùng để hiển thị trên giao diện (không gọi API).
Hiện có 2 module:
- `roadmaps.ts`: dữ liệu lộ trình học
- `grammarRoadmaps.ts`: dữ liệu lộ trình/ngữ pháp theo chủ đề

## Nguyên tắc chung
- Xuất (export) các hằng số đã gán kiểu rõ ràng để IDE có thể gợi ý.
- Tối ưu cho đọc/hiểu: giữ mô tả ngắn gọn, có thể xuống dòng khi dài.
- Không import component trong các file dữ liệu; chỉ chứa dữ liệu thuần.

## Kiểu dữ liệu liên quan
Các kiểu cho lộ trình được định nghĩa tại `src/types/roadmap.ts`:

```ts
export interface RoadmapResource {
  name: string;
  type: 'video' | 'pdf' | 'anki' | 'link' | 'document';
  url: string;
}

export interface RoadmapStep {
  id: number;
  level: 'Cơ bản' | 'Sơ cấp' | 'Trung cấp' | 'Nâng cao' | 'Chuyên ngành';
  title: string;
  description: string;
  duration: string;
  status: 'available' | 'coming-soon' | 'locked';
  resources: RoadmapResource[];
}

export interface Roadmap {
  id: string;
  title: string;
  description: string;
  steps: RoadmapStep[];
}
```

## `roadmaps.ts`
- Mục đích: Cung cấp danh sách các lộ trình học theo chủ đề/mục tiêu.
- Dạng xuất đề xuất: `export const roadmaps: Roadmap[] = [...]`.

Ví dụ nội dung mẫu:

```ts
import type { Roadmap } from '@/types/roadmap';

export const roadmaps: Roadmap[] = [
  {
    id: 'so-cap',
    title: 'Lộ trình Sơ cấp',
    description: 'Tập trung nền tảng phát âm, ngữ pháp, từ vựng cơ bản.',
    steps: [
      {
        id: 1,
        level: 'Sơ cấp',
        title: 'Bảng chữ cái & phát âm',
        description: 'Nắm vững Hangul và quy tắc phát âm.',
        duration: '1-2 tuần',
        status: 'available',
        resources: [
          { name: 'Video Hangul', type: 'video', url: 'https://...' },
          { name: 'PDF phát âm', type: 'pdf', url: '/downloads/...' },
        ],
      },
      // ... các bước tiếp theo
    ],
  },
  // ... các lộ trình khác
];
```

## `grammarRoadmaps.ts`
- Mục đích: Gom nhóm/lộ trình ngữ pháp theo cấp độ hoặc chủ đề để học tuần tự.
- Dạng xuất đề xuất: có thể dùng cấu trúc đơn giản để hiển thị nhanh.

Ví dụ cấu trúc gợi ý (tự do hóa dạng dữ liệu nếu không dùng chung với `Roadmap`):

```ts
export interface GrammarUnit {
  id: string;           // ví dụ: '으면서'
  title: string;        // tiêu đề hiển thị
  level: 'Sơ cấp' | 'Trung cấp' | 'Nâng cao';
  slug: string;         // slug dùng cho routing
}

export interface GrammarGroup {
  id: string;           // ví dụ: 'so-cap-1'
  title: string;        // nhóm: Sơ cấp - Phần 1
  description?: string; // mô tả ngắn
  items: GrammarUnit[]; // danh sách mẫu ngữ pháp
}

export const grammarRoadmaps: GrammarGroup[] = [
  {
    id: 'so-cap-1',
    title: 'Sơ cấp - Phần 1',
    description: 'Các mẫu cơ bản mở đầu cho người mới học.',
    items: [
      { id: '으면서', title: '으면서', level: 'Sơ cấp', slug: 'so-cap/으면서' },
      // ... các mẫu khác
    ],
  },
  // ... các nhóm khác
];
```

## Cách sử dụng trong component
Ví dụ import trong một component để render danh sách lộ trình:

```ts
import { roadmaps } from '@/data/roadmaps';

function getAvailableStepsCount() {
  return roadmaps.flatMap(r => r.steps).filter(s => s.status === 'available').length;
}
```

Ví dụ import lộ trình ngữ pháp để render theo nhóm:

```ts
import { grammarRoadmaps } from '@/data/grammarRoadmaps';

const allGrammar = grammarRoadmaps.flatMap(group => group.items);
```

## Lưu ý triển khai
- Nếu dữ liệu lớn, cân nhắc tách thành nhiều file nhỏ theo chủ đề.
- Với liên kết tĩnh đến asset (PDF, ảnh), ưu tiên đường dẫn dưới `public/`.
- Giữ naming và slug nhất quán với hệ thống route trong `src/pages/`.
