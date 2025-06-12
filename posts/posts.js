const posts = [
  {
    title: "Bí Quyết Phân Biệt Phụ Âm Thường, Bật Hơi và Căng Trong Tiếng Hàn",
    path: "blog/2025-02-01-phan-biet-phu-am-tieng-han.md",
    summary: "Học cách phân biệt 3 loại phụ âm trong tiếng Hàn một cách dễ dàng và hiệu quả nhất.",
    date: "2025-02-01",
    tags: ["phụ âm", "phát âm", "bật hơi", "căng"]
  },
  {
    title: "5 Mẹo Học Hangeul Hiệu Quả Cho Người Mới Bắt Đầu", 
    path: "blog/2025-01-15-hoc-hangeul-hieu-qua.md",
    summary: "Khám phá những mẹo học bảng chữ cái tiếng Hàn nhanh và nhớ lâu cho người mới bắt đầu.",
    date: "2025-01-15",
    tags: ["hangeul", "mẹo học", "người mới"]
  },
  {
    title: "Chào mừng đến với The Free Korean",
    path: "blog/2025-01-01-hello-world.md", 
    summary: "Ra mắt nền tảng học tiếng Hàn miễn phí được thiết kế đặc biệt cho người Việt Nam.",
    date: "2025-01-01",
    tags: ["giới thiệu", "tin tức"]
  }
];

if (typeof window !== 'undefined') {
  document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('posts-list');
    if (container) {
      posts.forEach(post => {
        const article = document.createElement('article');
        article.className = 'mb-8 bg-white rounded-xl p-6 shadow-lg hover:shadow-xl transition-shadow';
        article.innerHTML = `
          <div class="flex items-start justify-between mb-3">
            <h3 class="text-2xl font-bold mb-2">
              <a href="${post.path}" class="text-blue-600 hover:text-blue-800 transition-colors hover:underline">
                ${post.title}
              </a>
            </h3>
            <span class="text-sm text-gray-500 whitespace-nowrap ml-4">${post.date}</span>
          </div>
          <p class="text-gray-600 mb-4 leading-relaxed">${post.summary}</p>
          <div class="flex items-center justify-between">
            <div class="flex flex-wrap gap-2">
              ${post.tags ? post.tags.map(tag => `
                <span class="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full">${tag}</span>
              `).join('') : ''}
            </div>
            <a href="${post.path}" class="text-blue-600 hover:text-blue-800 font-semibold text-sm flex items-center space-x-1">
              <span>Đọc thêm</span>
              <i class="fas fa-arrow-right"></i>
            </a>
          </div>
        `;
        container.appendChild(article);
      });
    }
  });
}
