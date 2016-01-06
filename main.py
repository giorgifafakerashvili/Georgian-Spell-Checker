# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 14:37:58 2015

@author: giorgi fafakerashvili

"""

from __future__ import division
import nltk
import math
import os
import distance
import collections
import time

import geonlp
import buildindex
import hibernate
import wordgenerator.py
import utils
import suffixes
import wordsimilarity
    

     

def MLETrigram(ngram, bigramfrequency, trigramfrequency):
    a = bigramfrequency[ngram[:2]]
    b = trigramfrequency[ngram]
    print b/a
    

def MLE(ngram, freqOne, freqTwo):
    l = len(ngram)-1
    a = freqOne[ngram[:l]]
    b = freqTwo[ngram]
    return b/a
    



def predictTrigram(ngram, chars):
    l  = []
    for i in chars:
        l.append((MLE(ngram+i, bigram, trigram),i))
    l.sort(reverse=True)
    arr = [] 
    for freq, ngram in l:
        arr.append(ngram)
    return arr


def predictFourgram(ngram, chars):
    l = [] 
    for i in chars:
        l.append((MLE(ngram+i,trigram, fourgram), i))
    l.sort(reverse=True)
    arr = [] 
    for freq, ngram in l:
        arr.append(ngram)
    return arr



    





    








    




        

    
            


            
