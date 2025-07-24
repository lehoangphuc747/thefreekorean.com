import React from 'react';

export default function AboutSection() {
  return (
    <section className="bg-white rounded-2xl shadow-xl p-8 mb-10 border border-blue-100">
      <h2 className="text-2xl font-bold text-blue-700 mb-4">Xin chào! 👋</h2>
      <p className="text-lg text-gray-700 mb-4">
        Tôi là <span className="font-semibold text-blue-600">Lê Hoàng Phúc</span> - người sáng lập <span className="font-semibold text-purple-600">The Free Korean</span>.<br/>
        Đam mê giáo dục, công nghệ và chia sẻ tri thức, tôi xây dựng website này với mong muốn giúp mọi người học tiếng Hàn dễ dàng, miễn phí và hiệu quả nhất.
      </p>
    </section>
  );
}
