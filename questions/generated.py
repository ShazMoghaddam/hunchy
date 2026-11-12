"""Questions worked out from data, so the answer can't be mistyped.

    Maths       calculated here, and recalculated by the tests
    Geography   capital, area and continent from two country datasets, kept only where both agree; population
                from the World Bank, kept only where an older second dataset gives the same order
    Science     element names and symbols from two periodic tables, kept only where both agree
    Space       planet sizes, distances and day lengths from NASA's Planetary Fact Sheet

Everything is seeded, so running this twice gives the same questions in the same order.
"""

from __future__ import annotations

import csv
import random
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "datasets"

SOURCES = {
    "countries": ("REST Countries data (mledoze/countries) and samayo/country-json", "https://github.com/mledoze/countries"),
    "population": ("World Bank, population total", "https://data.worldbank.org/indicator/SP.POP.TOTL"),
    "elements": ("Royal Society of Chemistry periodic table", "https://www.rsc.org/periodic-table"),
    "planets": ("NASA Planetary Fact Sheet", "https://nssdc.gsfc.nasa.gov/planetary/factsheet/"),
    "maths": ("Worked out by Hunchy's own code", "https://github.com/ShazMoghaddam/hunchy/blob/main/questions/generated.py"),
}

# Capitals both datasets agree on once local spellings are allowed for (samayo uses the local name).
LOCAL_NAMES = {"Wien": "Vienna", "Bruxelles [Brussel]": "Brussels", "Santiago de Chile": "Santiago", "Peking": "Beijing",
               "Bogota": "Bogotá", "La Habana": "Havana", "Addis Abeba": "Addis Ababa", "Helsinki [Helsingfors]": "Helsinki",
               "Athenai": "Athens", "Reykjavík": "Reykjavik", "Roma": "Rome", "Ciudad de M": "Mexico City",
               "Warszawa": "Warsaw", "Lisboa": "Lisbon", "Washington": "Washington D.C.", "Praha": "Prague",
               "Alger": "Algiers", "Yaounde": "Yaoundé", "Masqat": "Muscat", "Bucuresti": "Bucharest",
               "Toskent": "Tashkent", "Chisinau": "Chișinău", "Port-of-Spain": "Port of Spain",
               "Santo Domingo de Guzm": "Santo Domingo"}
# Spellings used in English today, where a dataset keeps an older one
DISPLAY = {"Ulan Bator": "Ulaanbaatar"}
# Countries that span two continents, or whose capital is shared between cities, are left out of those questions.
NOT_ONE_CONTINENT = {"Russia", "Turkey", "Egypt", "Kazakhstan"}
NOT_ONE_CAPITAL = {"Bolivia", "South Africa", "Netherlands", "Sudan"}
# Where the capital shares the country's name the question answers itself, so those are left out too.
SAME_NAME = {"Luxembourg", "Monaco", "San Marino", "Kuwait", "Panama", "Guatemala", "Singapore", "Andorra",
             "Mexico", "Djibouti", "Tunisia", "Algeria"}
# Countries whose only 'coast' is on the Caspian, which some count as a sea: too disputed for a yes or no.
CASPIAN = {"Azerbaijan", "Kazakhstan", "Turkmenistan"}

# How well known a country is, for setting difficulty: 1 = almost everyone has heard of it.
KNOWN = {"Austria", "Belgium", "Chile", "Colombia", "Croatia", "Cuba", "Denmark", "Finland", "Iceland", "Jamaica",
         "Kenya", "Morocco", "Nepal", "Norway", "Peru", "Poland", "South Korea", "Sweden", "Switzerland", "Thailand",
         "Turkey", "Ukraine", "Vietnam", "Nigeria", "Philippines", "Indonesia", "Pakistan", "Iran", "Iraq", "Malta",
         "Cyprus", "Hungary", "Czechia", "Romania", "Bulgaria", "Serbia", "Qatar", "United Arab Emirates", "Jordan",
         "Lebanon", "Malaysia", "Uruguay", "Venezuela", "Ecuador", "Bangladesh", "Ghana", "Ethiopia", "Zimbabwe"}
