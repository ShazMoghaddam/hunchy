"""Hand-written questions, one file per category.

Each question is written with one of three helpers:

    yes_no(prompt, True or False, fact, source)
    higher_lower(prompt, True if the answer is the first label, fact, source, labels=("Higher", "Lower"))
    choice(prompt, right_answer, [three wrong answers], fact, source)

and these optional settings:

    era         "timeless" (anyone can know it), "classic" (older generations have the edge) or "modern" (younger ones do)
    difficulty  1 (easy for most players, and used for 'Easier questions'), 2 (most adults) or 3 (a real stretch)
    as_of       for anything that can change, such as a record or a count: the date it was last checked

Every source is a page that states the answer. CONTRIBUTING.md explains how questions are checked.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Category:
    key: str
    prefix: str = ""  # a second file for the same subject gives its ids a different prefix, e.g. "sport2"
    questions: list[dict] = field(default_factory=list)

    def _add(self, kind, prompt, options, answer, fact, source, era, difficulty, as_of):
        name, url = source
        q = {"id": f"{self.prefix or self.key}-{len(self.questions) + 1:03d}", "category": self.key, "type": kind, "prompt": prompt,
             "options": options, "answer": answer, "fact": fact, "era": era, "difficulty": difficulty,
             "source": {"name": name, "url": url}}
        if as_of:
            q["asOf"] = as_of
        self.questions.append(q)

    def yes_no(self, prompt, truth, fact, source, era="timeless", difficulty=2, as_of=None):
        self._add("yes-no", prompt, ["Yes", "No"], 0 if truth else 1, fact, source, era, difficulty, as_of)

    def true_false(self, prompt, truth, fact, source, era="timeless", difficulty=2, as_of=None):
        self._add("yes-no", prompt, ["True", "False"], 0 if truth else 1, fact, source, era, difficulty, as_of)

    def higher_lower(self, prompt, first, fact, source, labels=("Higher", "Lower"), era="timeless", difficulty=2, as_of=None):
        self._add("higher-lower", prompt, list(labels), 0 if first else 1, fact, source, era, difficulty, as_of)

    def choice(self, prompt, right, wrong, fact, source, era="timeless", difficulty=2, as_of=None):
        assert len(wrong) in (2, 3) and right not in wrong, prompt
        self._add("choice", prompt, [right, *wrong], 0, fact, source, era, difficulty, as_of)


def wiki(title: str) -> tuple[str, str]:
    """A Wikipedia article as a source: wiki('Apollo 11')."""
    return (f"Wikipedia: {title}", "https://en.wikipedia.org/wiki/" + title.replace(" ", "_"))


def brit(name: str, path: str) -> tuple[str, str]:
    """An Encyclopaedia Britannica article as a source."""
    return (f"Britannica: {name}", "https://www.britannica.com/" + path)
