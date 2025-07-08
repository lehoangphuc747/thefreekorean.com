import React, { useState } from 'react';

const categories = {
  'Giáo trình': ['Tiếng Hàn Tổng Hợp', 'Seoul', 'Vitamin', 'New Korean', 'King Sejong'],
  'Tài liệu': ['Từ vựng', 'Ngữ pháp', 'Luyện nghe', 'Luyện đọc', 'Bài tập'],
  'Video': ['Hangul', 'Phát âm', 'Hội thoại', 'Ngữ pháp', 'TOPIK'],
  'Trang web': ['Từ điển', 'Luyện thi', 'Tin tức', 'K-pop', 'Phim/Drama']
};

const sampleDocuments = [
  { id: 1, title: 'Tiếng Hàn Tổng Hợp Sơ cấp 1', category: 'Giáo trình', subcategory: 'Tiếng Hàn Tổng Hợp', type: 'PDF', description: 'Giáo trình cơ bản cho người mới bắt đầu học tiếng Hàn.', image: 'https://via.placeholder.com/200x280/3245ff/ffffff?text=Tiếng+Hàn+Tổng+Hợp+1' },
  { id: 2, title: 'Tiếng Hàn Tổng Hợp Sơ cấp 2', category: 'Giáo trình', subcategory: 'Tiếng Hàn Tổng Hợp', type: 'PDF', description: 'Tiếp tục chương trình học sau quyển 1.', image: 'https://via.placeholder.com/200x280/bc52ee/ffffff?text=Tiếng+Hàn+Tổng+Hợp+2' },
  { id: 3, title: 'Seoul Korean Student Book 1A', category: 'Giáo trình', subcategory: 'Seoul', type: 'PDF', description: 'Giáo trình Seoul phổ biến dành cho sinh viên quốc tế.', image: 'https://via.placeholder.com/200x280/ff6b6b/ffffff?text=Seoul+Korean+1A' },
  { id: 4, title: 'Bảng từ vựng TOPIK I', category: 'Tài liệu', subcategory: 'Từ vựng', type: 'Excel', description: 'Danh sách từ vựng cần thiết cho kỳ thi TOPIK I.', image: 'https://via.placeholder.com/200x280/4ecdc4/ffffff?text=TOPIK+Vocabulary' },
  { id: 5, title: 'Video học Hangul cơ bản', category: 'Video', subcategory: 'Hangul', type: 'Video', description: 'Video hướng dẫn cách viết và đọc bảng chữ cái Hangul.', image: 'https://via.placeholder.com/200x280/45b7d1/ffffff?text=Hangul+Video' },
  { id: 6, title: 'iTOPIK - Thi thử online', category: 'Trang web', subcategory: 'Luyện thi', type: 'Website', description: 'Website luyện thi TOPIK với đầy đủ đề thi mẫu.', image: 'https://via.placeholder.com/200x280/96ceb4/ffffff?text=iTOPIK' }
];

