import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const kienThuc = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/topik/kien-thuc' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional(),
    category: z.string().optional(),
    level: z.enum(['TOPIK I', 'TOPIK II']).optional(),
    tags: z.array(z.string()).optional(),
    date: z.string().optional(),
  }),
});

const dangDe = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/topik/dang-de' }),
  schema: z.object({
    meta: z.object({
      title: z.string(),
      type: z.enum(['reading', 'listening', 'writing']),
      slug: z.string(),
      range: z.string(),
      level: z.string(),
    }),
    questions: z.array(z.object({
      id: z.number(),
      exam: z.string(),
      group_instruction: z.string().optional(),
      group_instruction_vi: z.string().optional(),
      question_ko: z.string(),
      question_vi: z.string().optional(),
      image: z.string().optional(),
      choices: z.array(z.union([
        z.string(),
        z.object({
          type: z.string(),
          text: z.string(),
          image: z.string().optional(),
        })
      ])),
      answer: z.union([z.number(), z.string()]),
      explain: z.string(),
    })),
  }),
});

// Thi-thu collection (exam simulation)
const thiThu = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/topik/thi-thu' }),
  schema: z.object({
    meta: z.object({
      title: z.string(),
      level: z.enum(['TOPIK I', 'TOPIK II']),
      duration: z.number(), // phút
      totalQuestions: z.number(),
      description: z.string().optional(),
    }),
    sections: z.array(z.object({
      type: z.enum(['listening', 'reading', 'writing']),
      title: z.string(),
      duration: z.number(), // phút
      audio: z.string().optional(),
      questions: z.array(z.object({
        id: z.number(),
        group_instruction: z.string().optional(),
        group_instruction_vi: z.string().optional(),
        question_ko: z.string(),
        question_vi: z.string().optional(),
        image: z.string().optional(),
        audio: z.string().optional(),
        choices: z.array(z.union([
          z.string(),
          z.object({
            type: z.string(),
            text: z.string(),
            image: z.string().optional(),
          })
        ])),
        answer: z.union([z.number(), z.string()]),
        model_answer: z.string().optional(),
        points: z.number().optional(),
        minChars: z.number().optional(),
        maxChars: z.number().optional(),
      })),
    })),
  }),
});

export const collections = { 'kien-thuc': kienThuc, 'dang-de': dangDe, 'thi-thu': thiThu };
