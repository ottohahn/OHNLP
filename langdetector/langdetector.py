#!/usr/bin/env python3

"""
A language detector using cosine distance and n-grams
TO DO
- [ ] Calcular la frecuencia de cada ngrama en letterngram
- [ ] Contar solo las letras o poner una opcion en letterngram para contar solo
      letras
"""
import math
import string
import pickle
import OHNLP.letterngram.letterngram as lng


def bigram_freq(textinp):
    """
    Function to calculate the letter bigram frequency distribution of a
    string using the letterngram function
    """
    bigrams = {}
    tot = 0.0
    # Iterate over text and ignore punctuation, and numbers
    textinp = textinp.replace('\n', ' ')
    for i in range(0, len(textinp)-1):
        if (((textinp[i].isalpha()) and  (textinp[i] not in string.punctuation))
                and ((textinp[i+1].isalpha()) and  (textinp[i+1] not in string.punctuation))):
            if textinp[i:i+2].lower() in bigrams:
                bigrams[textinp[i:i+2].lower()] += 1.
            else:
                bigrams[textinp[i:i+2].lower()] = 1.
            tot += 1.0
    for key in bigrams:
        bigrams[key] = bigrams[key] / tot
    return bigrams

def cosine_distance(vec1, vec2):
    """
    Function to calculate the cosine distance between two dictionaries
    """
    if len(vec1) == 0 or len(vec2) == 0:
        return 0
    if len(vec2) < len(vec1):
        vec1, vec2 = vec2, vec1
    res = 0
    norm_vec1 = 0
    norm_vec2 = 0
    for key in vec1:
        norm_vec1 += vec1[key]**2
    norm_vec1 = math.sqrt(norm_vec1)
    for key in vec2:
        norm_vec2 += vec2[key]**2
    norm_vec2 = math.sqrt(norm_vec2)
    for key in vec1:
        if key in vec2:
            res += vec1[key]*vec2[key]
    if res == 0:
        return 0
    try:
        res = res / (norm_vec1*norm_vec2)
    except ZeroDivisionError:
        res = 0
    return res

def create_lang_model(corpus, modelname):
    """
    Auxiliary function to create a language model from a group of files
    and store it in the languages dictionary, then pickle everything
    
    """
    # Corpus is a list of filenames that we have to open
    master = ""
    for doc in corpus:
        fileinp = open(doc, 'r')
        raw_text = fileinp.read()
        master += raw_text  # here we have a huge string
    model = bigram_freq(master)
    # Open the modelname file
    fileout = open(modelname, 'w')
    for key in model:
        fileout.write(key+','+str(model[key])+'\n')
    fileout.close()

def readmodels(filename):
    """
    Here we will read a pickle file of the models
    """
    lang_dict = pickle.load(open(filename, "rb"))
    return lang_dict

def language_detection(sample):
    """
    Language detection routine that reads language models from text files
    and calculate which one is the nearest neighbour to the given text
    returning the name of the model file as the output
    """
    # Here we are going to read the models
    lang_dict = readmodels('models.pkl')
    # Here we begin the actual language detection
    sample_freq = lng.letterngrams(sample, num=2) # Change this to letterngrams
    mindist = 0.5
    lang = 'UNK'
    for key in lang_dict:
        dist = cosine_distance(sample_freq, lang_dict[key])
        # print(key, dist)
        if dist > mindist:
            mindist = dist
            lang = key
    return lang
