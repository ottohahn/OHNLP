#!/usr/bin/env python3

"""
Module for language detection routiines using bigrams and cosine distance
Created by Otto Hahn Herrera
12/20/2016
Atipica Inc.
"""

import math
import string

class LanguageDetector:
    """
    Language detector class using letter bigram frequency and cosine distance
    """
    def __init__(self, list_of_models):
        """
        Here we will read the data files into a dictionary
        """
        self.lang_dict = {}
        for model in list_of_models:
            langmodel = {}
            modelfile = open(model, 'r')
            modellines = modelfile.readlines()
            for line in modellines:
                data = line.split(',')
                langmodel[data[0]] = float(data[1].strip())
            self.lang_dict[model[:-4]] = langmodel

    def bigram_freq(self, textinp):
        """
        Function to calculate the letter bigram frequency distribution of a
        string
        """
        bigrams = {}
        tot = 0.0
        # Iterate over text and ignore punctuation, and numbers
        textinp = textinp.replace('\n', ' ')
        for i in range(0, len(textinp)-1):
            if (((textinp[i].isalpha()) and  (textinp[i] not in string.punctuation)) and ((textinp[i+1].isalpha()) and  (textinp[i+1] not in string.punctuation))):
                if textinp[i:i+2].lower() in bigrams:
                    bigrams[textinp[i:i+2].lower()] += 1.
                else:
                    bigrams[textinp[i:i+2].lower()] = 1.
                tot += 1.0
        for key in bigrams:
            bigrams[key] = bigrams[key] / tot
        return bigrams


    def cosine_distance(self, vec1, vec2):
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

    
    def create_lang_model(self, corpus, modelname):
        """
        Auxiliary function to create a language model from a group of files
        and name it as a language like english.txt (otherwise the detection
        won't work properly)
        """
        # Corpus is a list of filenames that we have to open
        master = ""
        for doc in corpus:
            fileinp = open(doc, 'r')
            raw_text = fileinp.read()
            master += raw_text  # here we have a huge string
        model = self.bigram_freq(master)
        # Open the modelname file
        fileout = open(modelname, 'w')
        for key in model:
            fileout.write(key+','+str(model[key])+'\n')
        fileout.close()

    def language_detection(self, sample):
        """
        Language detection routine that reads language models from text files
        and calculate which one is the nearest neighbour to the given text
        returning the name of the model file as the output
        """
        # Here we begin the actual language detection
        sample_freq = self.bigram_freq(sample)
        mindist = 0.5
        lang = 'UNK'
        for key in self.lang_dict:
            dist = self.cosine_distance(sample_freq, self.lang_dict[key])
            # print(key, dist)
            if dist > mindist:
                mindist = dist
                lang = key
        return lang

if __name__ == '__main__':
    # We are going to generate models for Engish, Spanish, French and German
    #list_of_books = ['bailen.txt', 'la_regenta.txt', 'el_quijote.txt']
    #create_lang_model(list_of_books, 'ES.txt')
    #resumefile = open('res29-306926.txt','r')
    #resume = resumefile.read()
    resume = """
    Logo n'essa semana, sem escolher, Jacintho _Galião_ comprou a um
    Principe polaco, que depois da tomada de Varsovia se mettera frade
    cartuxo, aquelle palacete dos Campos Elyseos, n.^o 202. E sob o pesado
    ouro dos seus estuques, entre as suas ramalhudas sedas se enconchou,
    descançando de tantas agitações, n'uma vida de pachorra e de boa mesa,
    com alguns companheiros d'emigração (o desembargador Nuno Velho, o conde
    de Rabacena, outros menores), até que morreu de indigestão, d'uma
    lampreia d'escabeche que lhe mandára o seu procurador em Monte-mór. Os
    amigos pensavam que a snr.^a D. Angelina Fafes voltaria ao reino. Mas a
    boa senhora temia a jornada, os mares, as caleças que racham. E não se
    queria separar do seu Confessor, nem do seu Medico, que tão bem lhe
    comprehendiam os escrupulos e a asthma.
    """
    langdet = LanguageDetector(['us_ENG.txt', 'FR.txt', 'PR.txt', 'ES.txt'])
    print(langdet.language_detection(resume))
    #print(language_detection(resume, ['us_ENG.txt', 'FR.txt', 'PR.txt', 'ES.txt'])) 
