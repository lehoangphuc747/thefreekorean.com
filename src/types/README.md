# Types Documentation

Thư mục `src/types` chứa các định nghĩa TypeScript dùng chung cho toàn dự án.

## Danh sách type/module
- `roadmap.ts`: Định nghĩa các interface cho dữ liệu lộ trình học.

### `roadmap.ts`
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

## Hướng dẫn sử dụng
- Import type để gán kiểu cho dữ liệu tĩnh trong `src/data` hoặc props component:
```ts
import type { Roadmap } from '@/types/roadmap';
```
- Ưu tiên dùng `import type` để tránh kéo type vào bundle client.

## Mở rộng/Thay đổi type
- Khi thêm thuộc tính mới, đảm bảo cập nhật nơi khởi tạo dữ liệu (`src/data`) và nơi render.
- Duy trì backward compatibility nếu có dữ liệu cũ; dùng thuộc tính tùy chọn (`?`) khi hợp lý.
- Đặt tên thuộc tính rõ ràng, đồng nhất (snake_case/kebab-case không dùng trong TS interface; dùng camelCase).
