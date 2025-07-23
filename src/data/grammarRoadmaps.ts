export interface GrammarRoadmap {
  id: string;
  title: string;
  level: 'Beginner' | 'Intermediate' | 'Advanced';
  order: number;
  grammarPoints: GrammarPoint[];
  description: string;
  estimatedTime: string;
  prerequisites?: string[];
}

export interface GrammarPoint {
  id: string;
  grammarPattern: string;
  title: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  estimatedTime: string;
  prerequisites?: string[];
  relatedGrammar?: string[];
  isCompleted?: boolean;
}

export const grammarRoadmaps: GrammarRoadmap[] = [
  {
    id: 'beginner-foundations',
    title: '초급 기초 문법 (Beginner Foundations)',
    level: 'Beginner',
    order: 1,
    description: 'Các cấu trúc ngữ pháp cơ bản để xây dựng nền tảng tiếng Hàn vững chắc.',
    estimatedTime: '4-6 tuần',
    grammarPoints: [
      {
        id: 'go',
        grammarPattern: '-고',
        title: 'Liên từ "và, rồi"',
        difficulty: 'Easy',
        estimatedTime: '2-3 ngày',
        prerequisites: ['verb-stems', 'present-tense'],
        relatedGrammar: ['eo-seo-a-seo', 'ji-man']
      },
      {
        id: 'eo-seo-a-seo',
        grammarPattern: '-어서/-아서',
        title: 'Nguyên nhân - Kết quả',
        difficulty: 'Medium',
        estimatedTime: '3-4 ngày',
        prerequisites: ['go', 'vowel-harmony'],
        relatedGrammar: ['ni-kka', 'ttae-mune']
      },
      {
        id: 'ji-man',
        grammarPattern: '-지만',
        title: 'Sự đối lập "nhưng"',
        difficulty: 'Easy',
        estimatedTime: '2-3 ngày',
        prerequisites: ['go'],
        relatedGrammar: ['neunde', 'go']
      },
      {
        id: 'myeon',
        grammarPattern: '-면',
        title: 'Điều kiện "nếu, khi"',
        difficulty: 'Medium',
        estimatedTime: '3-4 ngày',
        prerequisites: ['eo-seo-a-seo'],
        relatedGrammar: ['neun-dae', 'ni-kka']
      },
      {
        id: 'ni-kka',
        grammarPattern: '-니까',
        title: 'Lý do chủ quan "vì"',
        difficulty: 'Medium',
        estimatedTime: '3-4 ngày',
        prerequisites: ['eo-seo-a-seo', 'myeon'],
        relatedGrammar: ['eo-seo-a-seo', 'ttae-mune']
      }
    ]
  },
  {
    id: 'beginner-nominalization',
    title: '초급 명사화 (Beginner Nominalization)',
    level: 'Beginner',
    order: 2,
    description: 'Cách biến đổi động từ và tính từ thành danh từ trong tiếng Hàn.',
    estimatedTime: '3-4 tuần',
    grammarPoints: [
      {
        id: 'eun-geot-1',
        grammarPattern: '-은 것1',
        title: 'Danh từ hóa động từ',
        difficulty: 'Medium',
        estimatedTime: '4-5 ngày',
        prerequisites: ['past-tense', 'verb-stems'],
        relatedGrammar: ['eun-geot-2', 'neun-geot']
      },
      {
        id: 'eun-geot-2',
        grammarPattern: '-은 것2',
        title: 'Danh từ hóa tính từ',
        difficulty: 'Medium',
        estimatedTime: '4-5 ngày',
        prerequisites: ['eun-geot-1', 'adjective-stems'],
        relatedGrammar: ['eun-geot-1', 'neun-geot']
      },
      {
        id: 'neun-geot',
        grammarPattern: '-는 것',
        title: 'Danh từ hóa hiện tại',
        difficulty: 'Medium',
        estimatedTime: '4-5 ngày',
        prerequisites: ['eun-geot-1', 'present-tense'],
        relatedGrammar: ['eun-geot-1', 'eul-geot']
      },
      {
        id: 'eul-geot',
        grammarPattern: '-을 것',
        title: 'Danh từ hóa tương lai',
        difficulty: 'Hard',
        estimatedTime: '5-6 ngày',
        prerequisites: ['neun-geot', 'future-tense'],
        relatedGrammar: ['neun-geot', 'eun-geot-1']
      }
    ]
  },
  {
    id: 'intermediate-time-reason',
    title: '중급 시간과 이유 (Intermediate Time & Reason)',
    level: 'Intermediate',
    order: 3,
    description: 'Các cấu trúc phức tạp hơn để diễn tả thời gian và lý do.',
    estimatedTime: '5-6 tuần',
    prerequisites: ['beginner-foundations', 'beginner-nominalization'],
    grammarPoints: [
      {
        id: 'ttae',
        grammarPattern: '-때',
        title: 'Thời điểm "khi, lúc"',
        difficulty: 'Medium',
        estimatedTime: '3-4 ngày',
        prerequisites: ['myeon', 'neun-geot'],
        relatedGrammar: ['myeon', 'neun-dae']
      },
      {
        id: 'ttae-mune',
        grammarPattern: '-때문에',
        title: 'Nguyên nhân chính thức',
        difficulty: 'Medium',
        estimatedTime: '3-4 ngày',
        prerequisites: ['ni-kka', 'eo-seo-a-seo'],
        relatedGrammar: ['ni-kka', 'euro-inhae']
      },
      {
        id: 'neun-dae',
        grammarPattern: '-는데/-은데',
        title: 'Tình huống nền "mà"',
        difficulty: 'Hard',
        estimatedTime: '5-6 ngày',
        prerequisites: ['ji-man', 'neun-geot'],
        relatedGrammar: ['ji-man', 'myeon']
      },
      {
        id: 'euro-inhae',
        grammarPattern: '으로 인해',
        title: 'Nguyên nhân trang trọng',
        difficulty: 'Hard',
        estimatedTime: '4-5 ngày',
        prerequisites: ['ttae-mune'],
        relatedGrammar: ['ttae-mune', 'ni-kka']
      }
    ]
  },
  {
    id: 'intermediate-expression',
    title: '중급 표현 (Intermediate Expression)',
    level: 'Intermediate',
    order: 4,
    description: 'Các cách diễn đạt tinh tế và đa dạng trong giao tiếp.',
    estimatedTime: '6-8 tuần',
    prerequisites: ['intermediate-time-reason'],
    grammarPoints: [
      {
        id: 'deogun-yo',
        grammarPattern: '-더군요',
        title: 'Ấn tượng từ quá khứ',
        difficulty: 'Hard',
        estimatedTime: '4-5 ngày',
        prerequisites: ['past-tense', 'neun-dae'],
        relatedGrammar: ['deokundeun', 'neun-deut']
      },
      {
        id: 'ja-nayo',
        grammarPattern: '-잖아요',
        title: 'Sự thật hiển nhiên',
        difficulty: 'Medium',
        estimatedTime: '3-4 ngày',
        prerequisites: ['neun-dae'],
        relatedGrammar: ['deogun-yo', 'jiyo']
      },
      {
        id: 'neun-deut',
        grammarPattern: '-는 듯',
        title: 'Suy đoán "có vẻ như"',
        difficulty: 'Hard',
        estimatedTime: '5-6 ngày',
        prerequisites: ['neun-geot', 'deogun-yo'],
        relatedGrammar: ['deogun-yo', 'na-bwa']
      }
    ]
  },
  {
    id: 'advanced-complex',
    title: '고급 복합 문법 (Advanced Complex Grammar)',
    level: 'Advanced',
    order: 5,
    description: 'Các cấu trúc ngữ pháp phức tạp cho trình độ cao.',
    estimatedTime: '8-10 tuần',
    prerequisites: ['intermediate-expression'],
    grammarPoints: [
      {
        id: 'deokundeun',
        grammarPattern: '-더구든',
        title: 'Hồi tưởng và nhấn mạnh',
        difficulty: 'Hard',
        estimatedTime: '6-7 ngày',
        prerequisites: ['deogun-yo', 'neun-deut'],
        relatedGrammar: ['deogun-yo', 'janayo']
      },
      {
        id: 'eo-ya-hal',
        grammarPattern: '-어야 할',
        title: 'Nghĩa vụ phải làm',
        difficulty: 'Hard',
        estimatedTime: '5-6 ngày',
        prerequisites: ['myeon', 'eul-geot'],
        relatedGrammar: ['myeon', 'gi-wihae']
      },
      {
        id: 'gi-wihae',
        grammarPattern: '-기 위해',
        title: 'Mục đích "để"',
        difficulty: 'Hard',
        estimatedTime: '6-7 ngày',
        prerequisites: ['gi-formation', 'eo-ya-hal'],
        relatedGrammar: ['eo-ya-hal', 'dorok']
      }
    ]
  }
];

