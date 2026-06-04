import { handle } from '@astrojs/cloudflare/handler';
import { env } from 'cloudflare:workers';

export default {
  async fetch(request, ctx, env) {
    const url = new URL(request.url);
    
    // Handle API routes manually
    if (url.pathname.startsWith('/api/topik-audio/')) {
      const filename = url.pathname.replace('/api/topik-audio/', '');
      const key = `topik/${filename}`;
      console.log('[topik-audio] request', {
        pathname: url.pathname,
        filename,
        key,
        hasMediaBinding: Boolean(env.MEDIA),
      });
      
      try {
        const object = await env.MEDIA.get(key);
        console.log('[topik-audio] lookup result', {
          key,
          found: Boolean(object),
          contentType: object?.httpMetadata?.contentType,
        });
        
        if (!object) {
          console.warn('[topik-audio] not found', { key });
          return new Response('Not found', { status: 404 });
        }

        const headers = new Headers();
        headers.set('Content-Type', object.httpMetadata?.contentType || 'audio/mpeg');
        headers.set('Cache-Control', 'public, max-age=31536000');
        headers.set('Accept-Ranges', 'bytes');
        
        return new Response(object.body, { headers });
      } catch (err) {
        console.error('[topik-audio] internal error', {
          key,
          error: err instanceof Error ? err.message : String(err),
          stack: err instanceof Error ? err.stack : undefined,
        });
        return new Response('Internal error', { status: 500 });
      }
    }
    
    // For all other routes, use Astro's handler
    return handle(request, ctx, env);
  }
};
