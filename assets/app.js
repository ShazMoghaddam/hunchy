/* Hunchy: go with your hunch.
   A small, dependency-free game. Questions live in data/questions.json; progress is kept in this browser only. */
(() => {
  "use strict";

  const SITE = "https://shazmoghaddam.github.io/hunchy/";
  const REPO = "https://github.com/ShazMoghaddam/hunchy";
  const ROUND = 10;
  const LIVES = 3;
  const KIND = { "choice": "Pick one", "yes-no": "Yes or no", "higher-lower": "Higher or lower" };

  const app = document.getElementById("app");
  const announce = document.getElementById("announce");
  let bank = null;          // { categories, questions }
  let game = null;          // the round being played
  let audience = "everyone"; // "everyone" or "easier"
  let jokes = [];           // loaded from data/jokes.json; the game still works if they don't load
  let grownUps = false;     // grown-up jokes are off unless someone switches them on
  let shownJoke = null;     // the joke on screen, for sharing
  let sound = true;         // little sounds and a buzz on phones; one switch turns both off
  let theme = "dark";       // "dark" (the default) or "light"
  let updateWaiting = false; // a new version is ready but a round is being played
  let reloading = false;

  // Storage. Browsers can refuse it (private windows, blocked cookies), so every call is guarded and the game
  // works without it; it just won't remember streaks.
  const store = {
    get(key, fallback) {
      try { const v = localStorage.getItem("hunchy:" + key); return v === null ? fallback : JSON.parse(v); }
      catch { return fallback; }
    },
    set(key, value) { try { localStorage.setItem("hunchy:" + key, JSON.stringify(value)); } catch { /* not saved */ } },
  };

  // Text goes into the page through this, so a question can never inject markup.
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const icon = (name, cls = "") => `<svg class="icon ${cls}" aria-hidden="true"><use href="#i-${name}"/></svg>`;
  const say = (text) => { announce.textContent = ""; setTimeout(() => { announce.textContent = text; }, 30); };

  // Dates use the player's own calendar, so a whole family on one sofa shares the same daily ten.
  const todayKey = () => { const d = new Date(); return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`; };
  const dayBefore = (key) => { const d = new Date(key + "T12:00:00"); d.setDate(d.getDate() - 1); return d.toISOString().slice(0, 10); };
  const niceDate = (key) => new Date(key + "T12:00:00").toLocaleDateString("en-GB", { weekday: "long", day: "numeric", month: "long" });

  // A small seeded random number generator, so the daily ten is the same on every device.
  function seeded(text) {
    let h = 1779033703 ^ text.length;
    for (let i = 0; i < text.length; i++) { h = Math.imul(h ^ text.charCodeAt(i), 3432918353); h = (h << 13) | (h >>> 19); }
    let a = h >>> 0;
    return () => { a |= 0; a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; };
  }
  const shuffle = (list, rnd = Math.random) => { const a = list.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
  const pickOne = (list, rnd = Math.random) => list[Math.floor(rnd() * list.length)];

  const allowed = (q, who) => who === "everyone" || q.difficulty <= 2;
  // "1,200+" rather than "1,260": rounds down to the hundred, so the wording stays true as questions are added.
  const roundedCount = () => `${(Math.floor(bank.questions.length / 100) * 100).toLocaleString("en-GB")}+`;
  const plural = (n, word) => `${n} ${word}${n === 1 ? "" : "s"}`;

  // Choosing questions ------------------------------------------------------------------------

  // Ten questions from ten different subjects, with two of each quick kind and something for every generation.
  function dailyTen(key) {
    const rnd = seeded("hunchy-" + key);
    const cats = shuffle(Object.keys(bank.categories), rnd).slice(0, ROUND);
    const kinds = shuffle(["higher-lower", "higher-lower", "yes-no", "yes-no", "choice", "choice", "choice", "choice", "choice", "choice"], rnd);
    const levels = shuffle([1, 1, 1, 2, 2, 2, 2, 3, 3, 2], rnd);
    const picked = cats.map((cat, i) => {
      const inCat = bank.questions.filter((q) => q.category === cat);
      const exact = inCat.filter((q) => q.type === kinds[i] && q.difficulty === levels[i]);
      const sameKind = inCat.filter((q) => q.type === kinds[i]);
      return pickOne(exact.length ? exact : sameKind.length ? sameKind : inCat, rnd);
    });
    // Make sure there's at least one classic and one modern question, so nobody at the table is left out.
    for (const era of ["classic", "modern"]) {
      if (picked.some((q) => q.era === era)) continue;
      for (let i = 0; i < picked.length; i++) {
        const swap = bank.questions.filter((q) => q.category === picked[i].category && q.era === era && q.type === picked[i].type);
        if (swap.length) { picked[i] = pickOne(swap, rnd); break; }
      }
    }
    return picked;
  }

  // Questions this browser hasn't seen yet come first, so quick rounds don't repeat until the bank runs out.
  function fresh(pool, count) {
    const seen = new Set(store.get("seen", []));
    let unseen = pool.filter((q) => !seen.has(q.id));
    if (unseen.length < count) { store.set("seen", []); unseen = pool; }
    return balanced(shuffle(unseen), count);
  }

  // Spread the kinds of question through a round instead of clumping them.
  function balanced(list, count) {
    const byType = { "choice": [], "yes-no": [], "higher-lower": [] };
    list.forEach((q) => byType[q.type].push(q));
    const order = ["choice", "higher-lower", "choice", "yes-no"];
    const out = [];
    let i = 0;
    while (out.length < count && (byType.choice.length || byType["yes-no"].length || byType["higher-lower"].length)) {
      const want = order[i++ % order.length];
      const from = byType[want].length ? byType[want] : byType.choice.length ? byType.choice : byType["yes-no"].length ? byType["yes-no"] : byType["higher-lower"];
      out.push(from.shift());
    }
    return out;
  }

  function markSeen(id) {
    const seen = store.get("seen", []);
    // Every question is remembered (about 9 KB for the whole bank), so nothing repeats until the pile runs out.
    if (!seen.includes(id)) { seen.push(id); store.set("seen", seen); }
  }

  // Stats: kept in this browser only, like everything else.
  const emptyStats = () => ({ answered: 0, right: 0, games: 0, perfect: 0, cats: {} });
  function getStats() {
    const st = store.get("stats", null);
    return st && typeof st === "object" && st.cats ? { ...emptyStats(), ...st } : emptyStats();
  }
  function recordAnswer(q, right) {
    const st = getStats();
    st.answered++; if (right) st.right++;
    const c = st.cats[q.category] || [0, 0];
    st.cats[q.category] = [c[0] + 1, c[1] + (right ? 1 : 0)];
    store.set("stats", st);
  }
  function recordGame(perfect) {
    const st = getStats();
    st.games++; if (perfect) st.perfect++;
    store.set("stats", st);
  }
  function longestStreak() {
    const days = store.get("days", []).slice().sort();
    let best = 0, run = 0, prev = null;
    for (const d of days) {
      run = prev && dayBefore(d) === prev ? run + 1 : 1;
      best = Math.max(best, run); prev = d;
    }
    return best;
  }

  // Sound and buzz. Tones are made on the fly with Web Audio, so there are no sound files to download.
  let audio = null;
  function tone(freq, start, length, type = "sine", volume = 0.07) {
    const t = audio.currentTime + start;
    const osc = audio.createOscillator(); const gain = audio.createGain();
    osc.type = type; osc.frequency.setValueAtTime(freq, t);
    gain.gain.setValueAtTime(0.0001, t);
    gain.gain.exponentialRampToValueAtTime(volume, t + 0.015);
    gain.gain.exponentialRampToValueAtTime(0.0001, t + length);
    osc.connect(gain).connect(audio.destination);
    osc.start(t); osc.stop(t + length + 0.02);
  }
  function play(kind) {
    if (!sound) return;
    try {
      audio = audio || new (window.AudioContext || window.webkitAudioContext)();
      if (audio.state === "suspended") audio.resume();
      if (kind === "right") { tone(784, 0, 0.12); tone(1175, 0.08, 0.18); }
      else if (kind === "wrong") { tone(220, 0, 0.22, "triangle", 0.09); tone(175, 0.1, 0.26, "triangle", 0.08); }
      else if (kind === "done") { tone(659, 0, 0.14); tone(784, 0.11, 0.14); tone(1047, 0.22, 0.3); }
    } catch { /* no audio on this device */ }
    try { navigator.vibrate?.(kind === "wrong" ? [35, 45, 35] : kind === "right" ? 15 : [15, 40, 15, 40, 30]); } catch { /* no buzz */ }
  }

  function applyTheme() {
    document.documentElement.dataset.theme = theme;
    document.querySelector('meta[name="theme-color"]')?.setAttribute("content", theme === "light" ? "#F4F3FA" : "#0D1230");
  }

  // Screens ---------------------------------------------------------------------------------

  function render(html, focus = true) {
    app.innerHTML = html;
    if (focus) { app.focus({ preventScroll: true }); window.scrollTo({ top: 0 }); }
  }

  const logo = `
    <a class="logo" href="#" data-go="home" aria-label="Hunchy home">
      <svg class="logo-mark" viewBox="0 0 40 40" aria-hidden="true">
        <defs><linearGradient id="logo-g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7C5CFF"/><stop offset="1" stop-color="#B44CFF"/></linearGradient></defs>
        <rect x="1" y="1" width="38" height="38" rx="12" fill="url(#logo-g)"/>
        <path d="M13 16.5l6.5-6.5 6.5 6.5" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M14 23.5l6.5 6.5 6.5-6.5" fill="none" stroke="#FFB27A" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/>
      </svg>
      <span class="logo-word">hunchy</span>
    </a>`;

  function streakChip() {
    const s = currentStreak();
    const label = s === 1 ? "1 day streak" : `${s} day streak`;
    return `<span class="streak ${s ? "" : "cold"}" title="Days in a row you've played the daily ten">${icon("flame")}<span>${s}</span><span class="sr-only">${label}</span></span>`;
  }

  function currentStreak() {
    const days = new Set(store.get("days", []));
    let key = todayKey();
    if (!days.has(key)) key = dayBefore(key); // today not played yet: the streak still counts from yesterday
    let n = 0;
    while (days.has(key)) { n++; key = dayBefore(key); }
    return n;
  }

  function home() {
    game = null;
    if (updateWaiting && !reloading) { reloading = true; location.reload(); return; } // a new version arrived mid-game
    const key = todayKey();
    const done = store.get("daily", {})[key];
    const counts = {};
    bank.questions.forEach((q) => { counts[q.category] = (counts[q.category] || 0) + 1; });
    const tiles = Object.entries(bank.categories).map(([cat, name]) => `
      <button class="piece tile" data-cat="${cat}" data-go="quick" data-pick="${cat}">
        <span class="disc">${icon(cat)}</span><span>${esc(name)}</span><span class="count">${counts[cat]} questions</span>
      </button>`).join("");

    render(`
      <div class="wrap">
        <header class="top">${logo}<div class="right">${streakChip()}</div></header>

        <section class="card today" aria-labelledby="today-title">
          <svg class="fan" viewBox="0 0 150 150" aria-hidden="true">
            <rect x="44" y="20" width="62" height="86" rx="13" fill="rgba(255,255,255,.16)" stroke="rgba(255,255,255,.45)" stroke-width="2" transform="rotate(-16 75 63)"/>
            <rect x="44" y="20" width="62" height="86" rx="13" fill="#C8F542" transform="rotate(-4 75 63)"/>
            <rect x="44" y="20" width="62" height="86" rx="13" fill="#fff" transform="rotate(9 75 63)"/>
            <text x="83" y="78" font-family="Urbanist, sans-serif" font-weight="900" font-size="44" fill="#6A3DF0" text-anchor="middle" transform="rotate(9 75 63)">?</text>
          </svg>
          <p class="today-date">${icon("calendar")} ${esc(niceDate(key))}</p>
          <h1 id="today-title">Today's ten</h1>
          <p class="lede">Ten questions from ten different subjects. Everyone gets the same ones today, so you can compare scores.</p>
          ${done ? `<div class="done-note">${icon("check")} You scored ${done.score} out of ${ROUND} today. New questions tomorrow.</div>
                    <button class="piece quiet" data-go="share-daily">${icon("share")} Share today's score</button>`
                 : `<button class="piece primary" data-go="daily">Play today's ten</button>`}
        </section>

        <h2 class="section">More ways to play</h2>
        <div class="modes">
          <button class="piece mode quick" data-go="quick-setup"><span class="badge">${icon("bolt")}</span><span class="text">Quick round<small>Ten questions from the subjects you choose</small></span></button>
          <button class="piece mode lives" data-go="lives"><span class="badge">${icon("heart")}</span><span class="text">Three lives<small>Keep going until you've got three wrong. Best: ${store.get("best-lives", 0)}</small></span></button>
          <button class="piece mode hunchoff" data-go="hunchoff-setup"><span class="badge">${icon("family")}</span><span class="text">Hunch-off<small>Take turns on one phone</small></span></button>
          <button class="piece mode stats" data-go="stats"><span class="badge">${icon("chart")}</span><span class="text">Your stats<small>Best subjects, streaks and scores</small></span></button>
        </div>

        <h2 class="section">Pick a subject</h2>
        <div class="tiles">${tiles}</div>

        <h2 class="section" id="settings-title">Settings</h2>
        <section class="card settings" aria-labelledby="settings-title">
          <div class="setting">
            <span class="what" id="aud-label"><strong>Questions</strong><small>${audience === "easier" ? "Leaves out the hardest ones in quick rounds, three lives and Hunch-off." : "Everything, from easy to properly tricky."}</small></span>
            <div class="segmented" role="group" aria-labelledby="aud-label">
              <button aria-pressed="${audience === "everyone"}" data-audience="everyone">All</button>
              <button aria-pressed="${audience === "easier"}" data-audience="easier">Easier</button>
            </div>
          </div>
          <div class="setting">
            <span class="what" id="gu-label"><strong>Grown-up jokes</strong><small>${grownUps ? "On. Cheekier jokes are in the mix." : "Off. Every joke is fine for the whole family."}</small></span>
            <button class="switch" role="switch" aria-checked="${grownUps}" aria-labelledby="gu-label" data-grownups><span class="switch-track" aria-hidden="true"><span class="switch-thumb"></span></span></button>
          </div>
          <div class="setting">
            <span class="what" id="snd-label"><strong>Sound and buzz</strong><small>A little sound for each answer, and a buzz on phones that can.</small></span>
            <button class="switch" role="switch" aria-checked="${sound}" aria-labelledby="snd-label" data-sound><span class="switch-track" aria-hidden="true"><span class="switch-thumb"></span></span></button>
          </div>
          <div class="setting">
            <span class="what" id="theme-label"><strong>Look</strong><small>${theme === "light" ? "Light, for bright rooms and sunshine." : "Dark, easy on the eyes after tea."}</small></span>
            <div class="segmented" role="group" aria-labelledby="theme-label">
              <button aria-pressed="${theme === "dark"}" data-theme-pick="dark">Dark</button>
              <button aria-pressed="${theme === "light"}" data-theme-pick="light">Light</button>
            </div>
          </div>
        </section>

        ${siteFoot()}
      </div>`, false);
  }

  // The footer card: two tones split on the diagonal, like shazmoghaddam.github.io. The second layer is a visual
  // copy, hidden from screen readers and the keyboard, so the text can change colour where the tones meet.
  function siteFoot() {
    const inner = (hidden) => {
      const tab = hidden ? ` tabindex="-1"` : "";
      return `
        <ul class="ft-links">
          <li><a href="#" data-go="howto"${tab}>How to play, and how the answers are checked</a></li>
          <li><a href="#" data-go="stats"${tab}>Your stats</a></li>
        </ul>
        <p class="ft-count">${roundedCount()} questions in ${Object.keys(bank.categories).length} subjects, each with a source you can check. Works offline once it's loaded.</p>
        <div class="ft-rule" aria-hidden="true"></div>
        <div class="ft-sign">
          <p class="ft-copy"><span aria-hidden="true">&lt;&lt;&lt;</span><span class="ft-text">Made by <a href="https://shazmoghaddam.github.io/"${tab}>Shaz Moghaddam</a> · London</span><span aria-hidden="true">&gt;&gt;&gt;</span></p>
          <a class="ft-code" href="${REPO}"${tab}>Code on GitHub</a>
        </div>`;
    };
    return `
      <footer class="site-foot">
        <div class="ft-layer ft-layer--b">${inner(false)}</div>
        <div class="ft-layer ft-layer--a" aria-hidden="true">${inner(true)}</div>
      </footer>`;
  }

  function statsScreen() {
    const st = getStats();
    const pct = st.answered ? Math.round((st.right / st.answered) * 100) : 0;
    const subjects = Object.entries(st.cats)
      .filter(([cat, [n]]) => bank.categories[cat] && n >= 3)
      .map(([cat, [n, r]]) => ({ cat, n, r, p: Math.round((r / n) * 100) }))
      .sort((a, b) => b.p - a.p || b.n - a.n);
    const tile = (value, label) => `<div class="stat"><b>${value}</b><span>${label}</span></div>`;
    const bars = subjects.map((x) => `
      <li data-cat="${x.cat}"><span class="disc">${icon(x.cat)}</span><span class="name">${esc(bank.categories[x.cat])}</span>
        <span class="pct">${x.p}%</span><span class="track" role="img" aria-label="${x.r} right out of ${x.n}"><span class="fill" style="width:${x.p}%"></span></span></li>`).join("");
    render(`
      <div class="wrap">
        <header class="top">${logo}<div class="right"><button class="icon-btn" data-go="home" aria-label="Back to home">${icon("close")}</button></div></header>
        <section class="card panel">
          <h1>Your stats</h1>
          <p>Saved only in this browser.</p>
          <div class="stat-grid">
            ${tile(st.answered.toLocaleString("en-GB"), st.answered === 1 ? "question answered" : "questions answered")}
            ${tile(pct + "%", "right answers")}
            ${tile(st.games.toLocaleString("en-GB"), st.games === 1 ? "game finished" : "games finished")}
            ${tile(plural(longestStreak(), "day"), "longest daily streak")}
            ${tile(store.get("best-lives", 0), "best at three lives")}
            ${tile(st.perfect, st.perfect === 1 ? "perfect ten" : "perfect tens")}
          </div>
          <h2 class="section">Best subjects</h2>
          ${bars ? `<ul class="subject-bars">${bars}</ul>` : `<p class="empty">Answer a few questions in any subject and they'll show up here, best first.</p>`}
          <div class="actions two">
            <button class="piece quiet" data-go="home">Home</button>
            <button class="piece quiet" data-reset-stats>Reset my stats</button>
          </div>
        </section>
      </div>`);
  }

  function howto() {
    render(`
      <div class="wrap">
        <header class="top">${logo}<button class="icon-btn" data-go="home" aria-label="Back to home">${icon("close")}</button></header>
        <article class="card howto">
          <h1>How to play</h1>
          <p>Read the question, go with your hunch, and see if you're right. After every answer there's a short fact and a link to where it comes from.</p>
          <h2>Three kinds of question</h2>
          <div class="kinds">
            <div><span class="badge">${icon("up")}</span><p><strong>Higher or lower.</strong> You're told one number. Is the next one bigger or smaller, earlier or later?</p></div>
            <div><span class="badge">${icon("check")}</span><p><strong>Yes or no.</strong> Is it true? Some of them sound true and aren't.</p></div>
            <div><span class="badge">${icon("bolt")}</span><p><strong>Pick one.</strong> Choose from three or four answers.</p></div>
          </div>
          <h2>Ways to play</h2>
          <ul>
            <li><strong>Today's ten</strong> is the same for everyone each day. Play it every day to build a streak.</li>
            <li><strong>Quick round</strong> gives you ten questions from the subjects you choose.</li>
            <li><strong>Three lives</strong> keeps going until you get three wrong.</li>
            <li><strong>Hunch-off</strong> lets 2 to 6 people take turns on one phone or tablet. The highest score wins.</li>
          </ul>
          <p>In <strong>Settings</strong> on the home screen you can choose easier questions, switch sound and buzz on or off, and pick a dark or light look. <strong>Your stats</strong> shows your best subjects and longest streak.</p>
          <h2>Play anywhere</h2>
          <p>Once Hunchy has loaded, it works without an internet connection. On a phone, use your browser's <em>Add to Home Screen</em> to keep it with your apps.</p>
          <h2>Jokes</h2>
          <p>Every game ends with a joke, and Hunch-off has a joke break after each round of turns. Tap for the punchline, then share it if it made you laugh. Grown-up jokes are a bit cheekier, and only turn up if you switch them on in Settings.</p>
          <p>On a keyboard, press 1 to 4 to answer and Enter for the next question.</p>
          <h2>Can I trust the answers?</h2>
          <p>Every question has a source, shown after you answer. Maths answers are worked out by the game's own code. Country and science facts come from two separate datasets and are only used where both agree. Everything else was checked against a published source, and anything that can change, like a sports record, says when it was last checked.</p>
          <p>Spotted a mistake? Every answer has a <em>Report this question</em> link. Thank you.</p>
          <h2>Your data</h2>
          <p>Hunchy has no accounts, adverts or tracking. Your scores and streak are saved only in this browser.</p>
          <button class="piece primary" data-go="home">Back to the game</button>
        </article>
      </div>`);
  }

  // Quick round setup: choose subjects
  function quickSetup(preset) {
    const chosen = new Set(preset ? [preset] : []);
    const draw = (error = "") => {
      const picks = Object.entries(bank.categories).map(([cat, name]) =>
        `<button class="pick" data-cat="${cat}" data-toggle="${cat}" aria-pressed="${chosen.has(cat)}">${icon(cat)}${esc(name)}</button>`).join("");
      render(`
        <div class="wrap">
          <header class="top">${logo}<button class="icon-btn" data-go="home" aria-label="Back to home">${icon("close")}</button></header>
          <section class="card panel">
            <h1>Quick round</h1>
            <p>Choose one subject or several. Leave them all off for a mix of everything.</p>
            <div class="picks" role="group" aria-label="Subjects">${picks}</div>
            ${error ? `<p class="error" role="alert">${esc(error)}</p>` : ""}
            <div class="actions"><button class="piece primary" data-start>Start ten questions</button></div>
          </section>
        </div>`, !preset);
      app.querySelectorAll("[data-toggle]").forEach((b) => b.addEventListener("click", () => {
        const c = b.dataset.toggle; chosen.has(c) ? chosen.delete(c) : chosen.add(c);
        b.setAttribute("aria-pressed", chosen.has(c));
      }));
      app.querySelector("[data-start]").addEventListener("click", () => {
        const pool = bank.questions.filter((q) => (!chosen.size || chosen.has(q.category)) && allowed(q, audience));
        if (pool.length < 5) return draw("There aren't enough easier questions in that subject yet. Add another subject, or set Questions to All in Settings on the home screen.");
        start({ mode: "quick", questions: fresh(pool, ROUND), label: chosen.size === 1 ? bank.categories[[...chosen][0]] : "Quick round" });
      });
    };
    draw();
  }

  // Hunch-off setup: names and number of questions
  function hunchoffSetup(error = "") {
    const saved = store.get("players", ["", ""]);
    let names = saved.length >= 2 ? saved : ["", ""];
    let each = store.get("each", 5);
    const draw = (err = error) => {
      render(`
        <div class="wrap">
          <header class="top">${logo}<button class="icon-btn" data-go="home" aria-label="Back to home">${icon("close")}</button></header>
          <section class="card panel">
            <h1>Hunch-off</h1>
            <p>Take turns on one phone or tablet. Everyone gets their own questions, and the highest score wins.</p>
            <label class="label" for="p0">Who's playing?</label>
            <div class="players">
              ${names.map((n, i) => `
                <div class="player-row">
                  <input id="p${i}" value="${esc(n)}" maxlength="20" autocomplete="off" placeholder="Player ${i + 1}" aria-label="Player ${i + 1} name">
                  ${names.length > 2 ? `<button class="icon-btn" data-remove="${i}" aria-label="Remove player ${i + 1}">${icon("close")}</button>` : ""}
                </div>`).join("")}
            </div>
            ${names.length < 6 ? `<button class="piece quiet" data-add>${icon("plus")} Add a player</button>` : ""}
            <span class="label" id="each-label">Questions each</span>
            <div class="segmented" role="group" aria-labelledby="each-label">
              ${[3, 5, 8].map((n) => `<button data-each="${n}" aria-pressed="${each === n}">${n}</button>`).join("")}
            </div>
            <p class="hint">${audience === "easier" ? "Using easier questions. Change this in Settings on the home screen." : "Using all questions. Choose Easier in Settings on the home screen to leave out the hardest ones."}</p>
            ${err ? `<p class="error" role="alert">${esc(err)}</p>` : ""}
            <div class="actions"><button class="piece primary" data-start>Start the game</button></div>
          </section>
        </div>`);
      const read = () => { names = names.map((_, i) => app.querySelector("#p" + i).value.trim()); };
      app.querySelector("[data-add]")?.addEventListener("click", () => { read(); names.push(""); draw(""); app.querySelector("#p" + (names.length - 1)).focus(); });
      app.querySelectorAll("[data-remove]").forEach((b) => b.addEventListener("click", () => { read(); names.splice(+b.dataset.remove, 1); draw(""); }));
      app.querySelectorAll("[data-each]").forEach((b) => b.addEventListener("click", () => { read(); each = +b.dataset.each; draw(""); }));
      app.querySelector("[data-start]").addEventListener("click", () => {
        read();
        const players = names.map((n, i) => n || `Player ${i + 1}`);
        if (new Set(players.map((p) => p.toLowerCase())).size !== players.length) return draw("Two players have the same name. Give everyone a different one.");
        store.set("players", names); store.set("each", each);
        const pool = bank.questions.filter((q) => allowed(q, audience));
        const questions = fresh(pool, players.length * each);
        start({ mode: "hunchoff", questions, players: players.map((name) => ({ name, score: 0 })), each });
      });
    };
    draw();
  }

  // Playing ---------------------------------------------------------------------------------

  function start(options) {
    game = { index: 0, score: 0, lives: LIVES, results: [], answered: false, ...options };
    if (game.mode === "hunchoff") return passTo();
    ask();
  }

  function player() { return game.players[game.index % game.players.length]; }

  function passTo() {
    // After everyone has had a turn, there's a joke break before the next round.
    const breather = game.index > 0 && game.index % game.players.length === 0;
    render(`
      <div class="wrap">
        <header class="top">${logo}<button class="icon-btn" data-quit aria-label="Stop this game">${icon("close")}</button></header>
        <section class="card pass">
          <p>Question ${Math.floor(game.index / game.players.length) + 1} of ${game.each}. Pass the phone to</p>
          <h1>${esc(player().name)}</h1>
          <button class="piece primary" data-ready>I'm ready</button>
        </section>
        ${breather ? jokeCard("Joke break") : ""}
      </div>`);
    app.querySelector("[data-ready]").addEventListener("click", ask);
    app.querySelector("[data-ready]").focus();
  }

  function ask() {
    const q = game.questions[game.index];
    game.answered = false;
    // Pick-one answers are shuffled so the right one isn't always first. Yes/no and higher/lower keep their order.
    game.order = q.type === "choice" ? shuffle(q.options.map((_, i) => i)) : q.options.map((_, i) => i);
    const cat = bank.categories[q.category];

    let top;
    if (game.mode === "lives") {
      top = `<div class="lives" aria-label="${game.lives} lives left">${Array.from({ length: LIVES }, (_, i) => icon("heart", i < game.lives ? "" : "lost")).join("")}</div>
             <span class="score-pill" aria-label="Score ${game.score}">${game.score}</span>`;
    } else {
      const total = game.questions.length;
      const dots = Array.from({ length: total }, (_, i) => {
        const r = game.results[i];
        return `<span class="${r === true ? "right" : r === false ? "wrong" : i === game.index ? "now" : ""}"></span>`;
      }).join("");
      top = `<div class="progress" role="img" aria-label="Question ${game.index + 1} of ${total}">${dots}</div>`;
    }

    const answers = game.order.map((i, n) => {
      const text = q.options[i];
      let lead = `<span class="letter" aria-hidden="true">${"ABCD"[n]}</span>`;
      if (q.type === "yes-no") lead = icon(i === 0 ? "check" : "cross", "dir");
      if (q.type === "higher-lower") lead = icon(i === 0 ? "up" : "down", "dir");
      return `<button class="piece answer" data-answer="${i}" aria-keyshortcuts="${n + 1}">${lead}<span>${esc(text)}</span></button>`;
    }).join("");

    render(`
      <div class="wrap">
        <div class="bar">
          <button class="icon-btn" data-quit aria-label="Stop and go home">${icon("close")}</button>
          ${top}
          <button class="icon-btn" data-sound-quick aria-pressed="${sound}" aria-label="Sound and buzz">${icon(sound ? "sound" : "mute")}</button>
        </div>
        ${game.mode === "hunchoff" ? `<p class="turn-name">${esc(player().name)}'s question</p>` : ""}
        <article class="card question" data-cat="${q.category}">
          <div class="stripe">${icon(q.category)}<span>${esc(cat)}</span><span class="kind">${KIND[q.type]}</span></div>
          <div class="ask"><h1 id="q-text">${esc(q.prompt)}</h1></div>
        </article>
        <div class="answers ${q.type === "choice" ? (q.options.length === 4 ? "four" : "") : "pair"}" role="group" aria-labelledby="q-text">${answers}</div>
        <div id="reveal"></div>
      </div>`);
    app.querySelectorAll("[data-answer]").forEach((b) => b.addEventListener("click", () => choose(+b.dataset.answer, b)));
  }

  function choose(i, button) {
    if (game.answered) return;
    game.answered = true;
    const q = game.questions[game.index];
    const right = i === q.answer;
    markSeen(q.id);
    recordAnswer(q, right);
    play(right ? "right" : "wrong");
    if (game.mode !== "lives") game.results[game.index] = right;
    if (right) { game.score++; if (game.mode === "hunchoff") player().score++; }
    else if (game.mode === "lives") game.lives--;

    app.querySelectorAll("[data-answer]").forEach((b) => {
      const n = +b.dataset.answer;
      b.disabled = true;
      if (n === q.answer) { b.classList.add("is-right"); b.insertAdjacentHTML("beforeend", icon("check", "mark")); }
      else if (n === i) { b.classList.add("is-wrong"); b.insertAdjacentHTML("beforeend", icon("cross", "mark")); }
      else b.classList.add("faded");
    });
    button.classList.add("pressed");
    setTimeout(() => button.classList.remove("pressed"), 120);

    const over = game.mode === "lives" ? game.lives === 0 : game.index + 1 >= game.questions.length;
    const nextLabel = over ? "See how you did" : game.mode === "hunchoff" ? `Next: ${esc(game.players[(game.index + 1) % game.players.length].name)}` : "Next question";
    const asOf = q.asOf ? `<span>True as of ${esc(asOfText(q.asOf))}</span>` : "";
    const report = `${REPO}/issues/new?${new URLSearchParams({ title: `Question check: ${q.id}`, labels: "question-check", body: `Question: ${q.prompt}\nAnswer given: ${q.options[q.answer]}\n\nWhat looks wrong, and where did you see the right answer?\n` })}`;
    document.getElementById("reveal").innerHTML = `
      <section class="reveal ${right ? "good" : "bad"}" aria-labelledby="verdict">
        <h2 id="verdict">${icon(right ? "check" : "cross")}${right ? pickOne(["Right!", "Spot on!", "Good hunch!", "Nailed it!"]) : pickOne(["Not quite.", "So close.", "Not this time."])}</h2>
        ${right ? "" : `<p class="answer-line">The answer is: ${esc(q.options[q.answer])}</p>`}
        <p class="fact">${esc(q.fact)}</p>
        <div class="meta">
          <a href="${esc(q.source.url)}" target="_blank" rel="noopener">${icon("link")}Source: ${esc(q.source.name)}</a>
          ${asOf}
          <a href="${esc(report)}" target="_blank" rel="noopener">${icon("flag")}Report this question</a>
        </div>
        <button class="piece primary" data-next>${nextLabel}</button>
      </section>`;
    say(`${right ? "Right." : "Not quite. The answer is " + q.options[q.answer] + "."} ${q.fact}`);
    const next = app.querySelector("[data-next]");
    next.addEventListener("click", () => advance(over));
    next.focus({ preventScroll: true });
    document.getElementById("reveal").scrollIntoView({ behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "nearest" });
  }

  function asOfText(v) {
    if (/^\d{4}$/.test(v)) return v;
    const [y, m] = v.split("-");
    return new Date(+y, +m - 1, 1).toLocaleDateString("en-GB", { month: "long", year: "numeric" });
  }

  function advance(over) {
    game.index++;
    if (over) return finish();
    if (game.mode === "lives" && game.index >= game.questions.length) {
      game.questions = game.questions.concat(fresh(bank.questions.filter((q) => allowed(q, audience)), 20));
    }
    if (game.mode === "hunchoff") return passTo();
    ask();
  }

  function finish() {
    const key = todayKey();
    play("done");
    if (game.mode !== "lives") recordGame(game.mode !== "hunchoff" && game.score === game.questions.length && game.questions.length === ROUND);
    else recordGame(false);
    let extra = "";
    if (game.mode === "daily") {
      const daily = store.get("daily", {});
      daily[key] = { score: game.score, results: game.results };
      const keep = Object.keys(daily).sort().slice(-60);
      store.set("daily", Object.fromEntries(keep.map((k) => [k, daily[k]])));
      const days = new Set(store.get("days", [])); days.add(key); store.set("days", [...days].sort().slice(-400));
    }
    if (game.mode === "lives") {
      const best = store.get("best-lives", 0);
      if (game.score > best) { store.set("best-lives", game.score); extra = "That's your best yet."; }
      else if (best > 0) extra = `Your best is ${best}.`;
    }

    if (game.mode === "hunchoff") {
      const ranked = game.players.slice().sort((a, b) => b.score - a.score);
      const top = ranked[0].score;
      const winners = ranked.filter((p) => p.score === top);
      const plain = winners.length > 1 ? `It's a draw between ${winners.map((w) => w.name).join(" and ")}!` : `${winners[0].name} wins!`;
      const title = esc(plain);
      const each = game.each;
      shareResult = () => share(`Hunch-off on Hunchy: ${plain} ${ranked.map((p) => `${p.name} ${p.score}`).join(", ")}, out of ${each} each. Fancy a go? ${SITE}`);
      render(`
        <div class="wrap">
          <header class="top">${logo}</header>
          <section class="card result">
            <p class="verdict">${title}</p>
            <ol class="board">
              ${ranked.map((p, i) => `<li class="${p.score === top ? "first" : ""}"><span class="place">${i + 1}</span>${esc(p.name)}<span class="pts">${p.score} of ${game.each}</span></li>`).join("")}
            </ol>
            <div class="actions"><button class="piece primary" data-again>Play again</button></div>
            <div class="actions two"><button class="piece quiet" data-go="home">Home</button><button class="piece quiet" data-share-result>${icon("share")} Share</button></div>
          </section>
          ${jokeCard("One for the road")}
        </div>`);
      app.querySelector("[data-again]").addEventListener("click", () => hunchoffSetup());
      say(plain);
      return;
    }

    const total = game.mode === "lives" ? null : game.questions.length;
    const ratio = total ? game.score / total : 0;
    const verdict = total ? (ratio === 1 ? "A perfect ten. Incredible." : ratio >= .8 ? "Brilliant hunches." : ratio >= .6 ? "Great work." : ratio >= .4 ? "Not bad at all." : "Tricky one. Try again tomorrow?")
                          : game.score >= 15 ? "What a run." : game.score >= 8 ? "Good going." : "Have another go.";
    const chips = total ? `<div class="chips" aria-hidden="true">${game.questions.map((q, i) => `<span class="${game.results[i] ? "right" : "wrong"}">${icon(q.category)}</span>`).join("")}</div>` : "";
    render(`
      <div class="wrap">
        <header class="top">${logo}${game.mode === "daily" ? streakChip() : ""}</header>
        <section class="card result">
          <p>${game.mode === "daily" ? esc(niceDate(key)) : game.mode === "lives" ? "Three lives" : esc(game.label)}</p>
          <p class="big">${game.score}${total ? `<small> / ${total}</small>` : ""}</p>
          <p class="verdict">${verdict}</p>
          ${extra ? `<p>${extra}</p>` : ""}
          ${chips}
          <div class="actions">
            ${game.mode === "daily" ? `<button class="piece primary" data-go="share-daily">${icon("share")} Share your score</button>` : `<button class="piece primary" data-again>Play again</button>`}
          </div>
          <div class="actions two">
            <button class="piece quiet" data-go="home">Home</button>
            ${game.mode === "daily" ? `<button class="piece quiet" data-go="quick-setup">Quick round</button>` : `<button class="piece quiet" data-share-result>${icon("share")} Share</button>`}
          </div>
        </section>
        ${jokeCard(game.score === total ? "A joke, for a perfect round" : "And now, a joke")}
      </div>`);
    say(`You scored ${game.score}${total ? " out of " + total : ""}. ${verdict}`);
    const mode = game.mode, label = game.label, score = game.score;
    shareResult = mode === "lives"
      ? () => share(`I got ${plural(score, "answer")} right on Hunchy before losing all three lives. Can you beat it? ${SITE}`)
      : () => share(`I scored ${score}/${total} in a Hunchy quick round${label === "Quick round" ? "" : ` (${label})`}. Can you beat it? ${SITE}`);
    app.querySelector("[data-again]")?.addEventListener("click", () => {
      if (mode === "lives") return startLives();
      const pool = bank.questions.filter((q) => allowed(q, audience) && (label === "Quick round" || bank.categories[q.category] === label));
      start({ mode: "quick", questions: fresh(pool, ROUND), label });
    });
  }

  function startLives() {
    start({ mode: "lives", questions: fresh(bank.questions.filter((q) => allowed(q, audience)), 30) });
  }

  // Sharing. Phones get their own share sheet (WhatsApp, Messages and so on); everywhere else the text is copied.
  // Share text only ever says how someone did, never which answers were right, so it can't spoil today's ten.
  let shareResult = null;

  async function share(text, copied = "Copied. Paste it into your family chat.") {
    try {
      if (navigator.share) { await navigator.share({ text }); return; }
      await navigator.clipboard.writeText(text);
      toast(copied);
    } catch (err) {
      if (err && err.name === "AbortError") return; // they closed the share sheet
      toast("Couldn't share from this browser. Try copying the page address instead.");
    }
  }

  function shareDaily() {
    const key = todayKey();
    const done = store.get("daily", {})[key];
    if (!done) return;
    const row = done.results.map((r) => (r ? "+" : "-")).join("");
    const s = currentStreak();
    share(`Hunchy, ${niceDate(key)}: ${done.score}/${ROUND} [${row}]${s > 1 ? `, ${s} day streak` : ""}. Play today's ten: ${SITE}`,
      "Score copied. Paste it into your family chat.");
  }

  // Jokes ------------------------------------------------------------------------------------

  // A joke nobody on this browser has seen yet, at random. Once every joke has been shown, the pile is reshuffled.
  function drawJoke() {
    const pool = jokes.filter((j) => grownUps || !j.grownUp);
    if (!pool.length) return null;
    let seen = store.get("jokes-seen", []);
    let unseen = pool.filter((j) => !seen.includes(j.id));
    if (!unseen.length) {
      // Every joke has been seen: start a fresh pile, but don't hand back the one that was just on screen.
      seen = [];
      unseen = pool.length > 1 && shownJoke ? pool.filter((j) => j.id !== shownJoke.id) : pool;
    }
    const joke = pickOne(unseen);
    seen.push(joke.id);
    store.set("jokes-seen", seen.slice(-jokes.length));
    return joke;
  }

  function jokeCard(heading) {
    const joke = drawJoke();
    shownJoke = joke;
    if (!joke) return "";
    return `
      <section class="card joke" aria-labelledby="joke-title">
        <h2 id="joke-title">${icon("smile")}${esc(heading)}${joke.grownUp ? `<span class="tag">Grown-up</span>` : ""}</h2>
        <p class="setup">${esc(joke.setup)}</p>
        <button class="piece quiet punch" data-punch aria-expanded="false" aria-controls="punchline">Tap for the punchline</button>
        <div id="punchline" hidden>
          <p class="punchline">${esc(joke.punchline)}</p>
          <div class="joke-actions">
            <button class="link-btn" data-joke-share>${icon("share")}Share this joke</button>
            <button class="link-btn" data-joke-next>Another one</button>
          </div>
        </div>
      </section>`;
  }

  function revealPunchline(button) {
    const box = document.getElementById("punchline");
    if (!box) return;
    box.hidden = false;
    button.setAttribute("aria-expanded", "true");
    button.remove();
    say(shownJoke ? shownJoke.punchline : "");
    box.querySelector("[data-joke-share]")?.focus({ preventScroll: true });
  }

  function nextJoke() {
    const card = app.querySelector(".joke");
    if (!card) return;
    card.outerHTML = jokeCard("Another one");
    app.querySelector(".joke [data-punch]")?.focus({ preventScroll: true });
  }

  function toast(text) {
    document.querySelector(".toast")?.remove();
    const t = document.createElement("div");
    t.className = "toast"; t.setAttribute("role", "status"); t.textContent = text;
    document.body.appendChild(t);
    setTimeout(() => t.remove(), 3200);
  }

  // Wiring -----------------------------------------------------------------------------------

  app.addEventListener("click", (e) => {
    const go = e.target.closest("[data-go]");
    const aud = e.target.closest("[data-audience]");
    const quit = e.target.closest("[data-quit]");
    if (aud) { audience = aud.dataset.audience; store.set("audience", audience); home(); app.querySelector(`[data-audience="${audience}"]`)?.focus({ preventScroll: true }); return; }
    if (e.target.closest("[data-grownups]")) {
      grownUps = !grownUps; store.set("grown-ups", grownUps); home();
      app.querySelector("[data-grownups]")?.focus({ preventScroll: true });
      return;
    }
    const punch = e.target.closest("[data-punch]");
    if (punch) return revealPunchline(punch);
    if (e.target.closest("[data-joke-share]") && shownJoke) {
      return share(`${shownJoke.setup}\n${shownJoke.punchline}\n\nFrom Hunchy, a free family quiz: ${SITE}`, "Joke copied. Go and make someone groan.");
    }
    if (e.target.closest("[data-joke-next]")) return nextJoke();
    if (e.target.closest("[data-sound]")) {
      sound = !sound; store.set("sound", sound); home();
      app.querySelector("[data-sound]")?.focus({ preventScroll: true });
      if (sound) play("right");
      return;
    }
    const soundQuick = e.target.closest("[data-sound-quick]");
    if (soundQuick) {
      sound = !sound; store.set("sound", sound);
      soundQuick.setAttribute("aria-pressed", sound);
      soundQuick.innerHTML = icon(sound ? "sound" : "mute");
      toast(sound ? "Sound and buzz on." : "Sound and buzz off.");
      return;
    }
    const pickTheme = e.target.closest("[data-theme-pick]");
    if (pickTheme) {
      theme = pickTheme.dataset.themePick; store.set("theme", theme); applyTheme(); home();
      app.querySelector(`[data-theme-pick="${theme}"]`)?.focus({ preventScroll: true });
      return;
    }
    if (e.target.closest("[data-reset-stats]")) {
      if (Date.now() - resetArmed < 3000) {
        store.set("stats", emptyStats()); store.set("days", []); store.set("best-lives", 0);
        toast("Stats cleared."); statsScreen();
      } else { resetArmed = Date.now(); toast("Tap Reset again to clear your stats and streak."); }
      return;
    }
    if (e.target.closest("[data-share-result]") && shareResult) return shareResult();
    if (quit) { if (!game || game.index === 0 || confirmQuit()) home(); return; }
    if (!go) return;
    e.preventDefault();
    const where = go.dataset.go;
    if (where === "home") home();
    else if (where === "howto") howto();
    else if (where === "daily") start({ mode: "daily", questions: dailyTen(todayKey()) });
    else if (where === "quick-setup") quickSetup();
    else if (where === "quick") quickSetup(go.dataset.pick);
    else if (where === "lives") startLives();
    else if (where === "hunchoff-setup") hunchoffSetup();
    else if (where === "share-daily") shareDaily();
    else if (where === "stats") statsScreen();
  });

  // A gentle check, without the browser's blocking pop-up: tapping the cross twice within three seconds quits.
  let quitArmed = 0;
  let resetArmed = 0;
  function confirmQuit() {
    if (Date.now() - quitArmed < 3000) return true;
    quitArmed = Date.now();
    toast("Tap the cross again to stop. This round won't be saved.");
    return false;
  }

  document.addEventListener("keydown", (e) => {
    if (!game || e.metaKey || e.ctrlKey || e.altKey || /input|textarea/i.test(e.target.tagName)) return;
    if (!game.answered && /^[1-4]$/.test(e.key)) {
      const b = app.querySelectorAll("[data-answer]")[+e.key - 1];
      if (b) { e.preventDefault(); b.click(); }
    }
  });

  async function boot() {
    // "younger" was the old name for easier questions, so anyone who chose it keeps their setting.
    audience = ["easier", "younger"].includes(store.get("audience", "everyone")) ? "easier" : "everyone";
    grownUps = store.get("grown-ups", false) === true;
    sound = store.get("sound", true) !== false;
    theme = store.get("theme", "dark") === "light" ? "light" : "dark";
    applyTheme();
    // Offline play: the service worker keeps a copy of the game and its questions. Only on https or localhost.
    if ("serviceWorker" in navigator && (location.protocol === "https:" || location.hostname === "localhost")) {
      // When a new version takes over, reload onto it straight away, so nobody plays the old one. On a first visit
      // there was no old version, so there's nothing to reload. Mid-game, the reload waits until the round is over.
      const hadOldVersion = !!navigator.serviceWorker.controller;
      navigator.serviceWorker.addEventListener("controllerchange", () => {
        if (!hadOldVersion || reloading) return;
        if (game) { updateWaiting = true; return; }
        reloading = true; location.reload();
      });
      navigator.serviceWorker.register("sw.js").then((reg) => {
        // Phones often keep Hunchy open in the background for days, so look for a new version whenever it comes back.
        document.addEventListener("visibilitychange", () => { if (document.visibilityState === "visible") reg.update().catch(() => {}); });
      }).catch(() => { /* still playable online */ });
    }
    const loadJokes = fetch("data/jokes.json", { cache: "no-cache" })
      .then((r) => (r.ok ? r.json() : { jokes: [] })).then((d) => { jokes = Array.isArray(d.jokes) ? d.jokes : []; })
      .catch(() => { jokes = []; });
    try {
      const res = await fetch("data/questions.json", { cache: "no-cache" });
      if (!res.ok) throw new Error(res.status);
      bank = await res.json();
      await loadJokes;
      home();
    } catch {
      render(`<div class="wrap"><div class="card panel"><h1>The questions didn't load</h1><p>Check your internet connection, then reload the page. After the first visit, Hunchy works offline too.</p><button class="piece primary" onclick="location.reload()">Reload</button></div></div>`);
    }
  }
  boot();
})();
