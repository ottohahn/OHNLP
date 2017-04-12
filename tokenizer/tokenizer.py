#!/usr/bin/env python3

"""
Simple Tokenizer function using a regular expression or a vocabulary to split a
text
"""

BASIC_RE = re.compile(r"[\w']+|[\!\#\$\%\&\\\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\]\^\_\`\{\|\}\~]")

def tokenize(text, regex = BASIC_RE):
    """
    A function to tokenize a string of text using regular expressions or a
    vocabulary
    INPUT: A TEXT STRING
    OUTPUT: A LIST OF TOKENS (STRINGS)
    """
    if regex is not None:
        tokens = BASIC_RE.find_all(text)
        return tokens
    
