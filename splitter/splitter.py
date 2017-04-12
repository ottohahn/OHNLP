#!/usr/bin/env python3
"""
A basic sentence splitter, it takes a text as input and returns an array of
sentences
"""
import re

INITIALS_RE = re.compile(r'([A-z])\.')

def splitter(text):
    """
    Basic sentence splitting routine
    It doesn't take into account dialog or quoted sentences inside a sentence.
    """
    sentences = []
    # First step remove newlines
    text = text.replace('\n', ' ')
    # we remove tabs
    text = text.replace('\t', ' ')
    # then we replace abbreviations
    text = text.replace('Ph.D.', "Ph<prd>D<prd>")
    text = text.replace('Mr.', 'Mr<prd>')
    text = text.replace('St.', 'Mr<prd>')
    text = text.replace('Mrs.', 'Mrs<prd>')
    text = text.replace('Ms.', 'Ms<prd>')
    text = text.replace('Dr.', 'Dr<prd>')
    text = text.replace('Drs.', 'Drs<prd>')
    text = text.replace('vs.', 'vs<prd>')
    text = text.replace('etc.', 'etc<prd>')
    text = text.replace('Inc.', 'Inc<prd>')
    text = text.replace('Ltd.', 'Ltd<prd>')
    text = text.replace('Jr.', 'Jr<prd>')
    text = text.replace('Sr.', 'Sr<prd>')
    text = text.replace('Co.', 'Co<prd>')
    text = INITIALS_RE.sub('\1<prd>', text)
    text = text.replace('.', '.<stop>')
    text = text.replace('?', '?<stop>')
    text = text.replace('!', '!<stop>')
    text = text.replace('<prd>', '.')
    sentences = text.split('<stop>')
    return sentences
