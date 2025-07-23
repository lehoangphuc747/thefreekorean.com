// src/components/roadmap/RoadmapSelector.tsx
import React, { useState } from 'react';
import type { Roadmap } from '../../types/roadmap';

interface RoadmapOption {
  roadmap: Roadmap;
  icon: string;
  color: string;
  tags: string[];
  level: 'Mới bắt đầu' | 'Đã có nền tảng' | 'Mục tiêu cụ thể';
  duration: string;
}

interface RoadmapSelectorProps {
  roadmaps: Roadmap[];
  onSelectRoadmap: (roadmapId: string) => void;
  selectedRoadmapId: string;
}

const RoadmapSelector: React.FC<RoadmapSelectorProps> = ({ roadmaps, onSelectRoadmap, selectedRoadmapId }) => {
  const [selectedFilter, setSelectedFilter] = useState<string>('all');

  const roadmapOptions: RoadmapOption[] = [
    {
      roadmap: roadmaps.find(r => r.id === 'core')!,
      icon: '🎯',
      color: 'from-blue-500 to-purple-600',
      tags: ['Toàn diện', 'Nền tảng', 'Lâu dài'],
      level: 'Mới bắt đầu',
      duration: '6-12 tháng'
    },
    {
      roadmap: roadmaps.find(r => r.id === 'grammar')!,
      icon: '📚',
      color: 'from-emerald-500 to-cyan-600',
      tags: ['Ngữ pháp', 'Cấu trúc', 'Nền tảng'],
      level: 'Mới bắt đầu',
      duration: '3-4 tháng'
    },
    {
      roadmap: roadmaps.find(r => r.id === 'travel')!,
      icon: '✈️',
      color: 'from-green-500 to-teal-600',
      tags: ['Du lịch', 'Ngắn hạn', 'Thực tế'],
      level: 'Mới bắt đầu',
      duration: '1-2 tháng'
    },
    {
      roadmap: roadmaps.find(r => r.id === 'restaurant')!,
      icon: '🍽️',
      color: 'from-orange-500 to-red-600',
      tags: ['Chuyên ngành', 'Nghề nghiệp', 'Thực tế'],
      level: 'Mục tiêu cụ thể',
      duration: '3-4 tháng'
    },
    {
      roadmap: roadmaps.find(r => r.id === 'topik')!,
      icon: '📝',
      color: 'from-purple-500 to-pink-600',
      tags: ['Thi cử', 'Chứng chỉ', 'Học thuật'],
      level: 'Đã có nền tảng',
      duration: '4-6 tháng'
    },
    {
      roadmap: roadmaps.find(r => r.id === 'eps')!,
      icon: '🏭',
      color: 'from-indigo-500 to-blue-600',
      tags: ['Xuất khẩu lao động', 'EPS-TOPIK', 'Nghề nghiệp'],
      level: 'Mục tiêu cụ thể',
      duration: '4-6 tháng'
    }
  ].filter(option => option.roadmap);

  const filters = [
    { id: 'all', label: 'Tất cả', icon: '🌟' },
    { id: 'beginner', label: 'Mới bắt đầu', icon: '🌱' },
    { id: 'foundation', label: 'Đã có nền tảng', icon: '🏗️' },
    { id: 'specific', label: 'Mục tiêu cụ thể', icon: '🎯' }
  ];

  const filteredOptions = roadmapOptions.filter(option => {
    if (selectedFilter === 'all') return true;
    if (selectedFilter === 'beginner') return option.level === 'Mới bắt đầu';
    if (selectedFilter === 'foundation') return option.level === 'Đã có nền tảng';
    if (selectedFilter === 'specific') return option.level === 'Mục tiêu cụ thể';
    return true;
  });

  return (
    <div className="max-w-6xl mx-auto">
      {/* Header */}
      <div className="text-center mb-8">
        <h2 className="text-2xl md:text-3xl font-bold mb-3 text-gray-800">
          Chọn lộ trình phù hợp với bạn
        </h2>
        <p className="text-gray-600 max-w-2xl mx-auto">
          Mỗi lộ trình được thiết kế cho một mục tiêu cụ thể. Hãy chọn lộ trình phù hợp nhất với nhu cầu của bạn.
        </p>
      </div>

      {/* Filters */}
      <div className="flex flex-wrap justify-center gap-2 mb-8">
        {filters.map(filter => (
          <button
            key={filter.id}
            onClick={() => setSelectedFilter(filter.id)}
            className={`flex items-center gap-2 px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 ${
              selectedFilter === filter.id
                ? 'bg-blue-500 text-white shadow-lg'
                : 'bg-gray-100 hover:bg-gray-200 text-gray-700'
            }`}
          >
            <span>{filter.icon}</span>
            {filter.label}
          </button>
        ))}
      </div>

      {/* Roadmap Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredOptions.map(option => (
          <div
            key={option.roadmap.id}
            className={`relative bg-white rounded-2xl shadow-lg overflow-hidden transition-all duration-300 transform hover:scale-105 cursor-pointer ${
              selectedRoadmapId === option.roadmap.id ? 'ring-4 ring-blue-500 ring-opacity-50' : ''
            }`}
            onClick={() => onSelectRoadmap(option.roadmap.id)}
          >
            {/* Gradient Header */}
            <div className={`h-32 bg-gradient-to-r ${option.color} flex items-center justify-center relative`}>
              <div className="text-6xl">{option.icon}</div>
              {selectedRoadmapId === option.roadmap.id && (
                <div className="absolute top-2 right-2 bg-white rounded-full p-1">
                  <svg className="w-4 h-4 text-blue-500" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                </div>
              )}
            </div>

            {/* Content */}
            <div className="p-6">
              <div className="flex items-center justify-between mb-3">
                <span className="text-sm font-medium text-blue-600">{option.level}</span>
                <span className="text-sm text-gray-500">⏱️ {option.duration}</span>
              </div>
              
              <h3 className="font-bold text-lg mb-2 text-gray-800">{option.roadmap.title}</h3>
              <p className="text-gray-600 text-sm mb-4 line-clamp-2">{option.roadmap.description}</p>
              
              {/* Tags */}
              <div className="flex flex-wrap gap-1 mb-4">
                {option.tags.map(tag => (
                  <span
                    key={tag}
                    className="px-2 py-1 bg-gray-100 text-gray-600 text-xs rounded-full"
                  >
                    {tag}
                  </span>
                ))}
              </div>

              {/* Steps count */}
              <div className="flex items-center justify-between">
                <span className="text-sm text-gray-500">
                  {option.roadmap.steps.length} bước học
                </span>
                <div className="flex items-center gap-1 text-sm text-blue-600">
                  <span>Chi tiết</span>
                  <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                  </svg>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* Help Text */}
      <div className="mt-8 p-6 bg-gradient-to-r from-blue-50 to-purple-50 rounded-xl">
        <div className="text-center">
          <h3 className="font-bold text-gray-800 mb-2">💡 Không chắc chọn lộ trình nào?</h3>
          <p className="text-sm text-gray-600 mb-3">
            Hãy bắt đầu với <strong>Lộ trình Cốt lõi</strong> nếu bạn hoàn toàn mới hoặc muốn xây dựng nền tảng vững chắc.
          </p>
          <p className="text-xs text-gray-500">
            Bạn có thể thay đổi lộ trình bất cứ lúc nào!
          </p>
        </div>
      </div>
    </div>
  );
};

export default RoadmapSelector;
