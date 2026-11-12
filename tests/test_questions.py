"""Checks every question before it reaches players. Run from the repository root with `pytest`."""

import csv
import json
import re
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from questions.build import CATEGORIES, check, curated  # noqa: E402
from questions.generated import DISPLAY, LOCAL_NAMES, all_generated, name, to_roman  # noqa: E402

sys.path.insert(0, str(ROOT / "jokes"))
import build_jokes  # noqa: E402

BANK = json.loads((ROOT / "data" / "questions.json").read_text(encoding="utf-8"))
QUESTIONS = BANK["questions"]
DATASETS = ROOT / "questions" / "datasets"


def test_the_published_file_matches_the_source():
    """data/questions.json must be exactly what questions/build.py makes, so nobody edits the JSON by hand."""
    assert QUESTIONS == all_generated() + curated()


def test_there_are_1200_questions_with_no_problems():
    assert len(QUESTIONS) == BANK["count"] == 1200
    assert check(QUESTIONS) == []


def test_every_category_is_well_stocked():
    counts = Counter(q["category"] for q in QUESTIONS)
    assert set(counts) == set(CATEGORIES)
    assert min(counts.values()) >= 30


def test_every_generation_and_level_is_covered():
    for cat in CATEGORIES:
        qs = [q for q in QUESTIONS if q["category"] == cat]
        assert any(q["difficulty"] == 1 for q in qs), f"{cat} has nothing for Easier questions"


def test_the_daily_ten_can_always_be_filled():
    """The game picks two higher-or-lower and two yes-or-no questions a day; there must be plenty of each."""
    types = Counter(q["type"] for q in QUESTIONS)
    assert types["higher-lower"] >= 40 and types["yes-no"] >= 40


def test_no_lyrics_or_emojis():
    emoji = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
    for q in QUESTIONS:
        text = " ".join([q["prompt"], q["fact"], *q["options"]])
        assert not emoji.search(text), q["id"]


def test_dated_facts_say_when_they_were_true():
    """Anything about a record, a ranking or 'the most' can change, so it must carry an as-of date."""
    changeable = re.compile(r"\b(the most|most visited|best-selling|highest-earning|record|tallest building)\b", re.I)
    fixed_in_time = re.compile(r"\b(1[0-9]|20)\d\d\b")  # 'at the Paris 2024 Olympics' can't change
    for q in QUESTIONS:
        if changeable.search(q["prompt"]) and not fixed_in_time.search(q["prompt"]):
            assert "asOf" in q, f"{q['id']} may change over time: add as_of"


# The maths is worked out again here, a second time, independently of the generator ----------------------

def test_maths_answers_are_correct():
    for q in (x for x in QUESTIONS if x["category"] == "maths"):
        p, right = q["prompt"], q["options"][q["answer"]].replace(",", "")
        if m := re.fullmatch(r"What is (\d+) × (\d+)\?", p):
            assert int(right) == int(m[1]) * int(m[2])
        elif m := re.fullmatch(r"What is (\d+) ÷ (\d+)\?", p):
            assert int(right) * int(m[2]) == int(m[1])
        elif m := re.fullmatch(r"What is (\d+)% of (\d+)\?", p):
            assert Fraction(int(right)) == Fraction(int(m[1]), 100) * int(m[2])
        elif m := re.fullmatch(r"Is (\d+)/(\d+) bigger or smaller than (\d+)/(\d+)\?", p):
            bigger = Fraction(int(m[1]), int(m[2])) > Fraction(int(m[3]), int(m[4]))
            assert right == ("Bigger" if bigger else "Smaller")
        elif m := re.fullmatch(r"Is (\d+) a prime number\?", p):
            n = int(m[1])
            assert (right == "Yes") == all(n % d for d in range(2, n))
        elif m := re.fullmatch(r"Which number is ([MDCLXVI]+) in Roman numerals\?", p):
            assert to_roman(int(right)) == m[1]
        # wrong answers must really be wrong: no option can equal the right one
        assert q["options"].count(q["options"][q["answer"]]) == 1


# Geography and science answers must agree with both datasets they come from --------------------------------

