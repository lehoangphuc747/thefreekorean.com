// src/types/roadmap.ts
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
