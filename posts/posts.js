const posts = [
  {
    title: "Hello World",
    path: "posts/2025-01-01-hello-world.md",
    summary: "Welcome to our very first blog post!",
    date: "2025-01-01"
  }
];

if (typeof window !== 'undefined') {
  document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('posts-list');
    if (container) {
      posts.forEach(post => {
        const article = document.createElement('article');
        article.className = 'mb-6';
        article.innerHTML = `
          <h3 class="text-2xl font-semibold mb-2"><a href="${post.path}" class="text-blue-600 hover:underline">${post.title}</a></h3>
          <p class="text-gray-600">${post.summary}</p>
        `;
        container.appendChild(article);
      });
    }
  });
}
