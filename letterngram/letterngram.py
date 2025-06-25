#!/usr/bin/env python3
"""
letter n-gram calculator for text:
it generates a frequency distribution for the different n-grams found in a text
sample.
INPUT: TEXT, A STRING; N INTEGER
OUTPUT: NGRAMS: A DICTIONARY WITH THE NGRAMS AS KEYS AND THE FREQUENCY AS VALUE
"""

from collections import Counter


def letterngrams(text, num=1, charset="alpha"):
    """Return normalized letter ``num``-gram frequencies for ``text``.

    ``charset`` determines which n-grams are counted:
    ``"alpha"`` only alphabetic, ``"alphanum"`` alphanumeric, ``"num"`` digits
    only and ``"all"`` accepts every character.
    """

    # Normalize whitespace once
    text = text.replace("\n", " ").replace("\t", " ")

    # Pad words with ``@`` symbols and join them using the same padding.  This
    # mirrors the behaviour of the original implementation but avoids repeated
    # string concatenations inside the loop.
    pad = "@" * num
    text = pad + pad.join(text.split()) + pad

    ngrams = []
    for i in range(len(text) - num + 1):
        chunk = text[i:i + num]

        if charset == "alpha" and not chunk.isalpha():
            continue
        if charset == "alphanum" and not chunk.isalnum():
            continue
        if charset == "num" and not chunk.isdigit():
            continue

        ngrams.append(chunk)

    total = len(ngrams)
    freq = Counter(ngrams)
    return {k: v / total for k, v in freq.items()}
