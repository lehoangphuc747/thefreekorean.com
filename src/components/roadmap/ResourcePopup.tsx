// src/components/roadmap/ResourcePopup.tsx
import React, { useState } from 'react';
import type { RoadmapResource } from '../../types/roadmap';

interface ResourcePopupProps {
  resources: RoadmapResource[];
  isOpen: boolean;
  onClose: () => void;
  stepTitle: string;
}

const ResourceIcon = ({ type }: { type: RoadmapResource['type'] }) => {
  switch (type) {
    case 'video':
      return <div className="w-10 h-10 bg-red-100 rounded-full flex items-center justify-center">
        <span className="text-red-600 text-lg">📹</span>
      </div>;
    case 'pdf':
      return <div className="w-10 h-10 bg-blue-100 rounded-full flex items-center justify-center">
        <span className="text-blue-600 text-lg">📚</span>
      </div>;
    case 'anki':
      return <div className="w-10 h-10 bg-purple-100 rounded-full flex items-center justify-center">
        <span className="text-purple-600 text-lg">🔤</span>
      </div>;
    case 'document':
      return <div className="w-10 h-10 bg-green-100 rounded-full flex items-center justify-center">
        <span className="text-green-600 text-lg">📄</span>
      </div>;
    case 'link':
      return <div className="w-10 h-10 bg-orange-100 rounded-full flex items-center justify-center">
        <span className="text-orange-600 text-lg">🔗</span>
      </div>;
    default:
      return <div className="w-10 h-10 bg-gray-100 rounded-full flex items-center justify-center">
        <span className="text-gray-600 text-lg">📁</span>
      </div>;
  }
};

const ResourcePopup: React.FC<ResourcePopupProps> = ({ resources, isOpen, onClose, stepTitle }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* Backdrop */}
      <div 
        className="absolute inset-0 bg-black bg-opacity-50 transition-opacity"
        onClick={onClose}
      />
      
      {/* Modal */}
      <div className="relative bg-white rounded-2xl shadow-2xl max-w-md w-full mx-4 max-h-[80vh] overflow-hidden">
        {/* Header */}
        <div className="bg-gradient-to-r from-blue-500 to-purple-600 p-6 text-white">
          <div className="flex items-center justify-between">
            <h3 className="text-lg font-bold">Tài liệu học tập</h3>
            <button
              onClick={onClose}
              className="p-1 hover:bg-white/20 rounded-full transition-colors"
            >
              <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <p className="text-sm opacity-90 mt-1">{stepTitle}</p>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto max-h-96">
          {resources.length > 0 ? (
            <div className="space-y-4">
              {resources.map((resource, index) => (
                <div
                  key={index}
                  className="flex items-center gap-4 p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors group"
                >
                  <ResourceIcon type={resource.type} />
                  <div className="flex-1">
                    <h4 className="font-medium text-gray-800 group-hover:text-blue-600 transition-colors">
                      {resource.name}
                    </h4>
                    <p className="text-sm text-gray-500 capitalize">
                      {resource.type === 'video' && 'Video bài giảng'}
                      {resource.type === 'pdf' && 'Tài liệu PDF'}
                      {resource.type === 'anki' && 'Bộ thẻ Anki'}
                      {resource.type === 'document' && 'Tài liệu'}
                      {resource.type === 'link' && 'Liên kết'}
                    </p>
                  </div>
                  <a
                    href={resource.url}
                    className="flex items-center gap-2 px-3 py-1 bg-blue-500 text-white rounded-full text-sm hover:bg-blue-600 transition-colors"
                  >
                    <span>Mở</span>
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                    </svg>
                  </a>
                </div>
              ))}
            </div>
          ) : (
            <div className="text-center py-8">
              <div className="text-4xl mb-4">📚</div>
              <p className="text-gray-500">Chưa có tài liệu cho bước này</p>
              <p className="text-sm text-gray-400 mt-2">Tài liệu sẽ được cập nhật sớm</p>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="bg-gray-50 px-6 py-4 border-t">
          <div className="flex items-center justify-between">
            <span className="text-sm text-gray-500">
              {resources.length} tài liệu
            </span>
            <button
              onClick={onClose}
              className="px-4 py-2 bg-gray-200 hover:bg-gray-300 text-gray-700 rounded-lg text-sm font-medium transition-colors"
            >
              Đóng
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResourcePopup;
