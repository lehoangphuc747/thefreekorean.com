// src/components/roadmap/RoadmapCategoryTabs.tsx
import React from 'react';
import type { Roadmap } from '../../types/roadmap';

interface RoadmapCategoryTabsProps {
  roadmaps: Roadmap[];
  selectedRoadmapId: string;
  onSelectRoadmap: (roadmapId: string) => void;
}

const RoadmapCategoryTabs: React.FC<RoadmapCategoryTabsProps> = ({ roadmaps, selectedRoadmapId, onSelectRoadmap }) => {
  return (
    <div className="flex justify-center mb-8">
      <div className="flex flex-wrap justify-center gap-1 p-1 bg-gray-100 rounded-lg">
        {roadmaps.map((roadmap) => (
          <button
            key={roadmap.id}
            onClick={() => onSelectRoadmap(roadmap.id)}
            className={`px-4 py-2 text-sm font-medium rounded-md transition-all duration-200
              ${selectedRoadmapId === roadmap.id
                ? 'bg-white text-blue-600 shadow-sm font-semibold'
                : 'text-gray-600 hover:text-gray-900 hover:bg-gray-50'
              }`}
          >
            {roadmap.title}
          </button>
        ))}
      </div>
    </div>
  );
};

export default RoadmapCategoryTabs;
