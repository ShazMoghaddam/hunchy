/* Hunchy's service worker: keeps a copy of the game so it works offline.
   Pages and questions: try the network first so updates arrive straight away, and fall back to the copy offline.
   Everything else (styles, script, fonts, icons): use the copy at once and refresh it in the background.
   VERSION must match the latest version in CHANGELOG.md (a test checks). Changing it is what tells phones a new
   version exists: the new worker installs, clears the old copy, and the page reloads itself onto it. */
const VERSION = "hunchy-v1.2.0";
const SHELL = [
  "./",
  "index.html",
  "manifest.webmanifest",
  "assets/styles.css",
  "assets/app.js",
  "assets/fonts/urbanist-latin-wght-normal.woff2",
  "assets/fonts/urbanist-latin-ext-wght-normal.woff2",
  "assets/fonts/dm-mono-latin-500-normal.woff2",
  "assets/icons/favicon.svg",
  "assets/icons/icon-192.png",
  "data/questions.json",
  "data/jokes.json",
];

self.addEventListener("install", (event) => {
  // cache: "reload" skips the browser's own short-term cache, so a new version never stores yesterday's files.
  event.waitUntil(
    caches.open(VERSION)
      .then((cache) => cache.addAll(SHELL.map((url) => new Request(url, { cache: "reload" }))))
      .then(() => self.skipWaiting()),
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim()),
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  const url = new URL(req.url);
  if (req.method !== "GET" || url.origin !== self.location.origin) return; // leave other sites alone

  const networkFirst = req.mode === "navigate" || url.pathname.endsWith(".json");
  const key = req.mode === "navigate" ? "index.html" : url.pathname.endsWith(".json") ? new Request(url.pathname) : req;

  if (networkFirst) {
    event.respondWith(
      fetch(req)
        .then((res) => {
          if (res.ok) { const copy = res.clone(); caches.open(VERSION).then((c) => c.put(key, copy)); }
          return res;
        })
        .catch(() => caches.match(key, { ignoreSearch: true })),
    );
    return;
  }

  event.respondWith(
    caches.match(req, { ignoreSearch: true }).then((cached) => {
      const update = fetch(req)
        .then((res) => { if (res.ok) { const copy = res.clone(); caches.open(VERSION).then((c) => c.put(req, copy)); } return res; })
        .catch(() => cached);
      return cached || update;
    }),
  );
});