EASY = {"Australia", "Brazil", "Canada", "China", "France", "Germany", "India", "Italy", "Japan", "Mexico", "Spain",
        "United Kingdom", "United States", "Egypt", "Ireland", "Russia", "Greece", "Portugal", "Argentina", "New Zealand"}


def q(qid, category, kind, prompt, options, answer, fact, source, era="timeless", difficulty=2, as_of=None):
    name, url = SOURCES[source]
    out = {"id": qid, "category": category, "type": kind, "prompt": prompt, "options": options, "answer": answer,
           "fact": fact, "era": era, "difficulty": difficulty, "source": {"name": name, "url": url}}
    if as_of:
        out["asOf"] = as_of
    return out


THE = {"Philippines", "United Kingdom", "United States", "Netherlands"}


def name(country: str, start: bool = False) -> str:
    """Country names as people say them: 'the Netherlands', or 'The Netherlands' at the start of a sentence."""
    if country in THE:
        return ("The " if start else "the ") + country
    return country


def millions(n: float) -> str:
    if n >= 1e9:
        return f"{n / 1e9:.2f} billion"
    return f"{n / 1e6:.1f} million" if n < 1e8 else f"{n / 1e6:,.0f} million"


def km2(n: float) -> str:
    return f"{n / 1e6:.2f} million km²" if n >= 1e6 else f"{n:,.0f} km²"


def read(name: str) -> list[dict]:
    with open(DATA / name, encoding="utf-8") as f:
        return list(csv.DictReader(f))


# Geography -------------------------------------------------------------------------------------------

