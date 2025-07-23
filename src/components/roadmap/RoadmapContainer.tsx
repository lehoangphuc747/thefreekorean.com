// src/components/roadmap/RoadmapContainer.tsx
import React, { useState } from 'react';
import { coreRoadmap, specializedRoadmaps } from '../../data/roadmaps';
import type { Roadmap } from '../../types/roadmap';
import RoadmapSelector from './RoadmapSelector';
import RoadmapList from './RoadmapList';

interface RoadmapContainerProps {
  roadmaps: Roadmap[];
}

const RoadmapContainer: React.FC<RoadmapContainerProps> = ({ roadmaps }) => {
  const [selectedRoadmapId, setSelectedRoadmapId] = useState<string>('core');
  const [showRoadmapList, setShowRoadmapList] = useState(false);

  const selectedRoadmap = roadmaps.find(r => r.id === selectedRoadmapId) || roadmaps[0];

  const handleSelectRoadmap = (roadmapId: string) => {
    setSelectedRoadmapId(roadmapId);
    setShowRoadmapList(true);
  };

  const handleBackToSelector = () => {
    setShowRoadmapList(false);
  };

  return (
    <div className="w-full">
      {!showRoadmapList ? (
        <RoadmapSelector
          roadmaps={roadmaps}
          selectedRoadmapId={selectedRoadmapId}
          onSelectRoadmap={handleSelectRoadmap}
        />
      ) : (
        <div>
          {/* Back button */}
          <div className="mb-6">
            <button
              onClick={handleBackToSelector}
              className="flex items-center gap-2 px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg text-gray-700 transition-colors"
            >
              <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 19l-7-7 7-7" />
              </svg>
              <span>Chọn lộ trình khác</span>
            </button>
          </div>

          <RoadmapList roadmap={selectedRoadmap} />
        </div>
      )}
    </div>
  );
};

export default RoadmapContainer;
