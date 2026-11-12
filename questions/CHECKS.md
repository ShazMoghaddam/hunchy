# How the questions were checked

Every question was checked twice before launch: once when it was written, and again against a source. This page
records the second round, including what it changed.

## Checked by code

- **Maths (60 questions).** Answers are calculated by `questions/generated.py`, then calculated again a different way
  by `tests/test_questions.py`.
- **Countries (105 questions).** Capitals (asked both ways round), areas, continents and coastlines are only used where two independent datasets agree
  ([REST Countries](https://github.com/mledoze/countries) and [country-json](https://github.com/samayo/country-json)).
  Population questions use the World Bank's latest figures, and only pairs where an older second dataset gives the
  same answer. Countries with two capitals, or that span two continents, are left out.
- **Elements (19 questions).** Names and symbols are only used where two periodic tables agree.
- **Planets (11 questions).** Sizes, distances and day lengths come from NASA's Planetary Fact Sheet.

## Checked against published sources

Each hand-written question links to a page that states its answer. On top of that, facts that were recent, numeric
or easy to get wrong were checked against a second source:

| Checked | Source | Result |
|---|---|---|
| Spain won the 2026 World Cup | [ABC News](https://abcnews.com/culture/story/spain-argentina-win-2026-world-cup-134824556) | Confirmed: 1-0 after extra time against Argentina, 19 July 2026 |
| Lando Norris won the 2025 F1 title | [Formula 1](https://www.formula1.com/en/latest/article/abu-dhabi-lowdown-all-the-key-moments-as-norris-seals-his-debut-title-and.6WLoFRGsfe4fbq1TZeoVIa) | Confirmed |
| Arsenal won the 2025 to 2026 Premier League; Manchester United's 13 titles is still the record | [Premier League](https://www.premierleague.com/es/news/4662306/arsenal-win-2025-26-premier-league-title-ending-22-year-wait-to-be-crowned-champions-again) | Confirmed |
| Bulgaria won Eurovision 2026; the UK hasn't won since 1997 | [Express & Star](https://www.expressandstar.com/whats-on/showbiz/uks-look-mum-no-computer-last-in-eurovision-final-as-bulgaria-wins-first-trophy-8550005) | Confirmed |
| Jakarta is the world's most populous city | [UN DESA](https://desapublications.un.org/un-desa-voice/feature/december-2025/latest-urbanization-data-reveal-worlds-most-populous-cities) | Confirmed, with Dhaka second and Tokyo third. Tokyo was added as a wrong answer |
| The UK prime minister | News reports | Andy Burnham replaced Keir Starmer in July 2026. All "who holds this job now" questions were removed |
| Minecraft is the best-selling video game | [Guinness World Records](https://guinnessworldrecords.com/world-records/best-selling-video-game) | Confirmed: over 350 million copies |
| Turkey drinks the most tea per person | Wikipedia list of countries by tea consumption | Confirmed: about 3.16 kg a year |
| Finland drinks the most coffee per person | [AFAR](https://www.afar.com/magazine/this-country-drinks-more-coffee-than-any-other) | Confirmed: about 12 kg a year |
| Loch Ness holds more water than all the lakes in England and Wales | Wikipedia: Loch Ness | Confirmed |
| Dyson made 5,127 prototypes | Wikipedia: James Dyson | Confirmed |
| Wannabe was number one in 37 countries | Wikipedia: Spice Girls | Confirmed |
| Glastonbury 1970: £1 tickets, free milk, the day after Hendrix died | [NME](https://www.nme.com/features/glastonbury-festival-first-ever-story-1970-2510609) | Confirmed |
| Chichén Itzá's 365 steps | Wikipedia: El Castillo, Chichen Itza | Confirmed, counting the top platform. The fact says so |
| Prague's Astronomical Clock, 1410 | [Linda Hall Library](https://www.lindahall.org/about/news/scientist-of-the-day/prague-astronomical-clock/) | Confirmed |
| The USA topped the Paris 2024 medal table | [CBS Sports](https://www.cbssports.com/olympics/news/2024-paris-olympics-medal-count-tracker-for-how-many-gold-silver-bronze-medals-usa-each-country-has-won) | Confirmed: level with China on 40 golds, ahead on silvers |
| Sinner and Nosková won Wimbledon 2026 | [Flashscore](https://www.flashscore.com/news/tennis-wimbledon-atp-singles-the-base-line-sinner-goes-back-to-back-at-wimbledon-as-noskova-wins-all-czech-epic/foxlI0me/) | Confirmed |
| Djokovic has 24 Grand Slam singles titles; Alcaraz 7 | [Tennis365](https://www.tennis365.com/facts-stats/active-atp-players-win-grand-slam-title), as of February 2026 | Confirmed, with an as-of date |
| PSG won the Champions League in 2025 and 2026 | [Euronews](https://www.euronews.com/2026/05/30/paris-saint-germain-wins-the-champions-league-after-penalty-shootout-victory-against-arsen) | Confirmed: 5-0 against Inter in 2025; beat Arsenal on penalties after 1-1 in Budapest in 2026 |
| Mbappé is the all-time World Cup top scorer with 22 goals | [Fox Sports](https://www.foxsports.com/stories/soccer/world-cup-goal-scorers-all-time-messi-mbappe) | Confirmed: 10 of them in 2026, passing Klose's 16 |
| Despacito was the first YouTube video to reach 5 billion views | [Guinness World Records](https://www.guinnessworldrecords.com/world-records/520890-first-youtube-video-to-receive-5-billion-views) | Confirmed, April 2018 |
| Saturn has more known moons than any other planet | [Space.com](https://www.space.com/astronomy/saturn/astronomers-keep-finding-new-moons-of-jupiter-and-saturn) | Confirmed: about 285. The question carries an as-of date because the count keeps rising |
| Damavand is Asia's highest volcano | [Explorersweb](https://explorersweb.com/the-battle-over-asias-tallest-volcano-damavand-versus-kunlun/) | Disputed: a volcano in the Kunlun range may be taller. The fact now says "often called" and the question only asks about Iran and Mont Blanc |
| Koala fingerprints are almost identical to ours | [PBS NOVA](https://www.pbs.org/wgbh/nova/article/koala-fingerprints) | Confirmed |
| Danone began in Barcelona in 1919 | [Danone](https://www.danone.com/group/about-us/our-history.html) | Confirmed |
| Mini Babybel launched in 1977 | Supermarket listings and brand pages | Couldn't be confirmed, so the fact was rewritten without the year |
| Nobody knows for sure where the word "quiz" comes from | [Merriam-Webster](https://www.merriam-webster.com/wordplay/word-history-of-quiz) | Confirmed: the Dublin bet story is first recorded in 1856 and nothing backs it up |
| Shakespeare is the first recorded user of "eyeball" | [Mental Floss](https://mentalfloss.com/article/48657/20-words-) | Confirmed. The same article lists words often wrongly credited to him, so none of those were used |
| The Hawaiian alphabet has 13 letters | [Wikipedia: Hawaiian alphabet](https://en.wikipedia.org/wiki/Hawaiian_alphabet) | Confirmed: five vowels, seven consonants and the ʻokina |
| Key dates in British history | [English Heritage timeline](https://www.english-heritage.org.uk/members-area/kids/kids-timeline-of-history/) | Hastings, Magna Carta, Gunpowder Plot, Great Fire, Waterloo, Victoria, Lindisfarne, Hadrian's Wall, Black Death and the Roman invasion confirmed |
| Lewis Hamilton has the most F1 race wins: 106 | [Formula 1](https://www.formula1.com/en/latest/article/in-numbers-the-incredible-records-hamilton-holds-ahead-of-his-400th-grand-prix.1yNnQ8vuefRFhQj4AprTh0) and [Guinness World Records](https://www.guinnessworldrecords.com/world-records/63911-most-formula-one-grand-prix-wins-by-a-driver) | Confirmed: his first Ferrari win, at the Barcelona-Catalunya Grand Prix on 14 June 2026, took him to 106. Carries an as-of date |
| The Seattle Seahawks won Super Bowl LX; Bad Bunny did the halftime show | [JamBase](https://www.jambase.com/article/bad-bunny-super-bowl-lx-halftime-show-video) | Confirmed: beat the New England Patriots, 8 February 2026, a week after Bad Bunny's Album of the Year Grammy |
| Glasgow hosted the 2026 Commonwealth Games | [TNT Sports](https://www.tntsports.co.uk/commonwealth-games/2026/closing-ceremony-how-to-watch-start-time-who-is-performing_sto23324807/story.shtml) and [The Scotsman](https://www.scotsman.com/sport/other-sport/glasgow-2026-commonwealth-games-closing-ceremony-in-pictures-here-are-29-amazing-photos-of-the-spectacular-show-at-the-ovo-hydro-8835983) | Confirmed: stepped in when Victoria pulled out; Australia topped the table with 70 golds |
| Argentina have won the Copa América a record 16 times | [CONMEBOL](https://copaamerica.com/en/news/all-of-the-conmebol-copa-america-champions) | Confirmed: one ahead of Uruguay since 2024. Carries an as-of date |
| Artemis II flew four astronauts round the Moon in April 2026 | [collectSPACE](https://www.collectspace.com/news/news-041026a-artemis-ii-splashdown-landing-recovery.html) | Confirmed: launched 1 April, splashed down 10 April. Christina Koch was the first woman to travel to the Moon |
| Adults need about 7 to 9 hours of sleep | [NHS Every Mind Matters](https://www.nhs.uk/oneyou/every-mind-matters/sleep/) | Confirmed |
| Wash hands for about 20 seconds, the time it takes to sing Happy Birthday twice | [NHS](https://www.nhs.uk/live-well/best-way-to-wash-your-hands/) | Confirmed |
| At least 5 portions of fruit and veg a day, each 80 g | [NHS](https://www.nhs.uk/live-well/eat-well/5-a-day/portion-sizes/) | Confirmed |
| SPF measures UVB protection; the UK star rating measures UVA | [NHS](https://www.nhs.uk/livewell/skin/pages/sunsafe.aspx) and NHS trust pages | Confirmed |

## What the checks changed

- **The Statue of Liberty** took about 30 years, not 20, to turn fully green. The fact was corrected.
- **The Angel of the North's** 54-metre wings are almost as wide as a jumbo jet's, not wider. Corrected.
- **Leonardo DiCaprio** had four earlier acting nominations before his Oscar, not five. Corrected.
- **Abraham Lincoln** issued the Emancipation Proclamation; slavery was formally abolished after his death. The
  question was reworded.
- **Two facts with figures that couldn't be confirmed** (Ronald Reagan's exact film count and how many countries
  make Strictly) were rewritten without the numbers.
- **"The most-eaten meat"** was dropped: sources disagree on whether pork or chicken is now ahead.
- **Wrong answers that named people who don't exist**, such as made-up pairs of brothers, were replaced with real
  ones.
- **Hugo Boss** was asked about as a maker of 'work clothes and uniforms'. Accurate, but it invites a dark
  history that doesn't belong in a light-hearted quiz, so it now asks where the company was founded.
- **Old Faithful** erupts roughly every 90 minutes, not every hour. Corrected.
- **Religion** was taken out: a Diwali question became La Tomatina, and a camera-brand fact lost its religious detail.
- **"Which language has the most native speakers?"** was already in the bank, so the Words & Language version was
  swapped for a question about the word "piano".
- **New questions** replaced weaker ones where checking turned up something better: the 2025 to 2026 Premier League,
  Eurovision 2026 and the UN's new list of the biggest cities.
- **Euro 2028** will no longer have games in Northern Ireland after Casement Park was dropped, so the fact lists
  England, Scotland, Wales and the Republic of Ireland.
- **Blinding Lights'** 90 weeks in the US Hot 100 was once a record but has since been passed, so the question no
  longer calls it one.
- **The Liverpool and Manchester Railway** wasn't the first passenger railway (the Stockton and Darlington carried
  passengers in 1825), so it's now called the first inter-city railway.
- **The cornea** isn't the only part of the body without blood vessels, so the question now asks about the eye.
- **Britney Spears** was 16, not 15, when '...Baby One More Time' reached number one. Corrected before release.
- **The green anaconda's** often-quoted 200 kg isn't reliably recorded, so the fact no longer gives a weight.
- **Questions too close to existing ones** were dropped: the Shard against the Eiffel Tower (already asked the
  other way round), the Golden Gate Bridge's opening year and the Hollywood sign, whose answer another fact gives away.

If you find anything else, please [report it](https://github.com/ShazMoghaddam/hunchy/issues/new?template=question-check.yml).
