import 'kleur/colors';
import { h as decodeKey } from './chunks/astro/server_BzKNCO4n.mjs';
import 'clsx';
import 'cookie';
import { N as NOOP_MIDDLEWARE_FN } from './chunks/astro-designed-error-pages_DD_KkEiI.mjs';
import 'es-module-lexer';

function sanitizeParams(params) {
  return Object.fromEntries(
    Object.entries(params).map(([key, value]) => {
      if (typeof value === "string") {
        return [key, value.normalize().replace(/#/g, "%23").replace(/\?/g, "%3F")];
      }
      return [key, value];
    })
  );
}
function getParameter(part, params) {
  if (part.spread) {
    return params[part.content.slice(3)] || "";
  }
  if (part.dynamic) {
    if (!params[part.content]) {
      throw new TypeError(`Missing parameter: ${part.content}`);
    }
    return params[part.content];
  }
  return part.content.normalize().replace(/\?/g, "%3F").replace(/#/g, "%23").replace(/%5B/g, "[").replace(/%5D/g, "]");
}
function getSegment(segment, params) {
  const segmentPath = segment.map((part) => getParameter(part, params)).join("");
  return segmentPath ? "/" + segmentPath : "";
}
function getRouteGenerator(segments, addTrailingSlash) {
  return (params) => {
    const sanitizedParams = sanitizeParams(params);
    let trailing = "";
    if (addTrailingSlash === "always" && segments.length) {
      trailing = "/";
    }
    const path = segments.map((segment) => getSegment(segment, sanitizedParams)).join("") + trailing;
    return path || "/";
  };
}

function deserializeRouteData(rawRouteData) {
  return {
    route: rawRouteData.route,
    type: rawRouteData.type,
    pattern: new RegExp(rawRouteData.pattern),
    params: rawRouteData.params,
    component: rawRouteData.component,
    generate: getRouteGenerator(rawRouteData.segments, rawRouteData._meta.trailingSlash),
    pathname: rawRouteData.pathname || void 0,
    segments: rawRouteData.segments,
    prerender: rawRouteData.prerender,
    redirect: rawRouteData.redirect,
    redirectRoute: rawRouteData.redirectRoute ? deserializeRouteData(rawRouteData.redirectRoute) : void 0,
    fallbackRoutes: rawRouteData.fallbackRoutes.map((fallback) => {
      return deserializeRouteData(fallback);
    }),
    isIndex: rawRouteData.isIndex,
    origin: rawRouteData.origin
  };
}

function deserializeManifest(serializedManifest) {
  const routes = [];
  for (const serializedRoute of serializedManifest.routes) {
    routes.push({
      ...serializedRoute,
      routeData: deserializeRouteData(serializedRoute.routeData)
    });
    const route = serializedRoute;
    route.routeData = deserializeRouteData(serializedRoute.routeData);
  }
  const assets = new Set(serializedManifest.assets);
  const componentMetadata = new Map(serializedManifest.componentMetadata);
  const inlinedScripts = new Map(serializedManifest.inlinedScripts);
  const clientDirectives = new Map(serializedManifest.clientDirectives);
  const serverIslandNameMap = new Map(serializedManifest.serverIslandNameMap);
  const key = decodeKey(serializedManifest.key);
  return {
    // in case user middleware exists, this no-op middleware will be reassigned (see plugin-ssr.ts)
    middleware() {
      return { onRequest: NOOP_MIDDLEWARE_FN };
    },
    ...serializedManifest,
    assets,
    componentMetadata,
    inlinedScripts,
    clientDirectives,
    routes,
    serverIslandNameMap,
    key
  };
}

const manifest = deserializeManifest({"hrefRoot":"file:///D:/A%20Web/the-free-korean/","cacheDir":"file:///D:/A%20Web/the-free-korean/node_modules/.astro/","outDir":"file:///D:/A%20Web/the-free-korean/dist/","srcDir":"file:///D:/A%20Web/the-free-korean/src/","publicDir":"file:///D:/A%20Web/the-free-korean/public/","buildClientDir":"file:///D:/A%20Web/the-free-korean/dist/client/","buildServerDir":"file:///D:/A%20Web/the-free-korean/dist/server/","adapterName":"@astrojs/node","routes":[{"file":"","links":[],"scripts":[],"styles":[],"routeData":{"type":"page","component":"_server-islands.astro","params":["name"],"segments":[[{"content":"_server-islands","dynamic":false,"spread":false}],[{"content":"name","dynamic":true,"spread":false}]],"pattern":"^\\/_server-islands\\/([^/]+?)\\/?$","prerender":false,"isIndex":false,"fallbackRoutes":[],"route":"/_server-islands/[name]","origin":"internal","_meta":{"trailingSlash":"ignore"}}},{"file":"tai-lieu/index.html","links":[],"scripts":[],"styles":[],"routeData":{"route":"/tai-lieu","isIndex":false,"type":"page","pattern":"^\\/tai-lieu\\/?$","segments":[[{"content":"tai-lieu","dynamic":false,"spread":false}]],"params":[],"component":"src/pages/tai-lieu.astro","pathname":"/tai-lieu","prerender":true,"fallbackRoutes":[],"distURL":[],"origin":"project","_meta":{"trailingSlash":"ignore"}}},{"file":"index.html","links":[],"scripts":[],"styles":[],"routeData":{"route":"/","isIndex":true,"type":"page","pattern":"^\\/$","segments":[],"params":[],"component":"src/pages/index.astro","pathname":"/","prerender":true,"fallbackRoutes":[],"distURL":[],"origin":"project","_meta":{"trailingSlash":"ignore"}}}],"base":"/","trailingSlash":"ignore","compressHTML":true,"componentMetadata":[["D:/A Web/the-free-korean/src/pages/documents/[slug].astro",{"propagation":"none","containsHead":true}],["D:/A Web/the-free-korean/src/pages/index.astro",{"propagation":"none","containsHead":true}],["D:/A Web/the-free-korean/src/pages/tai-lieu.astro",{"propagation":"none","containsHead":true}]],"renderers":[],"clientDirectives":[["idle","(()=>{var l=(n,t)=>{let i=async()=>{await(await n())()},e=typeof t.value==\"object\"?t.value:void 0,s={timeout:e==null?void 0:e.timeout};\"requestIdleCallback\"in window?window.requestIdleCallback(i,s):setTimeout(i,s.timeout||200)};(self.Astro||(self.Astro={})).idle=l;window.dispatchEvent(new Event(\"astro:idle\"));})();"],["load","(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event(\"astro:load\"));})();"],["media","(()=>{var n=(a,t)=>{let i=async()=>{await(await a())()};if(t.value){let e=matchMedia(t.value);e.matches?i():e.addEventListener(\"change\",i,{once:!0})}};(self.Astro||(self.Astro={})).media=n;window.dispatchEvent(new Event(\"astro:media\"));})();"],["only","(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).only=e;window.dispatchEvent(new Event(\"astro:only\"));})();"],["visible","(()=>{var a=(s,i,o)=>{let r=async()=>{await(await s())()},t=typeof i.value==\"object\"?i.value:void 0,c={rootMargin:t==null?void 0:t.rootMargin},n=new IntersectionObserver(e=>{for(let l of e)if(l.isIntersecting){n.disconnect(),r();break}},c);for(let e of o.children)n.observe(e)};(self.Astro||(self.Astro={})).visible=a;window.dispatchEvent(new Event(\"astro:visible\"));})();"]],"entryModules":{"\u0000noop-middleware":"_noop-middleware.mjs","\u0000noop-actions":"_noop-actions.mjs","\u0000@astro-page:src/pages/documents/[slug]@_@astro":"pages/documents/_slug_.astro.mjs","\u0000@astro-page:src/pages/tai-lieu@_@astro":"pages/tai-lieu.astro.mjs","\u0000@astro-page:src/pages/index@_@astro":"pages/index.astro.mjs","\u0000@astrojs-ssr-virtual-entry":"entry.mjs","\u0000@astro-renderers":"renderers.mjs","\u0000@astrojs-ssr-adapter":"_@astrojs-ssr-adapter.mjs","\u0000@astrojs-manifest":"manifest_DU1H5-JE.mjs","D:/A Web/the-free-korean/node_modules/unstorage/drivers/fs-lite.mjs":"chunks/fs-lite_COtHaKzy.mjs","D:/A Web/the-free-korean/src/documents/anki-tieng-han-tong-hop-1-bai-1.mdx":"chunks/anki-tieng-han-tong-hop-1-bai-1_DHoh5ybp.mjs","D:/A Web/the-free-korean/src/documents/hangul-video.mdx":"chunks/hangul-video_BicTOr3k.mjs","D:/A Web/the-free-korean/src/documents/huong-dan.mdx":"chunks/huong-dan_BD528dKA.mjs","D:/A Web/the-free-korean/src/documents/itopik-website.mdx":"chunks/itopik-website_PupLwBRq.mjs","D:/A Web/the-free-korean/src/documents/seoul-korean-1a.mdx":"chunks/seoul-korean-1a_DM8J4z5u.mjs","D:/A Web/the-free-korean/src/documents/tai-lieu.mdx":"chunks/tai-lieu_7R7PjiXU.mjs","D:/A Web/the-free-korean/src/documents/tieng-han-tong-hop-1.mdx":"chunks/tieng-han-tong-hop-1_C9XhMbFP.mjs","D:/A Web/the-free-korean/src/documents/topik-vocabulary.mdx":"chunks/topik-vocabulary_DO5XNrNs.mjs","@astrojs/react/client.js":"_astro/client.Co0vMr8l.js","D:/A Web/the-free-korean/src/pages/documents/[slug].astro?astro&type=script&index=0&lang.ts":"_astro/_slug_.astro_astro_type_script_index_0_lang.DFPKrgYF.js","D:/A Web/the-free-korean/src/pages/tai-lieu.astro?astro&type=script&index=0&lang.ts":"_astro/tai-lieu.astro_astro_type_script_index_0_lang.DbPW6vHf.js","D:/A Web/the-free-korean/src/components/ScrollToTop.astro?astro&type=script&index=0&lang.ts":"_astro/ScrollToTop.astro_astro_type_script_index_0_lang.VHijKjDe.js","D:/A Web/the-free-korean/src/components/document/FilterSection.astro?astro&type=script&index=0&lang.ts":"_astro/FilterSection.astro_astro_type_script_index_0_lang.BVHGsZgd.js","D:/A Web/the-free-korean/src/components/document/DocumentGrid.astro?astro&type=script&index=0&lang.ts":"_astro/DocumentGrid.astro_astro_type_script_index_0_lang.D6FUwWoG.js","astro:scripts/before-hydration.js":""},"inlinedScripts":[["D:/A Web/the-free-korean/src/pages/documents/[slug].astro?astro&type=script&index=0&lang.ts","document.addEventListener(\"DOMContentLoaded\",function(){window.location.hash===\"#download-section\"&&setTimeout(()=>{const o=document.getElementById(\"download-section\");o&&o.scrollIntoView({behavior:\"smooth\",block:\"start\"})},100)});"],["D:/A Web/the-free-korean/src/pages/tai-lieu.astro?astro&type=script&index=0&lang.ts","document.addEventListener(\"DOMContentLoaded\",function(){const i=document.querySelectorAll(\".filter-button\"),n=document.querySelectorAll(\".subcategory-filter\"),g=document.querySelectorAll(\".document-card-wrapper\"),y=document.getElementById(\"documents-grid\"),c=document.getElementById(\"empty-state\");let a=\"all\",o=\"all\";i.forEach(e=>{e.addEventListener(\"click\",function(){a=this.getAttribute(\"data-category\")||\"all\",o=\"all\",u(),d(),s()})}),n.forEach(e=>{e.addEventListener(\"click\",function(){o=this.getAttribute(\"data-subcategory\")||\"all\",f(),s()})});function u(){i.forEach(e=>{(e.getAttribute(\"data-category\")||\"all\")===a?e.classList.add(\"active\"):e.classList.remove(\"active\")})}function f(){n.forEach(e=>{const t=e.getAttribute(\"data-subcategory\")||\"all\";e.getAttribute(\"data-category\")===a&&(t===o?e.classList.add(\"active\"):e.classList.remove(\"active\"))})}function d(){document.querySelectorAll(\".subcategory-section\").forEach(t=>{const l=t.getAttribute(\"data-category\");a===\"all\"?t.style.display=\"none\":l===a?t.style.display=\"block\":t.style.display=\"none\"})}function s(){let e=0;if(g.forEach(t=>{const l=t.getAttribute(\"data-category\"),b=t.getAttribute(\"data-subcategory\");let r=!0;a!==\"all\"&&l!==a&&(r=!1),o!==\"all\"&&b!==o&&(r=!1),r?(t.style.display=\"block\",e++):t.style.display=\"none\"}),e===0){const t=y?.querySelector(\".grid\");t&&(t.style.display=\"none\"),c&&(c.style.display=\"block\")}else{const t=y?.querySelector(\".grid\");t&&(t.style.display=\"grid\"),c&&(c.style.display=\"none\")}}u(),d(),s()});"],["D:/A Web/the-free-korean/src/components/ScrollToTop.astro?astro&type=script&index=0&lang.ts","document.addEventListener(\"DOMContentLoaded\",function(){const e=document.getElementById(\"scroll-to-top\");let o=!1;function s(){const t=(window.pageYOffset||document.documentElement.scrollTop)>300;t&&!o?(e.classList.add(\"visible\"),o=!0):!t&&o&&(e.classList.remove(\"visible\"),o=!1)}function c(){const n=window.pageYOffset,t=performance.now(),a=600;function i(r){const d=r-t,l=Math.min(d/a,1),u=1-Math.pow(1-l,3);window.scrollTo(0,n*(1-u)),l<1&&requestAnimationFrame(i)}requestAnimationFrame(i)}window.addEventListener(\"scroll\",s,{passive:!0}),e.addEventListener(\"click\",c),s()});"],["D:/A Web/the-free-korean/src/components/document/FilterSection.astro?astro&type=script&index=0&lang.ts","document.addEventListener(\"DOMContentLoaded\",function(){const c=document.querySelectorAll(\"#filter-buttons .filter-btn\"),l=document.querySelectorAll(\"#subcategory-filters .subcategory-btn\"),y=document.querySelectorAll(\".document-card-wrapper\"),g=document.querySelectorAll(\"#subcategory-filters [data-parent-category]\"),n=document.getElementById(\"empty-state\");let a=\"\",r=\"\";function i(){let t=0;y.forEach(e=>{const o=e.getAttribute(\"data-category\"),d=e.getAttribute(\"data-subcategory\");let s=!0;a&&o!==a&&(s=!1),r&&d!==r&&(s=!1),s?(e.style.display=\"block\",t++):e.style.display=\"none\"}),n&&(n.style.display=t===0?\"block\":\"none\")}function u(){c.forEach(t=>{(t.getAttribute(\"data-category\")||\"\")===a?(t.classList.add(\"bg-blue-700\",\"text-white\"),t.classList.remove(\"bg-white\",\"text-gray-700\",\"border-gray-300\")):(t.classList.remove(\"bg-blue-700\",\"text-white\"),t.classList.add(\"bg-white\",\"text-gray-700\",\"border-gray-300\"))}),l.forEach(t=>{(t.getAttribute(\"data-subcategory\")||\"\")===r?(t.classList.add(\"bg-blue-600\",\"text-white\"),t.classList.remove(\"bg-gray-100\",\"text-gray-600\")):(t.classList.remove(\"bg-blue-600\",\"text-white\"),t.classList.add(\"bg-gray-100\",\"text-gray-600\"))})}c.forEach(t=>{t.addEventListener(\"click\",function(){a=this.getAttribute(\"data-category\")||\"\",r=\"\",g.forEach(e=>{const o=e.getAttribute(\"data-parent-category\");a===\"\"||o===a?e.style.display=a?\"flex\":\"none\":e.style.display=\"none\"}),u(),i()})}),l.forEach(t=>{t.addEventListener(\"click\",function(){r=this.getAttribute(\"data-subcategory\")||\"\",u(),i()})})});"],["D:/A Web/the-free-korean/src/components/document/DocumentGrid.astro?astro&type=script&index=0&lang.ts","document.addEventListener(\"DOMContentLoaded\",function(){document.querySelectorAll(\".document-card-wrapper\").forEach(n=>{n.addEventListener(\"click\",function(o){const t=o.target;if(t?.tagName===\"A\"||t?.closest(\"a\")||t?.tagName===\"BUTTON\"||t?.closest(\"button\"))return;const e=this.getAttribute(\"data-slug\");e&&(window.location.href=`/documents/${e}`)})})});"]],"assets":["/_astro/_slug_.CeWu3RBd.css","/_astro/_slug_.CYa0ZXp7.css","/favicon.svg","/downloads/tieng-han-tong-hop-1.pdf","/images/hangul-video.jpg","/images/huong-dan.jpg","/images/itopik-website.jpg","/images/seoul-korean-1a.jpg","/images/tai-lieu.jpg","/images/tieng-han-tong-hop-1.jpg","/images/tieng-han-tong-hop-1.svg","/images/topik-vocabulary.jpg","/_astro/client.Co0vMr8l.js","/tai-lieu/index.html","/index.html"],"buildFormat":"directory","checkOrigin":true,"serverIslandNameMap":[],"key":"QJ0erB7tj3mqQgV4LvBiyX2LBhTDSENc5k2F85z0eQE=","sessionConfig":{"driver":"fs-lite","options":{"base":"D:\\A Web\\the-free-korean\\node_modules\\.astro\\sessions"}}});
if (manifest.sessionConfig) manifest.sessionConfig.driverModule = () => import('./chunks/fs-lite_COtHaKzy.mjs');

export { manifest };