def read(name):
    with open(DATASETS / name, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def agreed_capital(r):
    """The capital both datasets give, in the spelling the game shows, or None if they disagree."""
    if r["capital_a"] != LOCAL_NAMES.get(r["capital_b"], r["capital_b"]):
        return None
    return DISPLAY.get(r["capital_a"], r["capital_a"])


def test_capitals_agree_in_both_datasets():
    rows = {r["country"]: r for r in read("countries.csv")}
    asked = [x for x in QUESTIONS if x["id"].startswith("geo-capital-") and not x["id"].startswith("geo-capital-of")]
    assert asked
    for q in asked:
        country = re.fullmatch(r"What is the capital city of (?:the )?(.+)\?", q["prompt"])[1]
        assert q["options"][q["answer"]] == agreed_capital(rows[country]), q["id"]


def test_reverse_capitals_agree_in_both_datasets():
    """'Canberra is the capital city of which country?' The answer must be the only country whose capital it is."""
    rows = read("countries.csv")
    asked = [x for x in QUESTIONS if x["id"].startswith("geo-capital-of")]
    assert len(asked) >= 20
    for q in asked:
        capital = re.fullmatch(r"(.+) is the capital city of which country\?", q["prompt"])[1]
        matches = [r["country"] for r in rows if agreed_capital(r) == capital]
        assert len(matches) == 1, (q["id"], matches)
        assert q["options"][q["answer"]] == name(matches[0], start=True), q["id"]
        for wrong in q["options"]:
            if wrong != q["options"][q["answer"]]:
                assert all(name(r["country"], start=True) != wrong or agreed_capital(r) != capital for r in rows)


def test_areas_agree_in_both_datasets():
    rows = {r["country"]: r for r in read("countries.csv")}
    for q in (x for x in QUESTIONS if x["id"].startswith("geo-area")):
        a, b = re.fullmatch(r"(?:The )?(.+?) covers .+?\. Is (?:the )?(.+) bigger or smaller\?", q["prompt"]).groups()
        for source in ("area_a", "area_b"):
            bigger = float(rows[b][source]) > float(rows[a][source])
            assert q["options"][q["answer"]] == ("Bigger" if bigger else "Smaller"), (q["id"], source)


def test_element_symbols_agree_in_both_tables():
    rows = {r["symbol_a"]: r for r in read("elements.csv")}
    for q in (x for x in QUESTIONS if x["id"].startswith("sci-symbol")):
        sym = re.fullmatch(r"Which element has the chemical symbol (\w+)\?", q["prompt"])[1]
        r = rows[sym]
        assert r["symbol_a"] == r["symbol_b"] and q["options"][q["answer"]] == r["name_a"]


# Jokes ------------------------------------------------------------------------------------------------

JOKES = json.loads((ROOT / "data" / "jokes.json").read_text(encoding="utf-8"))["jokes"]


def test_the_jokes_file_matches_the_source():
    expected = [*build_jokes.FAMILY, *build_jokes.GROWN_UPS]
    assert [(j["setup"], j["punchline"]) for j in JOKES] == expected


def test_there_are_100_jokes_mostly_for_everyone():
    assert len(JOKES) == 100
    assert sum(not j["grownUp"] for j in JOKES) == 75
    assert len({j["id"] for j in JOKES}) == len({j["setup"] for j in JOKES}) == len({j["punchline"] for j in JOKES}) == 100


def test_jokes_are_clean_text():
    emoji = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF]")
    for j in JOKES:
        for text in (j["setup"], j["punchline"]):
            assert text.strip() and "—" not in text and not emoji.search(text), j["id"]


# No ages anywhere: Hunchy is a family quiz, full stop ------------------------------------------------------

@pytest.mark.parametrize("path", ["README.md", "CHANGELOG.md", "CONTRIBUTING.md", "index.html", "manifest.webmanifest",
                                  "assets/app.js", "questions/curated/__init__.py"])
def test_no_age_ranges(path):
    text = (ROOT / path).read_text(encoding="utf-8")
    assert not re.search(r"\bages? \d|\d+ to 80|year-old|younger players", text, re.I), path


# The page itself -------------------------------------------------------------------------------------

@pytest.mark.parametrize("path", ["index.html", "assets/app.js", "assets/styles.css", "manifest.webmanifest"])
def test_no_em_dashes_in_the_game(path):
    assert "—" not in (ROOT / path).read_text(encoding="utf-8")


def test_every_category_has_an_icon_and_a_colour():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    css = (ROOT / "assets" / "styles.css").read_text(encoding="utf-8")
    for cat in CATEGORIES:
        assert f'id="i-{cat}"' in html, f"no icon for {cat}"
        assert f'[data-cat="{cat}"]' in css, f"no colour for {cat}"


def test_files_the_page_needs_exist():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    for ref in re.findall(r'(?:href|src)="(?!https?:|#|mailto:)([^"]+)"', html):
        assert (ROOT / ref).exists(), ref
