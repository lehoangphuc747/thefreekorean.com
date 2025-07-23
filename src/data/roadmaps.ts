// src/data/roadmaps.ts
import type { Roadmap } from '../types/roadmap';
import { grammarRoadmaps } from './grammarRoadmaps';

export const coreRoadmap: Roadmap = {
  id: 'core',
  title: 'Lộ trình học tiếng Hàn cốt lõi',
  description: 'Lộ trình toàn diện dành cho tất cả mọi người, từ con số 0 đến trình độ cao cấp.',
  steps: [
    {
      id: 1,
      level: 'Cơ bản',
      title: 'Nhập môn: Bảng chữ cái Hangeul và phát âm',
      description: 'Làm quen với bảng chữ cái tiếng Hàn (Hangeul), học cách đọc, viết và các quy tắc phát âm cơ bản.',
      duration: '1-2 tuần',
      status: 'available',
      resources: [
        { name: 'Video bài giảng Hangeul', type: 'video', url: '#' },
        { name: 'Tài liệu PDF bảng chữ cái', type: 'pdf', url: '#' },
        { name: 'Bộ thẻ Anki luyện đọc', type: 'anki', url: '#' },
      ],
    },
    {
      id: 2,
      level: 'Sơ cấp',
      title: 'Ngữ pháp và từ vựng Sơ cấp 1',
      description: 'Nắm vững các cấu trúc ngữ pháp cơ bản, từ vựng thiết yếu trong giao tiếp hàng ngày.',
      duration: '4-6 tuần',
      status: 'available',
      resources: [
        { name: 'Giáo trình Sejong 1', type: 'document', url: '/tai-lieu/sejong-1' },
        { name: '500 từ vựng Topik 1', type: 'anki', url: '#' },
      ],
    },
    {
      id: 3,
      level: 'Sơ cấp',
      title: 'Ngữ pháp và từ vựng Sơ cấp 2',
      description: 'Mở rộng kiến thức ngữ pháp, học các chủ đề giao tiếp phức tạp hơn như mua sắm, chỉ đường, đặt lịch hẹn.',
      duration: '4-6 tuần',
      status: 'coming-soon',
      resources: [],
    },
    {
      id: 4,
      level: 'Trung cấp',
      title: 'Ngữ pháp và từ vựng Trung cấp 1',
      description: 'Nâng cao khả năng diễn đạt, thảo luận về các chủ đề xã hội, văn hóa.',
      duration: '8-10 tuần',
      status: 'locked',
      resources: [],
    },
  ],
};

