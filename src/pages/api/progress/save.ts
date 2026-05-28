import type { APIRoute } from "astro";

export const POST: APIRoute = async ({ request, cookies }) => {
  const sessionCookie = cookies.get("__session")?.value;
  
  if (!sessionCookie) {
    return new Response(JSON.stringify({ error: "Unauthorized" }), { 
      status: 401,
      headers: { "Content-Type": "application/json" }
    });
  }

  try {
    const body = await request.json();
    const { exerciseSlug, questionId, selectedAnswer, isCorrect } = body;
    
    if (!exerciseSlug || questionId === undefined || selectedAnswer === undefined) {
      return new Response(JSON.stringify({ error: "Missing required fields" }), { 
        status: 400,
        headers: { "Content-Type": "application/json" }
      });
    }

    // Lưu vào KV (sử dụng Cloudflare KV binding)
    const key = `progress:${sessionCookie.substring(0, 20)}:${exerciseSlug}`;
    
    // Lấy progress hiện tại
    let progress: Record<string, any> = {};
    try {
      const existing = await (Astro.locals as any).env?.SESSION?.get(key);
      if (existing) {
        progress = JSON.parse(existing);
      }
    } catch (e) {
      // Không có progress cũ
    }

    // Cập nhật progress
    progress[questionId] = {
      selectedAnswer,
      isCorrect,
      timestamp: Date.now(),
    };

    // Lưu vào KV
    await (Astro.locals as any).env?.SESSION?.put(key, JSON.stringify(progress), {
      expirationTtl: 60 * 60 * 24 * 30, // 30 ngày
    });

    return new Response(JSON.stringify({ success: true }), { 
      status: 200,
      headers: { "Content-Type": "application/json" }
    });
  } catch (error: any) {
    console.error("Error saving progress:", error);
    return new Response(JSON.stringify({ error: error.message }), { 
      status: 500,
      headers: { "Content-Type": "application/json" }
    });
  }
};
