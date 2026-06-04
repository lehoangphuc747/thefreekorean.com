import { handle } from '@astrojs/cloudflare/handler';
import fs from 'node:fs';
import path from 'node:path';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    if (url.pathname.startsWith('/api/topik-audio/')) {
      const filename = url.pathname.replace('/api/topik-audio/', '');
      const key = `topik/${filename}`;
      
      try {
        if (env.MEDIA) {
          const object = await env.MEDIA.get(key);
          if (!object) {
            return new Response('Not found', { status: 404 });
          }
          const headers = new Headers();
          headers.set('Content-Type', object.httpMetadata?.contentType || 'audio/mpeg');
          headers.set('Cache-Control', 'public, max-age=31536000');
          headers.set('Accept-Ranges', 'bytes');
          return new Response(object.body, { headers });
        }
        
        const localPath = path.join(process.cwd(), '.dev-assets', 'audio', filename);
        if (fs.existsSync(localPath)) {
          const stream = fs.createReadStream(localPath);
          const { Readable } = await import('node:stream');
          const readable = Readable.toWeb ? Readable.toWeb(stream) : Readable.from(stream);
          return new Response(readable, {
            headers: {
              'Content-Type': 'audio/mpeg',
              'Cache-Control': 'public, max-age=3600',
            },
          });
        }
        
        return new Response('Audio not available', { status: 404 });
      } catch (err) {
        console.error('[topik-audio] error:', err instanceof Error ? err.message : String(err));
        return new Response('Audio unavailable', { status: 503 });
      }
    }
    
    return handle(request, env, ctx);
  }
};
