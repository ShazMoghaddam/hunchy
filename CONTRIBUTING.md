# Contributing to Hunchy

Thanks for helping. The most useful things you can do are spot wrong answers and suggest good questions.

## Reporting a wrong answer

Use the **Report this question** link that appears after you answer, or
[open a question check](https://github.com/ShazMoghaddam/hunchy/issues/new?template=question-check.yml). A link to
a reliable source with the right answer makes it quick to fix.

## Suggesting a question

[Open an idea](https://github.com/ShazMoghaddam/hunchy/issues/new?template=idea.yml), or add it yourself in a pull
request.

## Writing a question

Questions live in `questions/curated/`, one file per group of subjects. Each one is a single call:

```python
c.choice("Which planet is known as the Red Planet?", "Mars", ["Jupiter", "Venus", "Mercury"],
         "Mars looks red because its soil is full of iron oxide: rust.",
         wiki("Mars"), difficulty=1)
```

There are three kinds, `yes_no` (or `true_false`), `higher_lower` and `choice`. The docstring at the top of
`questions/curated/__init__.py` explains each setting.

A good Hunchy question:

- **Has one clear, checkable answer.** If reliable sources disagree, it doesn't go in.
- **Has a source that states the answer.** Link the page itself, not a search result.
- **Says when it was true**, with `as_of`, if it could ever change: records, rankings, counts and "the most".
- **Doesn't ask who holds a job now.** Prime ministers, presidents and champions change. Ask about a year that's
  over instead.
- **Is fair to everyone at the table.** Set `era` to `timeless`, `classic` or `modern`, and `difficulty` from 1
  (easy for almost anyone) to 3 (a real stretch). Questions rated 3 are left out when someone chooses Easier questions.
- **Has believable wrong answers.** The best ones are things people genuinely mix up.
- **Never quotes song lyrics.** Ask about the title, the artist or the year.
- **Stays light.** No religion, no party politics, nothing that would start an argument at Christmas dinner.
- **Ends with a fact worth knowing**, in one or two plain sentences.

Then check it and rebuild the question file:

```bash
pip3 install -r requirements-dev.txt
python3 questions/build.py
python3 -m pytest
```

`build.py` refuses to save if anything breaks the rules, and the tests check the answers again. Commit your
change together with the updated `data/questions.json`.

## Writing a joke

Jokes live in [`jokes/build_jokes.py`](jokes/build_jokes.py) as pairs of setup and punchline. `FAMILY` jokes are
for everyone; `GROWN_UPS` jokes can be cheekier, flirtier or a bit darker, but never crude, cruel or about real
people. Every joke should be original, not copied from a joke book or website. Rebuild with
`python3 jokes/build_jokes.py`, then run the tests.

## Changing the game

The game is plain HTML, CSS and JavaScript: `index.html`, `assets/app.js` and `assets/styles.css`. Run
`python3 -m http.server 8000` and open http://localhost:8000 to try your changes. Please check them on a phone-sized
screen, with a keyboard, and in dark mode.

## Pull requests

Work on a new branch, keep each pull request to one change, and fill in the checklist in the template.
By contributing you agree to share your work under the [MIT licence](LICENSE).