def geography(rng: random.Random) -> list[dict]:
    rows = read("countries.csv")
    out = []

    capitals = [r for r in rows if r["country"] not in NOT_ONE_CAPITAL | SAME_NAME and r["capital_b"]
                and LOCAL_NAMES.get(r["capital_b"], r["capital_b"]) == r["capital_a"]]
    capitals = [{**r, "capital_a": DISPLAY.get(r["capital_a"], r["capital_a"])} for r in capitals]
    order = rng.sample(capitals, len(capitals))
    picks, reverse = order[:30], order[30:55]
    for i, r in enumerate(picks, 1):
        others = [c["capital_a"] for c in capitals if c["region_a"] == r["region_a"] and c["country"] != r["country"]]
        wrong = rng.sample(others, 3)
        # Famous cities that aren't the capital make the best wrong answers
        options = [r["capital_a"]] + wrong
        out.append(q(f"geo-capital-{i:02d}", "geography", "choice", f"What is the capital city of {name(r['country'])}?",
                     options, 0, f"{r['capital_a']} is the capital of {name(r['country'])}, which is home to about "
                     f"{millions(int(r['population_wb']))} people.", "countries",
                     difficulty=1 if r["country"] in EASY else 2 if r["country"] in KNOWN else 3))

    for i, r in enumerate(reverse, 1):
        others = [c for c in capitals if c["region_a"] == r["region_a"] and c["country"] != r["country"]]
        wrong = [name(c["country"], True) for c in rng.sample(others, 3)]
        out.append(q(f"geo-capital-of-{i:02d}", "geography", "choice", f"{r['capital_a']} is the capital city of which country?",
                     [name(r["country"], True)] + wrong, 0,
                     f"{r['capital_a']} is the capital of {name(r['country'])}, which is home to about "
                     f"{millions(int(r['population_wb']))} people.", "countries",
                     difficulty=1 if r["country"] in EASY else 2 if r["country"] in KNOWN else 3))

    areas = [r for r in rows if r["area_b"] and abs(float(r["area_a"]) / float(r["area_b"]) - 1) < 0.02]
    pairs = []
    while len(pairs) < 15:
        a, b = rng.sample(areas, 2)
        ra, rb = float(a["area_a"]), float(b["area_a"])
        if max(ra, rb) / min(ra, rb) < 1.25 or {a["country"], b["country"]} in [set(p) for p in pairs]:
            continue  # too close to call, or already asked
        pairs.append((a["country"], b["country"]))
        bigger = rb > ra
        out.append(q(f"geo-area-{len(pairs):02d}", "geography", "higher-lower",
                     f"{name(a['country'], True)} covers {km2(ra)}. Is {name(b['country'])} bigger or smaller?", ["Bigger", "Smaller"],
                     0 if bigger else 1, f"{name(b['country'], True)} covers {km2(rb)}, about {rb / ra:.1f} times the size of {name(a['country'])}."
                     if bigger else f"{name(b['country'], True)} covers {km2(rb)}. {name(a['country'], True)} is about {ra / rb:.1f} times bigger.",
                     "countries", difficulty=2))

    pops = [r for r in rows if r["population_b"]]
    pairs = []
    while len(pairs) < 15:
        a, b = rng.sample(pops, 2)
        pa, pb = int(a["population_wb"]), int(b["population_wb"])
        qa, qb = float(a["population_b"]), float(b["population_b"])
        if max(pa, pb) / min(pa, pb) < 1.5 or (pa > pb) != (qa > qb) or {a["country"], b["country"]} in [set(p) for p in pairs]:
            continue  # too close, or the two sources disagree on which is bigger
        pairs.append((a["country"], b["country"]))
        more = pb > pa
        year = a["population_year"]
        out.append(q(f"geo-people-{len(pairs):02d}", "geography", "higher-lower",
                     f"About {millions(pa)} people live in {name(a['country'])}. Does {name(b['country'])} have more people or fewer?",
                     ["More", "Fewer"], 0 if more else 1,
                     f"{name(b['country'], True)} has about {millions(pb)} people ({year} estimate).", "population",
                     era="modern", difficulty=2, as_of=year))

    continents = {"Europe": "Europe", "Asia": "Asia", "Africa": "Africa", "Oceania": "Oceania"}
    places = [r for r in rows if r["country"] not in NOT_ONE_CONTINENT and r["continent_b"]]
    answers = []
    for r in places:
        if r["region_a"] == "Americas":
            if r["continent_b"] in ("North America", "South America") and r["subregion_a"] in ("South America", "North America", "Central America", "Caribbean"):
                place = "South America" if r["subregion_a"] == "South America" else "North America"
                if place == r["continent_b"]:
                    answers.append((r, place))
        elif continents.get(r["region_a"]) == r["continent_b"]:
            answers.append((r, r["continent_b"]))
    all_names = ["Africa", "Asia", "Europe", "North America", "South America", "Oceania"]
    for i, (r, place) in enumerate(rng.sample(answers, 10), 1):
        wrong = rng.sample([n for n in all_names if n != place], 3)
        out.append(q(f"geo-continent-{i:02d}", "geography", "choice", f"Which continent is {name(r['country'])} in?",
                     [place] + wrong, 0, f"{name(r['country'], True)} is in {r['subregion_a'] or place}.", "countries", difficulty=1))

    landlocked = [r for r in rows if r["landlocked"] == "True" and r["country"] not in CASPIAN]
    coastal = [r for r in rows if r["country"] in {"Portugal", "Chile", "Vietnam", "Norway", "Croatia", "Peru", "Kenya",
                                                    "Poland", "Bulgaria", "Romania", "Slovenia", "Montenegro"}]
    for i, r in enumerate(rng.sample(landlocked, 5) + rng.sample(coastal, 5), 1):
        locked = r["landlocked"] == "True"
        out.append(q(f"geo-landlocked-{i:02d}", "geography", "yes-no", f"Is {name(r['country'])} landlocked, with no coastline on the sea?",
                     ["Yes", "No"], 0 if locked else 1,
                     f"{name(r['country'], True)} has no coast at all, so everything it trades by sea goes through its neighbours."
                     if locked else f"{name(r['country'], True)} has a coastline on the sea.", "countries", difficulty=2))
    return out


# Science: elements -------------------------------------------------------------------------------------

