// src/components/roadmap/RoadmapList.tsx
import React from 'react';
import type { Roadmap } from '../../types/roadmap';
import RoadmapCard from './RoadmapCard';

interface RoadmapListProps {
  roadmap: Roadmap;
}

const RoadmapList: React.FC<RoadmapListProps> = ({ roadmap }) => {
  return (
    <div className="max-w-4xl mx-auto">
      {/* Header */}
      <div className="text-center mb-8">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">{roadmap.title}</h2>
        <p className="text-gray-600 text-sm">{roadmap.description}</p>
      </div>
      
      {/* Steps */}
      <div className="space-y-6">
        {roadmap.steps.map((step, index) => (
          <div key={step.id} className="relative">
            {/* Connector line */}
            {index < roadmap.steps.length - 1 && (
              <div className="absolute left-4 top-16 w-0.5 h-12 bg-gray-200"></div>
            )}
            <RoadmapCard step={step} index={index} />
          </div>
        ))}
        
        {roadmap.steps.length === 0 && (
          <div className="p-8 bg-gray-50 rounded-xl text-center">
            <div className="text-4xl mb-4">🚧</div>
            <p className="text-gray-500">Lộ trình này đang được xây dựng</p>
            <p className="text-sm text-gray-400 mt-2">Vui lòng quay lại sau!</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default RoadmapList;
