"""Put every question together into data/questions.json, the file the game loads.

Run from the repository root:

    python questions/build.py

It refuses to write the file if any question breaks the rules in check(), so a mistake never reaches players.
"""

from __future__ import annotations

import importlib
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from questions.generated import all_generated  # noqa: E402

OUT = ROOT / "data" / "questions.json"
CURATED = ["history", "people", "places", "science", "sport", "screen", "culture",
           "sport2", "vehicles", "brands", "art2", "fashion_food_cartoons", "world2", "words",
           "sport3", "music3", "landmarks3", "world3", "people3", "science3", "history3",
           "screen4", "music4", "art4", "extras4"]

CATEGORIES = {
    "geography": "Geography", "landmarks": "Cities & Landmarks", "history": "History",
    "people": "Leaders & Famous People", "science": "Science", "space": "Space", "nature": "Nature & Animals",
    "maths": "Maths", "sport": "Sport", "film-tv": "Film & TV", "music": "Music", "art": "Art & Culture",
    "food": "Food & Drink", "inventions": "Inventions & Brands",
    "cars": "Cars & Motorbikes", "fashion": "Fashion", "cartoons": "Cartoons & Animation",
    "words": "Words & Language",
}
TYPES = {"yes-no", "higher-lower", "choice"}
ERAS = {"timeless", "classic", "modern"}


def curated() -> list[dict]:
    out = []
    for name in CURATED:
        module = importlib.import_module(f"questions.curated.{name}")
        for value in vars(module).values():
            if hasattr(value, "questions") and hasattr(value, "key"):
                out.extend(value.questions)
    return out


def check(questions: list[dict]) -> list[str]:
    problems = []
    ids = Counter(q["id"] for q in questions)
    problems += [f"{i}: id used {n} times" for i, n in ids.items() if n > 1]
    prompts = Counter(q["prompt"] for q in questions)
    problems += [f"asked twice: {p}" for p, n in prompts.items() if n > 1]
    for q in questions:
        where = q["id"]
        if q["category"] not in CATEGORIES:
            problems.append(f"{where}: unknown category {q['category']}")
        if q["type"] not in TYPES:
            problems.append(f"{where}: unknown type {q['type']}")
        if q["era"] not in ERAS or q["difficulty"] not in (1, 2, 3):
            problems.append(f"{where}: era or difficulty is wrong")
        opts = q["options"]
        if len(opts) != len(set(opts)) or not 2 <= len(opts) <= 4 or not 0 <= q["answer"] < len(opts):
            problems.append(f"{where}: options or answer are wrong")
        if q["type"] == "choice" and len(opts) < 3:
            problems.append(f"{where}: a choice question needs at least three options")
        if not q["fact"].strip() or not q["source"]["url"].startswith("https://"):
            problems.append(f"{where}: needs a fact and a source")
        text = " ".join([q["prompt"], q["fact"], *opts])
        if "—" in text:
            problems.append(f"{where}: contains an em dash")
        if not q["prompt"].rstrip().endswith(("?", ".")):
            problems.append(f"{where}: prompt should end with a question mark or full stop")
    return problems


def main() -> None:
    questions = all_generated() + curated()
    problems = check(questions)
    if problems:
        print("Not saved. Fix these first:\n  " + "\n  ".join(problems))
        sys.exit(1)
    data = {
        "version": 1,
        "categories": CATEGORIES,
        "count": len(questions),
        "questions": questions,
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    counts = Counter(q["category"] for q in questions)
    print(f"Saved {len(questions)} questions to {OUT.relative_to(ROOT)}")
    for key, label in CATEGORIES.items():
        print(f"  {label:<26}{counts[key]:>4}")
    print("  " + ", ".join(f"{k}: {v}" for k, v in sorted(Counter(q['type'] for q in questions).items())))
    print("  " + ", ".join(f"{k}: {v}" for k, v in sorted(Counter(q['era'] for q in questions).items())))
    print("  " + ", ".join(f"difficulty {k}: {v}" for k, v in sorted(Counter(q['difficulty'] for q in questions).items())))


if __name__ == "__main__":
    main()