def science(rng: random.Random) -> list[dict]:
    rows = [r for r in read("elements.csv") if r["symbol_a"] == r["symbol_b"]
            and r["name_a"].lower() == r["name_b"].lower().replace("aluminum", "aluminium")]
    # Symbols that don't obviously match the English name make the best questions
    tricky = ["Fe", "Au", "Ag", "Na", "K", "Pb", "Cu", "Sn", "Hg", "W"]
    common = ["O", "H", "C", "N", "He", "Ca", "Cl", "Si", "Ne", "Mg", "Zn", "S"]
    by_symbol = {r["symbol_a"]: r for r in rows}
    out = []
    for i, sym in enumerate(rng.sample(tricky, 6) + rng.sample(common, 4), 1):
        r = by_symbol[sym]
        decoys = rng.sample([x["name_a"] for x in rows if x["symbol_a"] != sym and x["symbol_a"] in tricky + common], 3)
        hard = sym in tricky
        out.append(q(f"sci-symbol-{i:02d}", "science", "choice", f"Which element has the chemical symbol {sym}?",
                     [r["name_a"]] + decoys, 0, f"{r['name_a']} is element number {r['number']} in the periodic table."
                     + (" Its symbol comes from its Latin name." if sym in {"Fe", "Au", "Ag", "Na", "K", "Pb", "Cu", "Sn", "Hg"} else ""),
                     "elements", difficulty=3 if hard else 2))
    named = [by_symbol[s] for s in ["H", "He", "C", "N", "O", "Na", "Fe", "Cu", "Ag", "Au", "Ca", "Ne", "Zn", "Pb"]]
    pairs = []
    while len(pairs) < 5:
        a, b = rng.sample(named, 2)
        if {a["symbol_a"], b["symbol_a"]} in [set(p) for p in pairs]:
            continue
        pairs.append((a["symbol_a"], b["symbol_a"]))
        higher = int(b["number"]) > int(a["number"])
        out.append(q(f"sci-number-{len(pairs):02d}", "science", "higher-lower",
                     f"{a['name_a']} is element number {a['number']} in the periodic table. Is {b['name_a']}'s number higher or lower?",
                     ["Higher", "Lower"], 0 if higher else 1,
                     f"{b['name_a']} is element number {b['number']}. The number is how many protons each atom has.",
                     "elements", difficulty=3))
    for i, (sym, gas) in enumerate([("Ne", True), ("Fe", False), ("N", True), ("Hg", False)], 1):
        r = by_symbol[sym]
        assert (r["phase"] == "Gas") == gas, sym
        out.append(q(f"sci-gas-{i:02d}", "science", "yes-no", f"Is {r['name_a'].lower()} a gas at room temperature?",
                     ["Yes", "No"], 0 if gas else 1,
                     {"Ne": "Neon is a gas. It glows bright orange-red in the signs named after it.",
                      "Fe": "Iron is a solid metal, and it only melts at about 1,538 °C.",
                      "N": "Nitrogen is a gas, and it makes up about 78% of the air we breathe.",
                      "Hg": "Mercury is a liquid at room temperature: the only metal that is."}[sym],
                     "elements", difficulty=2))
    return out


# Space: planets -------------------------------------------------------------------------------------

