# Docusaurus Migration Plan

## Current Structure Analysis

### Static HTML Files to Convert:
```
/
├── index.html                    → src/pages/index.js (React)
├── anki.html                     → docs/anki-downloads.md
├── navigation.js                 → Docusaurus theme/navbar config
└── phat-am/                      → docs/lessons/
    ├── Nguyên âm - TEST.html     → docs/lessons/vowels.mdx
    ├── Phụ âm thường - LUYỆN TẬP.html → docs/lessons/consonants-basic.mdx
    ├── Phụ âm bật hơi - LUYỆN TẬP.html → docs/lessons/consonants-aspirated.mdx
    ├── Phụ âm căng - LUYỆN TẬP.html → docs/lessons/consonants-tensed.mdx
    └── Phụ âm - LUYỆN TẬP*.html  → docs/lessons/consonants-practice.mdx
```

### Blog Structure (Ready for Docusaurus):
```
/blog/
├── 2025-01-01-hello-world.md
├── 2025-01-15-hoc-hangeul-hieu-qua.md
└── 2025-02-01-phan-biet-phu-am-tieng-han.md
```

## Docusaurus Configuration Plan

### 1. Site Config (docusaurus.config.js)
```javascript
module.exports = {
  title: 'The Free Korean',
  tagline: 'Học tiếng Hàn miễn phí - Từ cơ bản đến nâng cao',
  url: 'https://your-username.github.io',
  baseUrl: '/thefreekorean.com/',
  organizationName: 'your-username',
  projectName: 'thefreekorean.com',
  
  i18n: {
    defaultLocale: 'vi',
    locales: ['vi'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          routeBasePath: '/lessons',
          editUrl: 'https://github.com/your-username/thefreekorean.com/tree/main/',
        },
        blog: {
          showReadingTime: true,
          routeBasePath: '/blog',
          blogTitle: 'Tin tức & Mẹo học',
          blogDescription: 'Blog về học tiếng Hàn',
          postsPerPage: 10,
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'The Free Korean',
      logo: {
        alt: 'The Free Korean Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Bài học',
        },
        {
          to: '/anki-downloads',
          label: 'Anki Files',
          position: 'left'
        },
        {
          to: '/blog', 
          label: 'Blog', 
          position: 'left'
        },
        {
          href: 'https://github.com/your-username/thefreekorean.com',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Bài học',
          items: [
            {
              label: 'Nguyên âm',
              to: '/lessons/vowels',
            },
            {
              label: 'Phụ âm',
              to: '/lessons/consonants',
            },
          ],
        },
        {
          title: 'Tài nguyên',
          items: [
            {
              label: 'Anki Files',
              to: '/anki-downloads',
            },
            {
              label: 'Blog',
              to: '/blog',
            },
          ],
        },
        {
          title: 'Liên kết',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/your-username/thefreekorean.com',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} The Free Korean. Made with ❤️ for Vietnamese learners.`,
    },
  },
};
```

### 2. Sidebar Structure (sidebars.js)
```javascript
module.exports = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Phát âm cơ bản',
      items: [
        'lessons/vowels',
        'lessons/consonants-basic',
        'lessons/consonants-aspirated', 
        'lessons/consonants-tensed',
      ],
    },
    {
      type: 'category',
      label: 'Luyện tập',
      items: [
        'lessons/vowels-practice',
        'lessons/consonants-practice',
        'lessons/comprehensive-practice',
      ],
    },
    'anki-downloads',
  ],
};
```

### 3. Custom Components to Create
- **InteractivePronunciation**: Component cho bài tập phát âm
- **DragDropExercise**: Component drag-drop
- **AudioPlayer**: Component phát âm thanh
- **ProgressTracker**: Component theo dõi tiến độ
- **KoreanText**: Component hiển thị chữ Hàn với font phù hợp

### 4. Migration Steps

#### Phase 1: Setup
1. Create new Docusaurus project
2. Configure basic settings
3. Setup custom CSS with Korean fonts

#### Phase 2: Content Migration  
1. Convert blog posts (already in Markdown format ✅)
2. Convert static pages to Markdown/MDX
3. Extract reusable components from HTML

#### Phase 3: Interactive Features
1. Convert JavaScript exercises to React components
2. Implement drag-drop with libraries like react-dnd
3. Add audio playback functionality

#### Phase 4: Styling & Polish
1. Recreate current design with CSS modules
2. Add responsive improvements
3. Optimize performance

#### Phase 5: Deployment
1. Setup GitHub Actions for deployment
2. Configure domain (if needed)
3. Add SEO optimizations

## Benefits After Migration

### For Users:
- ⚡ Faster loading times
- 🔍 Built-in search functionality  
- 📱 Better mobile experience
- 🌏 Better SEO
- 🔖 Bookmark-able lessons

### For Developers:
- 📝 Easier content management (Markdown)
- 🔧 Component reusability
- 🚀 Better deployment pipeline
- 📊 Built-in analytics integration
- 🎨 Consistent theming

## Timeline Estimate
- **Week 1**: Docusaurus setup + basic config
- **Week 2**: Content migration (blog + static pages)  
- **Week 3**: Interactive components development
- **Week 4**: Styling + testing + deployment

---

*This plan ensures a smooth transition while maintaining all current functionality and improving user experience.*
