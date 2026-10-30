/* Local stand-in for Vercel: serves public/ and runs api/lead.mjs at /api/lead and /api/lead/:action (the same rewrite
 * as vercel.json). With --fake-upstream it sets test keys, answers the Ecomail and Meta calls itself and records them
 * at GET /__calls, so the whole form → thank-you flow runs with nothing leaving the machine.
 *
 * Run: node tools/dev_server.mjs --port 8010 --fake-upstream
 */
import fs from "node:fs";
import http from "node:http";
import path from "node:path";
import { fileURLToPath } from "node:url";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const PUBLIC = path.join(ROOT, "public");
const argv = process.argv.slice(2);
const port = Number(argv[argv.indexOf("--port") + 1]) || 8010;
const fake = argv.includes("--fake-upstream");
const calls = [];

if (fake) {
  Object.assign(process.env, {
    ECOMAIL_API_KEY: "test-key", ECOMAIL_LIST_PDF: "11", ECOMAIL_LIST_TIPS: "12",
    META_PIXEL_ID: "000000000000001", META_CAPI_TOKEN: "test-token",
  });
  globalThis.fetch = async (url, opts = {}) => {
    const u = new URL(String(url));
    calls.push({ method: opts.method || "GET", host: u.host, path: u.pathname, query: Object.fromEntries(u.searchParams),
      key: opts.headers && opts.headers.key, body: opts.body ? JSON.parse(opts.body) : null });
    if (u.host === "graph.facebook.com") return Response.json({ events_received: 1 });
    if ((opts.method || "GET") === "GET") return Response.json({ errors: ["not found"] }, { status: 404 });
    return Response.json({ id: 259471, email: "x" });
  };
}
const handler = (await import("../api/lead.mjs")).default;

const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".css": "text/css", ".json": "application/json",
  ".svg": "image/svg+xml", ".webp": "image/webp", ".png": "image/png", ".pdf": "application/pdf", ".woff2": "font/woff2", ".txt": "text/plain" };

http.createServer(async (req, res) => {
  const u = new URL(req.url, `http://${req.headers.host}`);
  if (u.pathname === "/__calls") {
    res.writeHead(200, { "Content-Type": "application/json" });
    return res.end(JSON.stringify(calls));
  }
  const api = u.pathname.match(/^\/api\/lead(?:\/([^/]+))?\/?$/);
  if (api) {
    const chunks = [];
    for await (const c of req) chunks.push(c);
    if (api[1]) u.searchParams.set("action", api[1]);
    const headers = new Headers(Object.entries(req.headers).filter(([, v]) => typeof v === "string"));
    headers.set("x-forwarded-for", req.socket.remoteAddress || "");
    const body = ["GET", "HEAD"].includes(req.method) ? undefined : Buffer.concat(chunks);
    const out = await handler.fetch(new Request(u, { method: req.method, headers, body }));
    res.writeHead(out.status, Object.fromEntries(out.headers));
    return res.end(Buffer.from(await out.arrayBuffer()));
  }
  let file = path.join(PUBLIC, decodeURIComponent(u.pathname));
  if (!file.startsWith(PUBLIC)) { res.writeHead(403); return res.end(); }
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, "index.html");
  if (!fs.existsSync(file)) {
    res.writeHead(404, { "Content-Type": TYPES[".html"] });
    return res.end(fs.readFileSync(path.join(PUBLIC, "404.html")));
  }
  res.writeHead(200, { "Content-Type": TYPES[path.extname(file)] || "application/octet-stream" });
  fs.createReadStream(file).pipe(res);
}).listen(port, "127.0.0.1", () => console.log(`public/ + /api/lead on http://127.0.0.1:${port}${fake ? " (fake Ecomail/Meta, calls at /__calls)" : ""}`));
