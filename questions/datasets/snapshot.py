"""Rebuild the small dataset snapshots the generated questions are made from.

Run from the repository root (needs internet):

    python questions/datasets/snapshot.py

Every fact used for a generated question comes from two independent open datasets, and the snapshot keeps both
values side by side so the tests can check they agree:

    countries.csv   mledoze/countries (ODbL) and samayo/country-json (MIT) for capital, area and continent, plus the
                    World Bank's population figures (CC BY 4.0) via datasets/population
    elements.csv    Bowserinator/Periodic-Table-JSON (CC BY-SA 3.0) and the periodictable Python package (public domain)
    planets.csv     NASA's Planetary Fact Sheet, via devstronomy/nasa-data-scraper
"""

import csv
import io
import json
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = "https://raw.githubusercontent.com/"


def get(path: str) -> bytes:
    with urllib.request.urlopen(RAW + path, timeout=60) as resp:
        return resp.read()


# Countries most families will have heard of. Questions only use these, so nobody is asked about a tiny territory.
COUNTRIES = [
    "Argentina", "Australia", "Austria", "Belgium", "Brazil", "Canada", "Chile", "China", "Colombia", "Croatia",
    "Cuba", "Denmark", "Egypt", "Ethiopia", "Finland", "France", "Germany", "Ghana", "Greece", "Iceland", "India",
    "Indonesia", "Ireland", "Italy", "Jamaica", "Japan", "Kenya", "Mexico", "Morocco", "Nepal", "Netherlands",
    "New Zealand", "Nigeria", "Norway", "Pakistan", "Peru", "Philippines", "Poland", "Portugal", "Saudi Arabia",
    "South Africa", "South Korea", "Spain", "Sweden", "Switzerland", "Thailand", "Turkey", "Ukraine",
    "United Kingdom", "United States", "Vietnam", "Russia", "Mongolia", "Bolivia", "Paraguay", "Hungary",
    "Czechia", "Uganda", "Zambia", "Kazakhstan",
    "Algeria", "Angola", "Armenia", "Azerbaijan", "Bangladesh", "Bulgaria", "Cambodia", "Cameroon", "Costa Rica",
    "Cyprus", "Ecuador", "Estonia", "Fiji", "Georgia", "Guatemala", "Iran", "Iraq", "Jordan", "Kuwait", "Laos",
    "Latvia", "Lebanon", "Lithuania", "Luxembourg", "Madagascar", "Malaysia", "Mali", "Malta", "Mozambique",
    "Namibia", "Oman", "Panama", "Qatar", "Romania", "Rwanda", "Senegal", "Serbia", "Singapore", "Slovakia",
    "Slovenia", "Tunisia", "United Arab Emirates", "Uruguay", "Uzbekistan", "Venezuela", "Zimbabwe", "Bhutan",
    "Botswana", "Malawi", "Albania", "North Macedonia", "Montenegro", "Bosnia and Herzegovina", "Moldova",
    "Belarus", "Honduras", "Venezuela", "Sudan", "Libya", "Kyrgyzstan", "Tajikistan", "Turkmenistan",
    "Papua New Guinea", "Samoa", "Tonga", "Barbados", "Trinidad and Tobago", "Bahamas", "Dominican Republic",
    "Haiti", "Nicaragua", "El Salvador", "Liechtenstein", "Andorra", "Monaco", "San Marino",
]
COUNTRIES = list(dict.fromkeys(COUNTRIES))
# samayo/country-json uses some older or longer names
SAMAYO_NAMES = {"Czechia": "Czech Republic", "Russia": "Russian Federation", "South Korea": "South Korea",
                "Vietnam": "Vietnam", "Turkey": "Turkey"}
WORLD_BANK_CODES = {}  # filled from mledoze's cca3 codes


def countries() -> None:
    mledoze = {c["name"]["common"]: c for c in json.loads(get("mledoze/countries/master/countries.json"))}
    samayo = {}
    for key, field in [("capital-city", "city"), ("surface-area", "area"), ("continent", "continent"),
                       ("population", "population")]:
        for row in json.loads(get(f"samayo/country-json/master/src/country-by-{key}.json")):
            samayo.setdefault(row["country"], {})[field] = row[field]
    pop = list(csv.DictReader(io.StringIO(get("datasets/population/main/data/population.csv").decode())))
    latest = {}
    for row in pop:
        if row["Year"] >= latest.get(row["Country Code"], ("0", 0))[0]:
            latest[row["Country Code"]] = (row["Year"], int(float(row["Value"])))
    rows = []
    for name in COUNTRIES:
        m = mledoze[name if name != "Turkey" else "Türkiye"] if (name in mledoze or name == "Turkey") else None
        if m is None:
            raise SystemExit(f"{name} missing from mledoze/countries")
        s = samayo.get(SAMAYO_NAMES.get(name, name), {})
        year, population = latest.get(m["cca3"], ("", ""))
        rows.append({
            "country": name, "code": m["cca3"],
            "capital_a": (m.get("capital") or [""])[0], "capital_b": s.get("city") or "",
            "area_a": m.get("area", ""), "area_b": s.get("area") or "",
            "region_a": m.get("region", ""), "subregion_a": m.get("subregion", ""), "continent_b": s.get("continent") or "",
            "landlocked": m.get("landlocked"),
            "population_wb": population, "population_year": year, "population_b": s.get("population") or "",
        })
    with open(HERE / "countries.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def elements() -> None:
    import periodictable  # pip install periodictable

    bowser = json.loads(get("Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json"))["elements"]
    rows = []
    for e in bowser[:86]:  # up to radon: the elements people have a chance of knowing
        p = periodictable.elements[e["number"]]
        rows.append({"number": e["number"], "name_a": e["name"], "symbol_a": e["symbol"], "phase": e["phase"],
                     "category": e["category"], "name_b": p.name.capitalize(), "symbol_b": p.symbol})
    with open(HERE / "elements.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def planets() -> None:
    (HERE / "planets.csv").write_bytes(get("devstronomy/nasa-data-scraper/master/data/csv/planets.csv"))


if __name__ == "__main__":
    countries()
    elements()
    planets()
    print("Saved countries.csv, elements.csv and planets.csv")
