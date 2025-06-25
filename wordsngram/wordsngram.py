#!/usr/bin/env python3
"""Word n-gram calculator for text.

Generates a normalized frequency distribution of word n-grams. Punctuation
marks are treated as tokens unless they are part of an abbreviation.
"""

import re
from collections import Counter

# Pattern matching common abbreviations and sequences like "U.S.A."
TOKEN_RE = re.compile(
    r"(?:[A-Za-z]\.){2,}[A-Za-z]?\.?|"
    r"(?:Mr|St|Mrs|Ms|Dr|Drs|vs|etc|Inc|Ltd|Jr|Sr|Co|Ph\.D)\.|"
    r"\w+(?:'\w+)?|[^\w\s]"
)


def _tokenize(text: str):
    """Return a list of tokens from *text* considering abbreviations."""
    text = text.replace("\n", " ").replace("\t", " ")
    return TOKEN_RE.findall(text)


def wordsngram(text: str, n: int = 1, mode: str = "front"):
    """Return ``n``-gram frequencies for *text*.

    ``mode`` selects how n-grams are created: ``front`` from start to end,
    ``back`` from end to start, and ``window`` pads the text with ``<s>`` and
    ``</s>`` symbols.
    """

    tokens = _tokenize(text)
    if not tokens or n <= 0:
        return {}

    if mode not in {"front", "back", "window"}:
        raise ValueError("mode must be 'front', 'back' or 'window'")

    if mode == "back":
        tokens = list(reversed(tokens))
    elif mode == "window":
        tokens = ["<s>"] * (n - 1) + tokens + ["</s>"] * (n - 1)

    ngrams = [tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)]
    total = len(ngrams)
    freq = Counter(ngrams)
    return {k: v / total for k, v in freq.items()}