def space(rng: random.Random) -> list[dict]:
    planets = [r for r in read("planets.csv") if r["planet"] != "Pluto"]
    by = {r["planet"]: r for r in planets}
    out = []
    pairs = [("Earth", "Venus"), ("Mars", "Mercury"), ("Neptune", "Uranus"), ("Saturn", "Jupiter"), ("Earth", "Mars")]
    for i, (a, b) in enumerate(pairs, 1):
        da, db = float(by[a]["diameter"]), float(by[b]["diameter"])
        out.append(q(f"space-size-{i:02d}", "space", "higher-lower", f"{a} is {da:,.0f} km across. Is {b} bigger or smaller?",
                     ["Bigger", "Smaller"], 0 if db > da else 1, f"{b} is {db:,.0f} km across.", "planets", difficulty=2))
    order = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    dist = {p: float(by[p]["distance_from_sun"]) for p in order}
    assert sorted(order, key=dist.get) == order
    for i, (a, b) in enumerate([("Mars", "Jupiter"), ("Saturn", "Uranus"), ("Venus", "Mercury")], 1):
        out.append(q(f"space-distance-{i:02d}", "space", "higher-lower",
                     f"{a} is about {dist[a]:,.0f} million km from the Sun. Is {b} closer to the Sun or further away?",
                     ["Further", "Closer"], 0 if dist[b] > dist[a] else 1,
                     f"{b} is about {dist[b]:,.0f} million km from the Sun, on average.", "planets", difficulty=2))
    day = {p: float(by[p]["length_of_day"]) for p in order}
    out.append(q("space-day-01", "space", "choice", "Which planet has the shortest day?",
                 [min(order, key=day.get), "Earth", "Mercury", "Mars"], 0,
                 f"A day on {min(order, key=day.get)} lasts about {min(day.values()):.0f} hours: it spins faster than any other planet.",
                 "planets", difficulty=2))
    year = {p: float(by[p]["orbital_period"]) for p in order}
    out.append(q("space-year-01", "space", "higher-lower", f"A year on Earth lasts {year['Earth']:.0f} days. Is a year on Mars longer or shorter?",
                 ["Longer", "Shorter"], 0, f"Mars takes about {year['Mars']:.0f} Earth days to go round the Sun.", "planets", difficulty=2))
    temp = {p: float(by[p]["mean_temperature"]) for p in order}
    hottest = max(order, key=temp.get)
    out.append(q("space-hot-01", "space", "choice", "Which planet is the hottest?", [hottest, "Mercury", "Mars", "Jupiter"], 0,
                 f"{hottest} averages about {temp[hottest]:.0f} °C. Its thick clouds trap heat, so it is even hotter than Mercury, "
                 "which is closer to the Sun.", "planets", difficulty=2))
    return out


# Maths ----------------------------------------------------------------------------------------------

