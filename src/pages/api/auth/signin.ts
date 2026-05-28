import type { APIRoute } from "astro";

export const POST: APIRoute = async ({ request, cookies, redirect }) => {
  const idToken = request.headers.get("Authorization")?.split("Bearer ")[1];
  
  if (!idToken) {
    return new Response(JSON.stringify({ error: "No token provided" }), { 
      status: 401,
      headers: { "Content-Type": "application/json" }
    });
  }

  cookies.set("__session", idToken, {
    path: "/",
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    maxAge: 60 * 60 * 24 * 5,
  });

  return redirect("/dashboard");
};
