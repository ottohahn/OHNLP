#!/usr/bin/env python3
"""
A basic sentence splitter, it takes a text as input and returns an array of
sentences
"""
import re

INITIALS_RE = re.compile(r"\b([A-Za-z])\.")
ABBREV_RE = re.compile(
    r"\b(?:Ph\.D|Mr|St|Mrs|Ms|Dr|Drs|vs|etc|Inc|Ltd|Jr|Sr|Co)\.(?=\s+[A-Z])"
)


def splitter(text):
    """
    Basic sentence splitting routine
    It doesn't take into account dialog or quoted sentences inside a sentence.
    """
    # Normalize whitespace
    text = text.replace("\n", " ").replace("\t", " ")

    # Protect abbreviations and initials
    text = ABBREV_RE.sub(lambda m: m.group(0).replace(".", "<prd>"), text)
    text = INITIALS_RE.sub(r"\1<prd>", text)

    # Split sentences on punctuation followed by whitespace
    parts = re.split(r"(?<=[.!?])\s+", text)

    # Restore protected periods
    sentences = [p.replace("<prd>", ".") for p in parts if p]
    return sentences
