# Changelog

## v1.3.0 (2026-11-13)

A much bigger question bank: **2,207 questions, up from 1,630**. The 577 new ones lean into film, music, art and
culture, with tempting wrong answers that make you stop and think: another famous Tom, the actor who played the same
part in a different film, or a song with almost the same title.

- **Film & TV (+153):** Top Gun, Gladiator, Casablanca, The Godfather, Barbie and Frankenstein; Clint Eastwood, Morgan
  Freeman, Jacob Elordi and Mark Wahlberg; the great directors, film music, James Bond, British comedy, quiz shows and
  streaming.
- **Music (+145):** "Who sang it?" from Elvis and Motown to Sabrina Carpenter, and "Which of these is a Madonna song?"
  style questions, plus the stories behind famous covers, Eurovision, classical music and musicals. Song titles only,
  never lyrics.
- **Art & Culture (+108):** the world's great museums, from the V&A, the Science Museum and the National Gallery to the
  Louvre, MoMA, the Prado, the Rijksmuseum and the Grand Egyptian Museum; plus artists, architects, books and festivals.
- **The other subjects (+171):** cartoons, fashion, cars and motorbikes, food, inventions, words, nature and space.
- **Checked twice.** Every film cast and year was checked against a dataset built from Wikipedia, and every singer
  against the full Billboard Hot 100 history, including the wrong answers, so a decoy actor is never secretly in the
  film. The newest facts were checked against news reports. See `questions/CHECKS.md`.
- **No giveaways.** Each new question was checked against the facts shown after every other question, and 30 were
  replaced because another answer's fact would have given them away.
- The README, page description, banner and social preview now say 2,200+.

## v1.2.1 (2026-11-13)

**No more repeated questions.** With 1,630 questions in the bank, the same ones were coming up far too often. Three
things were causing it, and all three are fixed. Nothing to do on your phone: the update arrives by itself.

- **Playing one subject wiped your memory of everything.** Hunchy remembers which questions you've answered, but as
  soon as a single subject ran low (Fashion has 32 questions, so after three rounds), it forgot every question in
  every subject and started again. Now only questions you've seen in that subject can come back, starting with the
  ones you saw longest ago. In a test of 60 mixed rounds, repeats outside that subject went from 76 to none.
- **Today's ten kept picking from tiny piles.** It asked for a set kind and difficulty in each subject, and some
  subjects have only one or two questions of that kind, so the same question turned up again and again (one
  appeared 11 times in 90 days). The whole bank is now dealt out once into a fixed run of daily tens, still the same
  for everyone, so no daily question comes round again for about five months. Every day still has ten different
  subjects, at least one yes/no or higher/lower, and something classic and something modern.
- **Mixed rounds leaned on the biggest subjects.** Sport has 220 questions and Fashion 32, so a mixed round often
  had two or three sport questions. A mixed round now moves through ten different subjects.
- Yes/no and higher/lower questions are rarer than pick-one, so they no longer get repeated just to fill a slot. If
  you've seen them all, a fresh pick-one takes their place.
- New tests (`tests/picker.test.js`) check all of this on every pull request.

## v1.2.0 (2026-11-12)

A much bigger question bank: **1,630 questions, up from 1,260**. No new subjects; the existing ones go deeper.

- **Sport (+72):** the World Cup from 1998 to 2030, the Euros and the Copa América, the Olympics (how often they're
  held, legends from Jesse Owens to Nadia Comăneci), Formula One (Hamilton's record 106 wins, Senna, Silverstone,
  Monaco) and the big events: the Masters, the Ryder Cup, the Grand National, the Boat Race, the Six Nations,
  darts, snooker and boxing.
- **Music (+60):** bands, hit songs and singers, from the Beatles, Queen, ABBA and Motown to Oasis, BLACKPINK and
  Bad Bunny, plus composers and instruments.
- **Geography (+47):** the Nile, the Amazon, the Arctic and Antarctic, the Equator and the lines on the map, and the
  shape of the world.
- **Cities & Landmarks (+39):** the Great Wall of China, the Grand Canyon, Niagara Falls, the Statue of Liberty,
  the Golden Gate's city, the Tower of London, and natural wonders from Iguazu to the Salar de Uyuni.
- **Leaders & Famous People (+44):** inventors such as Edison, Bell, Tesla and Marconi; explorers such as Scott and
  Shackleton; and leaders who made a mark, including Nelson Mandela, Gandhi and Churchill. History, never politics.
