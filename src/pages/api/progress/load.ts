import type { APIRoute } from "astro";

export const GET: APIRoute = async ({ url, cookies }) => {
  const sessionCookie = cookies.get("__session")?.value;
  
  if (!sessionCookie) {
    return new Response(JSON.stringify({ error: "Unauthorized" }), { 
      status: 401,
      headers: { "Content-Type": "application/json" }
    });
  }

  try {
    const exerciseSlug = url.searchParams.get("slug");
    
    if (!exerciseSlug) {
      return new Response(JSON.stringify({ error: "Missing slug parameter" }), { 
        status: 400,
        headers: { "Content-Type": "application/json" }
      });
    }

    const key = `progress:${sessionCookie.substring(0, 20)}:${exerciseSlug}`;
    
    let progress: Record<string, any> = {};
    try {
      const existing = await (Astro.locals as any).env?.SESSION?.get(key);
      if (existing) {
        progress = JSON.parse(existing);
      }
    } catch (e) {
      // Không có progress
    }

    return new Response(JSON.stringify({ progress }), { 
      status: 200,
      headers: { "Content-Type": "application/json" }
    });
  } catch (error: any) {
    console.error("Error loading progress:", error);
    return new Response(JSON.stringify({ error: error.message }), { 
      status: 500,
      headers: { "Content-Type": "application/json" }
    });
  }
};