export default function DocumentsList() {
  const [selectedCategory, setSelectedCategory] = useState('');
  const [selectedSubcategory, setSelectedSubcategory] = useState('');

  const filteredDocuments = sampleDocuments.filter(doc => {
    if (!selectedCategory) return true;
    if (selectedCategory && !selectedSubcategory) return doc.category === selectedCategory;
    return doc.category === selectedCategory && doc.subcategory === selectedSubcategory;
  });

  return (
    <div style={{ maxWidth: '1200px', margin: '0 auto', padding: '2rem 1rem', fontFamily: 'Segoe UI, Arial, sans-serif' }}>
      {/* Filter Bar */}
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', marginBottom: '2.5rem' }}>
        <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', justifyContent: 'center', marginBottom: '1rem' }}>
          <button
            onClick={() => { setSelectedCategory(''); setSelectedSubcategory(''); }}
            style={{
              padding: '0.5rem 1.2rem',
              background: !selectedCategory ? '#3245ff' : 'white',
              color: !selectedCategory ? 'white' : '#3245ff',
              border: '2px solid #3245ff',
              borderRadius: '6px',
              fontWeight: 600,
              cursor: 'pointer',
              transition: 'all 0.2s',
            }}
          >
            Tất cả
          </button>
          {Object.keys(categories).map(category => (
            <button
              key={category}
              onClick={() => { setSelectedCategory(category); setSelectedSubcategory(''); }}
              style={{
                padding: '0.5rem 1.2rem',
                background: selectedCategory === category && !selectedSubcategory ? '#3245ff' : 'white',
                color: selectedCategory === category && !selectedSubcategory ? 'white' : '#3245ff',
                border: '2px solid #3245ff',
                borderRadius: '6px',
                fontWeight: 600,
                cursor: 'pointer',
                transition: 'all 0.2s',
              }}
            >
              {category}
            </button>
          ))}
        </div>
        {/* Subcategory */}
        {selectedCategory && (
          <div style={{ display: 'flex', gap: '0.7rem', flexWrap: 'wrap', justifyContent: 'center', marginTop: '0.5rem' }}>
            {categories[selectedCategory].map(sub => (
              <button
                key={sub}
                onClick={() => setSelectedSubcategory(sub)}
                style={{
                  padding: '0.35rem 1rem',
                  background: selectedSubcategory === sub ? '#bc52ee' : 'white',
                  color: selectedSubcategory === sub ? 'white' : '#bc52ee',
                  border: '2px solid #bc52ee',
                  borderRadius: '6px',
                  fontWeight: 500,
                  cursor: 'pointer',
                  fontSize: '0.98rem',
                  transition: 'all 0.2s',
                }}
              >
                {sub}
              </button>
            ))}
          </div>
        )}
      </div>

      {/* Documents Grid */}
      <h1 style={{ color: '#3245ff', marginBottom: '1.5rem', fontSize: '2rem', textAlign: 'center' }}>
        📚 {selectedCategory || 'Tất cả tài liệu'}
        {selectedSubcategory && ` - ${selectedSubcategory}`}
      </h1>
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(250px, 1fr))',
        gap: '1.5rem'
      }}>
        {filteredDocuments.map(doc => (
          <div key={doc.id} style={{
            background: 'white',
            borderRadius: '12px',
            boxShadow: '0 4px 12px rgba(0,0,0,0.1)',
            border: '1px solid #eee',
            overflow: 'hidden',
            transition: 'transform 0.2s, box-shadow 0.2s',
            cursor: 'pointer'
          }}
          onMouseEnter={e => {
            e.currentTarget.style.transform = 'translateY(-4px)';
            e.currentTarget.style.boxShadow = '0 8px 20px rgba(0,0,0,0.15)';
          }}
          onMouseLeave={e => {
            e.currentTarget.style.transform = 'translateY(0)';
            e.currentTarget.style.boxShadow = '0 4px 12px rgba(0,0,0,0.1)';
          }}>
            {/* Image */}
            <div style={{ width: '100%', height: '200px', overflow: 'hidden' }}>
              <img
                src={doc.image}
                alt={doc.title}
                style={{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover'
                }}
              />
            </div>
            {/* Content */}
            <div style={{ padding: '1rem' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start', marginBottom: '0.5rem' }}>
                <h3 style={{
                  color: '#3245ff',
                  margin: 0,
                  fontSize: '1rem',
                  lineHeight: '1.3',
                  flex: 1
                }}>
                  {doc.title}
                </h3>
                <span style={{
                  background: '#e0d7ff',
                  color: '#3245ff',
                  padding: '0.2rem 0.5rem',
                  borderRadius: '4px',
                  fontSize: '0.7rem',
                  marginLeft: '0.5rem',
                  whiteSpace: 'nowrap'
                }}>
                  {doc.type}
                </span>
              </div>
              <p style={{
                color: '#666',
                marginBottom: '0.75rem',
                fontSize: '0.85rem',
                lineHeight: '1.4',
                display: '-webkit-box',
                WebkitLineClamp: 3,
                WebkitBoxOrient: 'vertical',
                overflow: 'hidden'
              }}>
                {doc.description}
              </p>
              <div style={{ display: 'flex', gap: '0.5rem', fontSize: '0.75rem' }}>
                <span style={{ color: '#bc52ee', fontWeight: '500' }}>{doc.category}</span>
                <span style={{ color: '#999' }}>→ {doc.subcategory}</span>
              </div>
            </div>
          </div>
        ))}
      </div>
      {filteredDocuments.length === 0 && (
        <p style={{ textAlign: 'center', color: '#999', marginTop: '2rem' }}>
          Không có tài liệu nào trong danh mục này.
        </p>
      )}
    </div>
  );
} 