def maths(rng: random.Random) -> list[dict]:
    out = []
    n = 0

    def add(kind, prompt, options, answer, fact, difficulty, era="timeless"):
        nonlocal n
        n += 1
        out.append(q(f"maths-{n:02d}", "maths", kind, prompt, options, answer, fact, "maths", era=era, difficulty=difficulty))

    def choice(correct, spread):
        """Three wrong answers near the right one, all different and positive."""
        wrong = set()
        while len(wrong) < 3:
            w = correct + rng.choice(spread)
            if w != correct and w > 0:  # callers make sure there are always three positive choices
                wrong.add(w)
        return [correct] + sorted(wrong)

    for a, b in [(7, 8), (9, 6), (12, 12), (6, 7), (8, 9)]:
        opts = choice(a * b, [-a, a, -b, b, -1, 1, 10])
        add("choice", f"What is {a} × {b}?", [fmt(o) for o in opts], 0, f"{a} × {b} = {a * b}.", 1)
    for a, b in [(144, 12), (81, 9), (56, 7)]:
        opts = choice(a // b, [-2, -1, 1, 2, 3])
        add("choice", f"What is {a} ÷ {b}?", [fmt(o) for o in opts], 0, f"{a} ÷ {b} = {a // b}, because {b} × {a // b} = {a}.", 1)
    for pct, of in [(10, 250), (25, 80), (50, 64), (20, 150), (75, 40)]:
        v = Fraction(pct, 100) * of
        assert v.denominator == 1
        opts = choice(int(v), [-10, -5, 5, 10, 2])
        add("choice", f"What is {pct}% of {of}?", [fmt(o) for o in opts], 0, f"{pct}% of {of} is {int(v)}.", 2)
    for a, b in [((1, 2), (2, 5)), ((3, 4), (2, 3)), ((5, 8), (3, 5)), ((1, 3), (3, 10))]:
        fa, fb = Fraction(*a), Fraction(*b)
        add("higher-lower", f"Is {b[0]}/{b[1]} bigger or smaller than {a[0]}/{a[1]}?", ["Bigger", "Smaller"], 0 if fb > fa else 1,
            f"{b[0]}/{b[1]} = {float(fb):.3g} and {a[0]}/{a[1]} = {float(fa):.3g}.", 2)
    shapes = {"hexagon": 6, "octagon": 8, "pentagon": 5, "triangle": 3, "decagon": 10}
    for shape, sides in shapes.items():
        opts = choice(sides, [-2, -1, 1, 2])
        art = "an" if shape[0] in "aeiou" else "a"
        add("choice", f"How many sides does {art} {shape} have?", [fmt(o) for o in opts], 0,
            f"{art.capitalize()} {shape} has {sides} sides." + (" A stop sign is an octagon." if shape == "octagon" else ""), 1)
    for num in [17, 21, 29, 51, 91, 97]:
        prime = num > 1 and all(num % d for d in range(2, int(num ** 0.5) + 1))
        factors = next((f"{d} × {num // d}" for d in range(2, num) if num % d == 0), "")
        add("yes-no", f"Is {num} a prime number?", ["Yes", "No"], 0 if prime else 1,
            f"{num} is prime: only 1 and {num} divide into it." if prime else f"{num} is not prime: {num} = {factors}.", 2)
    for value, numeral in [(2026, "MMXXVI"), (1999, "MCMXCIX"), (14, "XIV"), (90, "XC")]:
        roman = to_roman(value)
        assert roman == numeral, (value, roman)
        opts = choice(value, [-10, -4, 4, 10, 100, -1])
        add("choice", f"Which number is {numeral} in Roman numerals?", [str(o) for o in opts], 0, f"{numeral} = {value}.", 3, era="classic")
    add("choice", "How many seconds are there in one hour?", ["3,600", "360", "6,000", "1,440"], 0, "60 seconds × 60 minutes = 3,600 seconds.", 1)
    add("choice", "How many minutes are there in a day?", ["1,440", "2,400", "1,200", "3,600"], 0, "24 hours × 60 minutes = 1,440 minutes.", 2)
    add("higher-lower", "A dozen is 12. Is a baker's dozen more or less?", ["More", "Less"], 0,
        "A baker's dozen is 13. Bakers once added an extra loaf so they couldn't be accused of selling short.", 1, era="classic")
    add("choice", "What is the next number in the pattern 1, 1, 2, 3, 5, 8, ...?", ["13", "11", "12", "16"], 0,
        "Each number is the two before it added together: 5 + 8 = 13. It's called the Fibonacci sequence.", 2)
    add("choice", "What is 2 to the power of 10?", [fmt(2 ** 10), "100", "512", "2,048"], 0, "2 multiplied by itself 10 times is 1,024.", 3)
    add("yes-no", "Is the square root of 144 equal to 12?", ["Yes", "No"], 0, "12 × 12 = 144.", 1)
    add("choice", "How many degrees are there in a right angle?", ["90", "45", "180", "100"], 0, "A right angle is 90°, a quarter of a full turn.", 1)
    add("choice", "The angles in a triangle always add up to how many degrees?", ["180", "360", "90", "270"], 0,
        "The three angles of any triangle add up to 180°.", 2)
    for side in [7, 9, 12]:
        opts = choice(side * side, [-side, side, -1, 1, 2 * side])
        add("choice", f"What is {side} squared ({side} × {side})?", [fmt(o) for o in opts], 0, f"{side} × {side} = {side * side}.", 2)
    for w, h in [(5, 3), (8, 4)]:
        per = 2 * (w + h)
        opts = choice(per, [-4, -2, 2, w * h - per if w * h != per else 6])
        add("choice", f"A rectangle is {w} cm long and {h} cm wide. What is its perimeter?", [f"{o} cm" for o in opts], 0,
            f"The perimeter is all the way round: {w} + {h} + {w} + {h} = {per} cm. Its area would be {w * h} cm².", 2)
    signed = lambda n: f"−{abs(n)}" if n < 0 else str(n)  # noqa: E731 - a proper minus sign
    for a, b in [(-3, 5), (-10, 4)]:
        right = a + b
        opts = [right] + [w for w in (right - 2, right + 2, -right, right + 1) if w != right][:3]
        assert len(set(opts)) == 4
        add("choice", f"What is {signed(a)} + {b}?", [signed(o) for o in opts], 0,
            f"Start at {signed(a)} on a number line and count {b} steps up: you land on {signed(right)}.", 2)
    for value, nearest in [(347, 10), (2650, 100), (7499, 1000)]:
        r = int(Fraction(value, nearest) + Fraction(1, 2)) * nearest
        opts = choice(r, [-nearest, nearest, 2 * nearest])
        add("choice", f"What is {fmt(value)} rounded to the nearest {fmt(nearest)}?", [fmt(o) for o in opts], 0,
            f"{fmt(value)} is closer to {fmt(r)} than to any other multiple of {fmt(nearest)}.", 2)
    nums = [4, 8, 6, 10]
    mean = Fraction(sum(nums), len(nums))
    assert mean.denominator == 1
    add("choice", f"What is the average (mean) of {', '.join(map(str, nums[:-1]))} and {nums[-1]}?", [str(int(mean)), "6", "8", "28"] if int(mean) not in (6, 8, 28) else [str(int(mean)), "5", "9", "28"], 0,
        f"Add them up ({sum(nums)}) and divide by how many there are ({len(nums)}): {int(mean)}.", 2)
    add("higher-lower", "Is 0.5 bigger or smaller than 0.45?", ["Bigger", "Smaller"], 0 if Fraction(1, 2) > Fraction(45, 100) else 1,
        "0.5 is the same as 0.50, which is bigger than 0.45.", 2)
    add("higher-lower", "Is 3/4 of an hour more or less than 40 minutes?", ["More", "Less"], 0 if Fraction(3, 4) * 60 > 40 else 1,
        f"Three quarters of an hour is {int(Fraction(3, 4) * 60)} minutes.", 1)
    add("yes-no", "Is 1,000 grams the same as 1 kilogram?", ["Yes", "No"], 0, "Kilo means a thousand, so a kilogram is 1,000 grams.", 1)
    add("yes-no", "Is every square also a rectangle?", ["Yes", "No"], 0,
        "A rectangle is any four-sided shape with four right angles. A square is just a rectangle with all sides equal.", 2)
    add("choice", "How many days are there in a leap year?", ["366", "365", "364", "360"], 0,
        "A leap year adds 29 February. They come every four years, with a few exceptions for century years.", 1)
    add("higher-lower", f"Are there more or fewer than 8,000 hours in a year?", ["More", "Fewer"],
        0 if 365 * 24 > 8000 else 1, f"365 days × 24 hours = {365 * 24:,} hours.", 3)
    add("choice", "What is half of a quarter?", ["An eighth", "A third", "A sixth", "A half"], 0, "Half of 1/4 is 1/8.", 2)
    add("choice", "How many faces does a cube have?", ["6", "4", "8", "12"], 0, "A cube has 6 faces, 12 edges and 8 corners.", 1)
    add("yes-no", "Is zero an even number?", ["Yes", "No"], 0, "Zero divides by 2 with nothing left over, so it's even.", 2)
    assert len(out) == 60, len(out)
    return out


def fmt(n: int) -> str:
    """Numbers as people write them: 1,024 rather than 1024."""
    return f"{n:,}"


def to_roman(value: int) -> str:
    parts = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
             (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
    out = ""
    for n, s in parts:
        while value >= n:
            out += s
            value -= n
    return out


def all_generated() -> list[dict]:
    rng = random.Random(2026)
    return geography(rng) + science(rng) + space(rng) + maths(rng)


if __name__ == "__main__":
    qs = all_generated()
    from collections import Counter
    print(len(qs), Counter(x["category"] for x in qs))
