// Tests for how Hunchy chooses questions. Run with: node --test tests/picker.test.js
// The picking code is read straight out of assets/app.js (between the "A small seeded" and "Stats: kept" comments),
// so these tests always check the code that ships.
const test = require("node:test");
const assert = require("node:assert");
const fs = require("node:fs");
const path = require("node:path");

const root = path.join(__dirname, "..");
const src = fs.readFileSync(path.join(root, "assets/app.js"), "utf8");
const start = src.indexOf("  // A small seeded"), end = src.indexOf("  // Stats: kept");
assert.ok(start > 0 && end > start, "couldn't find the question-picking code in assets/app.js");
const bank = JSON.parse(fs.readFileSync(path.join(root, "data/questions.json"), "utf8"));

function picker() {
  const mem = {};
  const store = { get: (k, f) => (k in mem ? JSON.parse(mem[k]) : f), set: (k, v) => { mem[k] = JSON.stringify(v); } };
  const make = new Function("bank", "store", "ROUND", `${src.slice(start, end)}\nreturn { dailyTen, fresh, markSeen, allowed };`);
  return { ...make(bank, store, 10), store };
}

const dayKey = (n) => new Date(Date.UTC(2026, 10, 13 + n)).toISOString().slice(0, 10);

test("today's ten has ten different subjects and is the same every time", () => {
  const a = picker(), b = picker();
  for (let d = 0; d < 30; d++) {
    const ten = a.dailyTen(dayKey(d));
    assert.strictEqual(ten.length, 10);
    assert.strictEqual(new Set(ten.map((q) => q.category)).size, 10);
    assert.deepStrictEqual(ten.map((q) => q.id), b.dailyTen(dayKey(d)).map((q) => q.id));
  }
});

test("today's ten doesn't repeat a question for at least three months", () => {
  const { dailyTen } = picker();
  const ids = [];
  for (let d = 0; d < 100; d++) ids.push(...dailyTen(dayKey(d)).map((q) => q.id));
  assert.strictEqual(new Set(ids).size, ids.length);
});

test("every daily ten has a quick kind, a classic and a modern question", () => {
  const { dailyTen } = picker();
  for (let d = 0; d < 100; d++) {
    const ten = dailyTen(dayKey(d));
    assert.ok(ten.some((q) => q.type !== "choice"), `day ${d}: no yes/no or higher/lower`);
    assert.ok(ten.some((q) => q.era === "classic"), `day ${d}: nothing classic`);
    assert.ok(ten.some((q) => q.era === "modern"), `day ${d}: nothing modern`);
  }
});

test("playing a small subject to the end doesn't bring back questions from other subjects", () => {
  const { fresh, markSeen } = picker();
  const play = (pool, n) => fresh(pool, n).map((q) => (markSeen(q.id), q.id));
  const all = bank.questions;
  const first = play(all, 300);
  const smallest = Object.keys(bank.categories).sort((a, b) =>
    all.filter((q) => q.category === a).length - all.filter((q) => q.category === b).length)[0];
  for (let i = 0; i < 8; i++) play(all.filter((q) => q.category === smallest), 10);
  const next = play(all, 300);
  assert.ok(!next.some((id) => first.includes(id)), "a mixed round brought back a question answered earlier");
});

test("no question repeats until the pool is used up, then the oldest come back first", () => {
  const { fresh, markSeen } = picker();
  const pool = bank.questions.filter((q) => q.category === "cars");
  const order = [];
  while (order.length < pool.length) fresh(pool, 10).forEach((q) => { if (order.length < pool.length) { markSeen(q.id); order.push(q.id); } });
  assert.strictEqual(new Set(order).size, pool.length);
  const back = fresh(pool, 10).map((q) => q.id);
  const oldest = new Set(order.slice(0, 20));
  assert.ok(back.every((id) => oldest.has(id)), "returning questions should be ones answered longest ago");
});

test("a mixed round of ten never uses the same subject twice", () => {
  const { fresh, markSeen } = picker();
  for (let r = 0; r < 50; r++) {
    const round = fresh(bank.questions, 10);
    assert.strictEqual(new Set(round.map((q) => q.category)).size, 10);
    round.forEach((q) => markSeen(q.id));
  }
});
