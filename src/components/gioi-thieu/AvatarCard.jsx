import React from 'react';

export default function AvatarCard() {
  return (
    <div className="flex flex-col items-center mb-10">
      <div className="w-32 h-32 rounded-full overflow-hidden shadow-lg border-4 border-blue-200 mb-6 bg-white flex items-center justify-center">
        <span className="text-6xl">👨‍💻</span>
      </div>
      <h1 className="text-4xl font-extrabold text-gray-900 mb-2 text-center">Lê Hoàng Phúc</h1>
      <a
        href="https://www.facebook.com/tui.la.phuc747/"
        target="_blank"
        rel="noopener noreferrer"
        className="inline-flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-full font-semibold text-lg shadow hover:from-blue-700 hover:to-purple-700 transition-all"
      >
        <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M22.675 0h-21.35C.595 0 0 .592 0 1.326v21.348C0 23.408.595 24 1.325 24h11.495v-9.294H9.692v-3.622h3.128V8.413c0-3.1 1.893-4.788 4.659-4.788 1.325 0 2.463.099 2.797.143v3.24l-1.918.001c-1.504 0-1.797.715-1.797 1.763v2.313h3.587l-.467 3.622h-3.12V24h6.116C23.406 24 24 23.408 24 22.674V1.326C24 .592 23.406 0 22.675 0"/></svg>
        Facebook
      </a>
    </div>
  );
}
