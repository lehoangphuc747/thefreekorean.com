import React, { useState } from 'react';

const slides = [
  {
    title: 'The Free Korean',
    content: (
      <>
        <h2 style={{ color: '#bc52ee', fontSize: '1.5rem' }}>Tự học tiếng Hàn miễn phí</h2>
        <p><b>The Free Korean</b> là dự án giúp mọi người tự học tiếng Hàn với tài liệu miễn phí, các công cụ ôn tập được phát triển cho cả giáo viên và học sinh.</p>
        <p>Ngoài ra, bạn còn có thể luyện đề thi TOPIK với chức năng thi thật như iTOPIK.</p>
        <p style={{ color: '#888', fontSize: '1rem', marginTop: '1em' }}>Trang web hiện đang trong giai đoạn phát triển. Hãy theo dõi lộ trình phát triển bên dưới!</p>
      </>
    )
  },
  {
    title: 'Tính năng nổi bật',
    content: (
      <ul style={{ lineHeight: 1.7 }}>
        <li>Tài liệu học tiếng Hàn miễn phí, dễ tiếp cận.</li>
        <li>Công cụ ôn tập, luyện tập cho cả giáo viên và học sinh.</li>
        <li>Đề thi TOPIK online với trải nghiệm thi thật.</li>
        <li>Bộ thẻ Anki ôn tập bảng chữ cái Hangul.</li>
      </ul>
    )
  },
  {
    title: 'Roadmap phát triển',
    content: (
      <ol style={{ lineHeight: 1.7 }}>
        <li>Tạo các bài học, bài tập về Hangul kèm bộ thẻ Anki ôn tập bảng chữ cái.</li>
        <li>Tiếng Hàn tổng hợp, từ vựng (bổ sung thêm ngoài sách) và ngữ pháp + luyện tập nâng cao.</li>
        <li>Tiếng Hàn tổng hợp đang tập trung quyển 1. Quyển 2, 3, 4, 5, 6 đang đợi.</li>
        <li>Ôn TOPIK trên web với đầy đủ tài liệu miễn phí.</li>
      </ol>
    )
  }
];

export default function HomeSlides() {
  const [idx, setIdx] = useState(0);
  return (
    <div style={{ maxWidth: 700, margin: '2rem auto', padding: '2rem 1rem', fontFamily: 'Segoe UI, Arial, sans-serif', background: '#fff', borderRadius: 16, boxShadow: '0 2px 16px #0001' }}>
      <h1 style={{ fontSize: '2.2rem', marginBottom: '0.5em', color: '#3245ff' }}>{slides[idx].title}</h1>
      <div style={{ minHeight: 120 }}>{slides[idx].content}</div>
      <div style={{ display: 'flex', justifyContent: 'center', gap: 16, marginTop: 32 }}>
        <button onClick={() => setIdx(i => Math.max(0, i - 1))} disabled={idx === 0} style={{ padding: '8px 18px', borderRadius: 8, border: 'none', background: '#eee', color: '#3245ff', fontWeight: 600, cursor: idx === 0 ? 'not-allowed' : 'pointer' }}>Prev</button>
        <button onClick={() => setIdx(i => Math.min(slides.length - 1, i + 1))} disabled={idx === slides.length - 1} style={{ padding: '8px 18px', borderRadius: 8, border: 'none', background: '#3245ff', color: '#fff', fontWeight: 600, cursor: idx === slides.length - 1 ? 'not-allowed' : 'pointer' }}>Next</button>
      </div>
      <div style={{ display: 'flex', justifyContent: 'center', gap: 8, marginTop: 16 }}>
        {slides.map((_, i) => (
          <span key={i} style={{ width: 10, height: 10, borderRadius: '50%', background: i === idx ? '#bc52ee' : '#eee', display: 'inline-block' }}></span>
        ))}
      </div>
    </div>
  );
} 