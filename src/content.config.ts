import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const grammar = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/grammar' }),
  schema: z.object({
    title: z.string(),
    meaning: z.string(),
    level: z.enum(['beginner', 'intermediate', 'advanced']),
    slug: z.string().optional(),
    description: z.string(),
    tags: z.array(z.string()),
    order: z.number()
  })
});

export const collections = { grammar };
