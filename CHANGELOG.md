# Changelog

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

First release of Hunchy, a free family quiz. Go with your hunch.

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
