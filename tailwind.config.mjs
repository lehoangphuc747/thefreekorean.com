/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      fontFamily: {
        'inter': ['Inter', 'system-ui', 'sans-serif'],
        'korean': ['Noto Sans KR', 'Malgun Gothic', '맑은 고딕', 'Apple SD Gothic Neo', 'sans-serif'],
      },
      colors: {
        primary: '#3245ff',
        secondary: '#bc52ee',
      },
      maxWidth: {
        'document-card': '280px',
      }
    },
  },
  plugins: [],
}
