// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

import react from '@astrojs/react';

import mdx from '@astrojs/mdx';

import cloudflare from '@astrojs/cloudflare';

// https://astro.build/config
export default defineConfig({
  site: 'https://thefreekorean.com',
  output: 'server',

  vite: {
    plugins: [tailwindcss()],
    ssr: {
      noExternal: ['@tailwindcss/vite']
    },
    optimizeDeps: {
      exclude: ['astro:content', 'astro:zod']
    }
  },

  integrations: [react(), mdx()],
  adapter: cloudflare()
});