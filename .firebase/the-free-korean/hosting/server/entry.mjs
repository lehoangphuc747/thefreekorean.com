import { renderers } from './renderers.mjs';
import { c as createExports, s as serverEntrypointModule } from './chunks/_@astrojs-ssr-adapter_JNSd7Yru.mjs';
import { manifest } from './manifest_DU1H5-JE.mjs';

const serverIslandMap = new Map();;

const _page0 = () => import('./pages/documents/_slug_.astro.mjs');
const _page1 = () => import('./pages/tai-lieu.astro.mjs');
const _page2 = () => import('./pages/index.astro.mjs');
const pageMap = new Map([
    ["src/pages/documents/[slug].astro", _page0],
    ["src/pages/tai-lieu.astro", _page1],
    ["src/pages/index.astro", _page2]
]);

const _manifest = Object.assign(manifest, {
    pageMap,
    serverIslandMap,
    renderers,
    actions: () => import('./_noop-actions.mjs'),
    middleware: () => import('./_noop-middleware.mjs')
});
const _args = {
    "mode": "standalone",
    "client": "file:///D:/A%20Web/the-free-korean/dist/client/",
    "server": "file:///D:/A%20Web/the-free-korean/dist/server/",
    "host": false,
    "port": 4321,
    "assets": "_astro",
    "experimentalStaticHeaders": false
};
const _exports = createExports(_manifest, _args);
const handler = _exports['handler'];
const startServer = _exports['startServer'];
const options = _exports['options'];
const _start = 'start';
if (_start in serverEntrypointModule) {
	serverEntrypointModule[_start](_manifest, _args);
}

export { handler, options, pageMap, startServer };
