import { useState, useEffect } from 'react';

const InteractiveDemo = () => {
  const [activeTab, setActiveTab] = useState('vocabulary');
  const [currentWord, setCurrentWord] = useState(0);
  const [isPlaying, setIsPlaying] = useState(false);

  const vocabulary = [
    { korean: '안녕하세요', vietnamese: 'Xin chào', romanized: 'annyeonghaseyo' },
    { korean: '감사합니다', vietnamese: 'Cảm ơn', romanized: 'gamsahabnida' },
    { korean: '죄송합니다', vietnamese: 'Xin lỗi', romanized: 'joesonghamnida' },
    { korean: '사랑해요', vietnamese: 'Yêu bạn', romanized: 'saranghaeyo' },
  ];

  const grammar = [
    { pattern: '~입니다/~습니다', usage: 'Thể lịch sự', example: '학생입니다 (Tôi là học sinh)' },
    { pattern: '~이에요/~예요', usage: 'Thể thân mật', example: '학생이에요 (Tôi là học sinh)' },
    { pattern: '~고 싶어요', usage: 'Muốn làm gì', example: '가고 싶어요 (Muốn đi)' },
  ];

  const levels = [
    { level: 'Sơ cấp', description: 'Học bảng chữ cái, từ vựng cơ bản', progress: 85 },
    { level: 'Trung cấp', description: 'Ngữ pháp, giao tiếp hàng ngày', progress: 60 },
    { level: 'Cao cấp', description: 'Văn phong, thành ngữ, TOPIK', progress: 30 },
  ];

  useEffect(() => {
    let interval;
    if (isPlaying && activeTab === 'vocabulary') {
      interval = setInterval(() => {
        setCurrentWord((prev) => (prev + 1) % vocabulary.length);
      }, 2000);
    }
    return () => clearInterval(interval);
  }, [isPlaying, activeTab]);

  const tabs = [
    { id: 'vocabulary', label: '📚 Từ vựng', icon: '📚' },
    { id: 'grammar', label: '📝 Ngữ pháp', icon: '📝' },
    { id: 'levels', label: '🎯 Lộ trình', icon: '🎯' }
  ];

  return (
    <div className="max-w-4xl mx-auto bg-white rounded-2xl shadow-2xl overflow-hidden">
      {/* Tab Navigation */}
      <div className="flex border-b border-gray-200">
        {tabs.map(tab => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`flex-1 py-4 px-6 text-center font-medium transition-all duration-300 ${
              activeTab === tab.id
                ? 'bg-blue-600 text-white border-b-2 border-blue-600'
                : 'text-gray-600 hover:text-blue-600 hover:bg-blue-50'
            }`}
          >
            <span className="text-xl mr-2">{tab.icon}</span>
            <span className="hidden sm:inline">{tab.label}</span>
          </button>
        ))}
      </div>

      {/* Tab Content */}
      <div className="p-8">
        {/* Vocabulary Tab */}
        {activeTab === 'vocabulary' && (
          <div className="text-center space-y-6">
            <div className="flex justify-center items-center gap-4 mb-6">
              <h3 className="text-2xl font-bold text-gray-800">Flashcard từ vựng</h3>
              <button
                onClick={() => setIsPlaying(!isPlaying)}
                className={`px-4 py-2 rounded-full font-medium transition-colors ${
                  isPlaying 
                    ? 'bg-red-500 text-white hover:bg-red-600' 
                    : 'bg-green-500 text-white hover:bg-green-600'
                }`}
              >
                {isPlaying ? '⏸️ Dừng' : '▶️ Phát'}
              </button>
            </div>
            
            <div className="bg-gradient-to-br from-blue-50 to-purple-50 rounded-xl p-8 transform transition-all duration-500 hover:scale-105">
              <div className="text-4xl font-bold text-blue-600 mb-2">
                {vocabulary[currentWord].korean}
              </div>
              <div className="text-xl text-gray-600 mb-2">
                {vocabulary[currentWord].romanized}
              </div>
              <div className="text-2xl font-semibold text-purple-600">
                {vocabulary[currentWord].vietnamese}
              </div>
            </div>
            
            <div className="flex justify-center gap-2">
              {vocabulary.map((_, index) => (
                <button
                  key={index}
                  onClick={() => setCurrentWord(index)}
                  className={`w-3 h-3 rounded-full transition-colors ${
                    index === currentWord ? 'bg-blue-600' : 'bg-gray-300'
                  }`}
                />
              ))}
            </div>
          </div>
        )}

        {/* Grammar Tab */}
        {activeTab === 'grammar' && (
          <div className="space-y-4">
            <h3 className="text-2xl font-bold text-gray-800 text-center mb-6">Ngữ pháp cơ bản</h3>
            {grammar.map((item, index) => (
              <div 
                key={index} 
                className="bg-gradient-to-r from-purple-50 to-blue-50 rounded-lg p-6 border-l-4 border-purple-500 hover:shadow-lg transition-all duration-300"
              >
                <div className="font-bold text-lg text-purple-700 mb-2">{item.pattern}</div>
                <div className="text-gray-600 mb-2">{item.usage}</div>
                <div className="text-blue-600 font-medium">{item.example}</div>
              </div>
            ))}
          </div>
        )}

        {/* Levels Tab */}
        {activeTab === 'levels' && (
          <div className="space-y-6">
            <h3 className="text-2xl font-bold text-gray-800 text-center mb-6">Lộ trình học tập</h3>
            {levels.map((level, index) => (
              <div key={index} className="bg-gray-50 rounded-lg p-6 hover:bg-gray-100 transition-colors">
                <div className="flex justify-between items-center mb-3">
                  <h4 className="font-bold text-lg text-gray-800">{level.level}</h4>
                  <span className="text-blue-600 font-medium">{level.progress}%</span>
                </div>
                <p className="text-gray-600 mb-3">{level.description}</p>
                <div className="w-full bg-gray-200 rounded-full h-2">
                  <div 
                    className="bg-gradient-to-r from-blue-500 to-purple-500 h-2 rounded-full transition-all duration-1000"
                    style={{ width: `${level.progress}%` }}
                  ></div>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default InteractiveDemo;
