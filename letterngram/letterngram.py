#!/usr/bin/env python3
"""
letter n-gram calculator for text:
it generates a frequency distribution for the different n-grams found in a text
sample.
INPUT: TEXT, A STRING; N INTEGER
OUTPUT: NGRAMS: A DICTIONARY WITH THE NGRAMS AS KEYS AND THE FREQUENCY AS VALUE
"""

def letterngrams(text, num=1, charset='alpha'):
    """
    A letter frequency counter for strings of text.
    the default is unigrams
    for n-grams we will use the following convention
    e.g. ablation, n = 3
    @@a
    @ab
    abl
    bla
    lat
    ati
    tio
    ion
    on@
    n@@
    the letter in question is always the last of the tuple
    for the character set it can be alpha, alphanum or all.
    """
    # First we replace newlines and tabs with space
    text = text.replace('\n', ' ')
    text = text.replace('\t', ' ')
    #Second we prepend and append n-1  @ signs
    simb = '@'
    finstr = ''
    for i in range(0, num):
        finstr += simb
    text = finstr.join(text.split())
    text = finstr + text
    text = text + finstr
    # Third we collect the n-grams
    ngramsdict = {}
    idx = 0
    for i in range(1, len(text)-num):
        if charset == 'alpha':
            if text[idx + i:idx + i + num].isalpha():
                ngram = text[idx + i:idx + i + num]
        elif charset == 'alphanum':
            if text[idx + i:idx + i + num].isalnum():
                ngram = text[idx + i:idx + i + num]
        elif charset == 'num':
            if text[idx + i:idx + i + num].isdigit():
                ngram = text[idx + i:idx + i + num]
        elif charset == 'all':
            ngram = text[idx + i:idx + i + num]
        if ngram in ngramsdict:
            ngramsdict[ngram] += 1
        else:
            ngramsdict[ngram] = 1
    return ngramsdict