export const specializedRoadmaps: Roadmap[] = [
  {
    id: 'grammar',
    title: 'Roadmap Ngữ pháp tiếng Hàn',
    description: 'Lộ trình học ngữ pháp tiếng Hàn từ cơ bản đến nâng cao, được sắp xếp theo độ khó và mức độ sử dụng.',
    steps: [
      {
        id: 1,
        level: 'Cơ bản',
        title: 'Ngữ pháp cơ bản - Nhóm 1',
        description: 'Các mẫu ngữ pháp thiết yếu nhất: tobe, adjective endings, object particles',
        duration: '2-3 tuần',
        status: 'available',
        resources: [
          { name: 'Mẫu câu "이에요/예요" (tobe)', type: 'document', url: '/ngu-phap#ieyo-yeyo' },
          { name: 'Ngữ pháp "-어서/-아서" (because)', type: 'document', url: '/ngu-phap#eo-seo-a-seo' },
          { name: 'Bài tập tổng hợp cơ bản', type: 'link', url: '/ngu-phap' },
        ],
      },
      {
        id: 2,
        level: 'Cơ bản',
        title: 'Ngữ pháp cơ bản - Nhóm 2', 
        description: 'Mở rộng với question particles, negation, conjunctions',
        duration: '2-3 tuần',
        status: 'available',
        resources: [
          { name: 'Ngữ pháp "-니까" (because/since)', type: 'document', url: '/ngu-phap#ni-kka' },
          { name: 'Ngữ pháp "-지만" (but/however)', type: 'document', url: '/ngu-phap#ji-man' },
          { name: 'Luyện tập ngữ pháp cơ bản', type: 'anki', url: '#' },
        ],
      },
      {
        id: 3,
        level: 'Trung cấp',
        title: 'Ngữ pháp trung cấp - Nhóm 1',
        description: 'Conditional forms, advanced tenses và complex sentence structures',
        duration: '3-4 tuần',
        status: 'available',
        resources: [
          { name: 'Ngữ pháp "-면" (if/when)', type: 'document', url: '/ngu-phap#myeon' },
          { name: 'Ngữ pháp "-고" (and/after)', type: 'document', url: '/ngu-phap#go' },
          { name: 'Bài tập conditional forms', type: 'link', url: '/ngu-phap' },
        ],
      },
      {
        id: 4,
        level: 'Nâng cao',
        title: 'Ngữ pháp nâng cao',
        description: 'Nominalization, advanced grammar patterns, literary forms',
        duration: '4-6 tuần',
        status: 'available',
        resources: [
          { name: 'Ngữ pháp "-은 것" (nominalization)', type: 'document', url: '/ngu-phap#eun-geot-2' },
          { name: 'Tổng hợp ngữ pháp nâng cao', type: 'document', url: '/ngu-phap' },
          { name: 'Luyện tập writing với ngữ pháp phức tạp', type: 'link', url: '#' },
        ],
      },
    ],
  },
  {
    id: 'travel',
    title: 'Roadmap cho người đi du lịch',
    description: 'Tập trung vào các mẫu câu, từ vựng và tình huống giao tiếp thực tế khi đi du lịch Hàn Quốc.',
    steps: [
        {
            id: 1,
            level: 'Cơ bản',
            title: 'Chào hỏi và giới thiệu bản thân',
            description: 'Học các câu chào hỏi, giới thiệu tên, tuổi, quốc tịch cơ bản.',
            duration: '1 ngày',
            status: 'available',
            resources: [
              { name: 'Mẫu câu giao tiếp sân bay', type: 'link', url: '#' },
            ],
          },
          {
            id: 2,
            level: 'Cơ bản',
            title: 'Hỏi đường và phương tiện đi lại',
            description: 'Các mẫu câu cần thiết để hỏi đường, đi taxi, tàu điện ngầm.',
            duration: '2 ngày',
            status: 'available',
            resources: [],
          },
    ],
  },
  {
    id: 'restaurant',
    title: 'Roadmap cho nhân viên nhà hàng',
    description: 'Từ vựng và mẫu câu chuyên dụng trong môi trường nhà hàng, từ nhận order đến thanh toán.',
    steps: [],
  },
  {
    id: 'topik',
    title: 'Roadmap luyện thi Topik',
    description: 'Chiến lược và tài liệu ôn luyện hiệu quả cho kỳ thi năng lực tiếng Hàn Topik I và II.',
    steps: [],
  },
  {
    id: 'eps',
    title: 'Roadmap xuất khẩu lao động EPS',
    description: 'Lộ trình chuyên biệt cho chương trình xuất khẩu lao động (EPS-TOPIK), bao gồm từ vựng chuyên ngành và kỹ năng giao tiếp tại nơi làm việc.',
    steps: [
      {
        id: 1,
        level: 'Cơ bản',
        title: 'Từ vựng chuyên ngành cơ bản',
        description: 'Học từ vựng về công việc, công cụ, an toàn lao động và giao tiếp cơ bản tại nơi làm việc.',
        duration: '3-4 tuần',
        status: 'available',
        resources: [
          { name: 'Sách EPS-TOPIK tiếng Việt', type: 'pdf', url: '#' },
          { name: 'Bộ thẻ từ vựng EPS', type: 'anki', url: '#' },
        ],
      },
      {
        id: 2,
        level: 'Trung cấp',
        title: 'Giao tiếp tại nơi làm việc',
        description: 'Luyện tập các tình huống giao tiếp thực tế: báo cáo công việc, xin phép, trao đổi với đồng nghiệp.',
        duration: '4-6 tuần',
        status: 'available',
        resources: [
          { name: 'Video tình huống EPS', type: 'video', url: '#' },
          { name: 'Mẫu câu giao tiếp công việc', type: 'document', url: '#' },
        ],
      },
      {
        id: 3,
        level: 'Nâng cao',
        title: 'Luyện thi EPS-TOPIK',
        description: 'Ôn luyện các dạng bài thi, làm quen với format EPS-TOPIK, luyện nghe và đọc hiểu.',
        duration: '6-8 tuần',
        status: 'coming-soon',
        resources: [],
      },
    ],
  }
];

// Export tổng hợp tất cả roadmaps
export const roadmaps: Roadmap[] = [coreRoadmap, ...specializedRoadmaps];
