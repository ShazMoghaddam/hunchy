# Dataset snapshots

Small extracts of open datasets, used by `questions/generated.py` to make the country, element and planet questions.
Each file keeps the values from two sources side by side, so the tests can check they agree. Rebuild them with
`python questions/datasets/snapshot.py`.

These files keep the licences of the data they come from, not this repo's MIT licence:

| File | Source | Licence |
|---|---|---|
| `countries.csv` | [mledoze/countries](https://github.com/mledoze/countries) (columns ending `_a`, `landlocked`, `code`) | [ODbL 1.0](https://opendatacommons.org/licenses/odbl/1-0/) |
| | [samayo/country-json](https://github.com/samayo/country-json) (columns ending `_b`) | MIT |
| | [World Bank](https://data.worldbank.org/indicator/SP.POP.TOTL) via [datasets/population](https://github.com/datasets/population) (`population_wb`, `population_year`) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) |
| `elements.csv` | [Bowserinator/Periodic-Table-JSON](https://github.com/Bowserinator/Periodic-Table-JSON) (columns ending `_a`, `phase`, `category`) | [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) |
| | [periodictable](https://pypi.org/project/periodictable/) Python package (columns ending `_b`) | Public domain |
| `planets.csv` | NASA Planetary Fact Sheet, via [devstronomy/nasa-data-scraper](https://github.com/devstronomy/nasa-data-scraper) | Public domain (NASA) |