- **Science (+51):** chemistry, physics, how the body works, and health facts checked against the NHS.
- **History (+19), Maths (+15), Space (+11) and Nature & Animals (+12)**, including Artemis II's 2026 trip round the Moon.
- Recent facts (Hamilton's wins, Super Bowl LX, Glasgow 2026, Artemis II, the Copa América record) were checked
  against a second source and are listed in `questions/CHECKS.md`.
- **100 more grown-up jokes**, making 200 in all. They're teasing, a little flirty or a little dark, never crude,
  and they only appear when Grown-up jokes is switched on in Settings. The existing jokes keep their ids, so
  nobody's "already seen" list is reset.
- The README banner and social preview now say 1,600+.

## v1.1.2 (2026-11-12)

- **A quiz for any get-together.** Hunchy's wording now fits every group: friends round, a party, the pub or a
  night in. The new line, "A free quiz for any get-together", is used in the app, the page description and link
  previews, the share messages, the README, the banner and the social preview.
- Two jokes reworded to match, with no change to how they play.
- A new test keeps the old wording from creeping back into the app and docs. The questions themselves are unchanged.

## v1.1.1 (2026-11-12)

- **Updates arrive straight away.** When a new version of Hunchy is published, the page now reloads itself onto it
  as soon as it's ready, instead of showing the old version for one more visit. If a round is being played, it waits
  until the round is over, so no game is lost.
- Hunchy now checks for a new version whenever it comes back to the screen, which helps on phones that keep it open
  in the background.
- A new version always downloads fresh files, never ones the browser kept from earlier.
- A test now checks that the offline copy's version in `sw.js` matches the latest version in this changelog.

## v1.1.0 (2026-11-12)

A new look, an 18th subject, and a game that works anywhere.

- **Midnight pop.** A new design: deep navy, a glowing daily card, a bright colour for every subject, and the
  Urbanist typeface throughout. Every icon is a clean outline drawing, including a redrawn streak flame.
- **A light look** for bright rooms and sunshine, chosen in Settings. Dark stays the default.
- **Words & Language**, the 18th subject: 60 questions on where words come from, languages of the world, alphabets
  and wordplay. That takes Hunchy past 1,200 questions, and the subject grid now fills its rows on phones and computers.
- **Plays offline.** Once Hunchy has loaded, it works with no signal, and phones can add it to the home screen.
- **No repeats until you've seen everything.** The game now remembers every question you've answered, not just the
  last 500.
- **Sound and buzz.** A soft sound for right and wrong answers and a little buzz on phones that support it, with a
  switch in Settings and a quick mute while you play.
- **Your stats**: questions answered, your hit rate, games finished, longest daily streak, best run at three lives,
  perfect tens, and your best subjects.
- **Settings** in one place on the home screen: easier questions, grown-up jokes, sound and buzz, and the look.
- **A proper footer**, in the two-tone style of [shazmoghaddam.github.io](https://shazmoghaddam.github.io/), with how
  to play, your stats, the live question count and the credits.
- New app icons, README banner and social preview to match.

## v1.0.0 (2026-11-12)

First release of Hunchy, a free quiz for any get-together. Go with your hunch.

- **1,200 questions in 17 subjects**: Geography, Cities & Landmarks, History, Leaders & Famous People, Science,
  Space, Nature & Animals, Maths, Sport, Film & TV, Music, Art & Culture, Food & Drink, Inventions & Brands,
  Cars & Motorbikes, Fashion, and Cartoons & Animation.
- **Three kinds of question**: higher or lower, yes or no, and pick one. Some are turned round, such as capitals
  asked both ways and "which of these brands comes from Japan?". Each is tagged timeless, classic or modern, and
  rated from 1 to 3 for difficulty.
- **Four ways to play**: today's ten (the same for everyone each day, with streaks), quick round, three lives, and
  Hunch-off, where 2 to 6 players take turns on one phone.
- **Easier questions** setting that leaves out the hardest ones.
- **100 original jokes.** One at the end of every game and a joke break between Hunch-off rounds, with the setup
  first and a tap for the punchline. No repeats until you've seen them all. A **Grown-up jokes** switch, off by
  default, adds 25 cheekier ones.
- **Share anything.** Every result and every joke has a share button: the share sheet on phones, copy to clipboard
  elsewhere. Shared scores never give away an answer.
- **Every answer sourced.** Each question shows a "did you know" fact, its source, an as-of date where facts can
  change, and a link to report a problem. Maths is worked out by code; country and element facts are only used where
  two independent datasets agree. No religion, and leaders only as history, never party politics.
- **Built for every screen**, with dark mode, full keyboard play, screen reader announcements, reduced-motion support
  and self-hosted fonts. No accounts, cookies, adverts or tracking.
- **Checks** that rebuild and test every question and joke on each pull request, and fail if a published data file
  doesn't match its source.
- MIT licence, contribution guide, security policy, issue templates, Dependabot, banner and social preview.
