import { defineCollection, z } from 'astro:content';

const grammar = defineCollection({
  type: 'content',
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

export const collections = {
  grammar
};
