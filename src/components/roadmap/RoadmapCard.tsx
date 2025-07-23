// src/components/roadmap/RoadmapCard.tsx
import React, { useState } from 'react';
import type { RoadmapStep } from '../../types/roadmap';
import ResourcePopup from './ResourcePopup';

const RoadmapCard: React.FC<{ step: RoadmapStep; index: number }> = ({ step, index }) => {
  const [isPopupOpen, setIsPopupOpen] = useState(false);
  const getStatusStyle = (status: RoadmapStep['status']) => {
    switch (status) {
      case 'available':
        return 'bg-green-50 border-green-200 text-green-800';
      case 'coming-soon':
        return 'bg-yellow-50 border-yellow-200 text-yellow-800';
      case 'locked':
        return 'bg-gray-50 border-gray-200 text-gray-500';
      default:
        return 'bg-gray-50 border-gray-200 text-gray-500';
    }
  };

  const getStatusIcon = (status: RoadmapStep['status']) => {
    switch (status) {
      case 'available':
        return '✅';
      case 'coming-soon':
        return '⏳';
      case 'locked':
        return '🔒';
      default:
        return '⚪';
    }
  };

  return (
    <div className={`relative border-2 rounded-xl p-6 transition-all duration-300 hover:shadow-lg ${getStatusStyle(step.status)}`}>
      {/* Step number */}
      <div className="absolute -left-4 top-6 w-8 h-8 bg-gradient-to-r from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white font-bold text-sm">
        {index + 1}
      </div>
      
      {/* Content */}
      <div className="ml-6">
        <div className="flex items-center gap-3 mb-3">
          <span className="text-lg">{getStatusIcon(step.status)}</span>
          <span className="text-sm font-medium opacity-75">{step.level}</span>
          <span className="text-sm opacity-60">• {step.duration}</span>
        </div>
        
        <h3 className="font-bold text-lg mb-2">{step.title}</h3>
        <p className="text-sm opacity-80 mb-4">{step.description}</p>
        
        {/* Resources - simplified */}
        {step.resources.length > 0 && (
          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-600">
              {step.resources.length} tài liệu
            </span>
            <button
              onClick={() => setIsPopupOpen(true)}
              className="flex items-center gap-2 px-3 py-1 bg-blue-500 hover:bg-blue-600 text-white rounded-full text-sm font-medium transition-colors"
            >
              <span></span>
              <span>Xem tài liệu</span>
            </button>
          </div>
        )}
      </div>

      {/* Resource Popup */}
      <ResourcePopup
        resources={step.resources}
        isOpen={isPopupOpen}
        onClose={() => setIsPopupOpen(false)}
        stepTitle={step.title}
      />
    </div>
  );
};

export default RoadmapCard;