export const getGrammarByLevel = (level: 'Beginner' | 'Intermediate' | 'Advanced') => {
  return grammarRoadmaps.filter(roadmap => roadmap.level === level);
};

export const getGrammarPointById = (id: string) => {
  for (const roadmap of grammarRoadmaps) {
    const point = roadmap.grammarPoints.find(point => point.id === id);
    if (point) return point;
  }
  return null;
};

export const getPrerequisites = (grammarId: string): string[] => {
  const point = getGrammarPointById(grammarId);
  return point?.prerequisites || [];
};

export const getRelatedGrammar = (grammarId: string): string[] => {
  const point = getGrammarPointById(grammarId);
  return point?.relatedGrammar || [];
};

export const getTotalGrammarPoints = () => {
  return grammarRoadmaps.reduce((total, roadmap) => total + roadmap.grammarPoints.length, 0);
};

export const getCompletedGrammarPoints = () => {
  return grammarRoadmaps.reduce((total, roadmap) => {
    return total + roadmap.grammarPoints.filter(point => point.isCompleted).length;
  }, 0);
};

export const getProgressPercentage = () => {
  const total = getTotalGrammarPoints();
  const completed = getCompletedGrammarPoints();
  return total > 0 ? Math.round((completed / total) * 100) : 0;
};
