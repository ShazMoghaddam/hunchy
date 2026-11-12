# Security policy

Hunchy is a static web page with no server, no accounts and no data collection, so the risks are small, but they're
taken seriously.

## Supported versions

Only the latest version on the `main` branch, which is what's live at
[shazmoghaddam.github.io/hunchy](https://shazmoghaddam.github.io/hunchy/), is supported.

## Reporting a vulnerability

Please report it privately, not in a public issue.

1. Open the [Security tab](https://github.com/ShazMoghaddam/hunchy/security) and press **Report a vulnerability**, or go straight to [a new advisory](https://github.com/ShazMoghaddam/hunchy/security/advisories/new).
2. Describe the problem and the steps that show it.

You'll get a reply within 7 days. Once the problem is confirmed, I'll agree a fix and a disclosure date with you, and
credit you in the advisory and the changelog unless you'd rather stay anonymous.

## Scope

In scope:

- The game in `index.html` and `assets/`, for example text from a question, a player's name or a link that could run
  script in the page.
- The scripts in `questions/` and the workflows in `.github/workflows/`.

Out of scope:

- GitHub Pages itself. Please report problems there to GitHub.
- A wrong answer. That isn't a security issue, but please
  [report it here](https://github.com/ShazMoghaddam/hunchy/issues/new?template=question-check.yml).

---

Created by **Shaz Moghaddam** · London
[Website](https://shazmoghaddam.github.io) · [LinkedIn](https://www.linkedin.com/in/shazmoghaddam)
