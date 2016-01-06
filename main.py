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







class Suffixes:
    
    @staticmethod
    def prefixes(arr):
        return filter(lambda x: len(x) > 0 and x[0] == "<", arr)
        
        
    
    @staticmethod
    def suffixes(arr):
        return filter(lambda x: len(x) > 0 and x[-1] == ">", arr)
   
   

  
def WordSimilarity(word, arr, ngrams = 1, n = 10):
    
    l = []
    c = 0
    for i in arr:
        l.append((distance.jaccard(NGramWord(i,ngrams),NGramWord(word,ngrams)), i))
    
    l.sort()
    return [(x,y) for x, y in l][:n]
    


 

    
def getNGramDict():
    di = {}    
    di[2] = ['s>', 'a>', 'i>', 'n>', 'T>', 'e>', 'c>', 'o>', 'd>', 'm>', 'l>', 'r>', 'b>', 't>', 'v>', 'u>', 'g>', 'S>', 'k>', 'A>', 'y>', 'C>', 'z>', 'E>', 'I>', 'N>', 'R>', 'f>', 'O>', 'p>', 'D>', 'x>', 'h>', 'P>', 'L>', 'M>', 'G>', 'Y>', 'F>', 'q>', 'K>', 'B>', 'X>', 'w>', 'V>', 'H>', 'U>', 'j>', 'W>', 'Z>', 'J>', 'Q>']
    di[3] = ['is>', 'an>', 'sa>', 'ma>', 'li>', 'Si>', 'ia>', 'iT>', 'as>', 'ze>', 'bi>', 'en>', 'ba>', 'bs>', 'es>', 'ad>', 'da>', 'ri>', 'ic>', 'ni>', 'os>', 'Ta>', 'aa>', 'am>', 'aT>', 'eT>', 'ul>', 'na>', 'ls>', 'on>', 'oT>', 'de>', 'vi>', 'si>', 'va>', 'di>', 'mi>', 'ec>', 'vs>', 'ra>', 'ti>', 'ea>', 'bT>', 'em>', 'ns>', 'ur>', 'io>', 'Ti>', 've>', 'To>', 'ao>', 'ki>','od>', 'ts>', 're>', 'ar>', 'vT>', 'om>', 'ne>', 'yo>',  'ms>', 'al>', 'bo>', 'do>', 'ko>', 'av>', 'ed>', 'ca>', 'xa>', 'oa>','Ci>']
    di[4] = ['bis>', 'Tan>', 'vis>', 'ebi>', 'isa>', 'ebs>', 'eba>', 'uli>', 'dan>', 'biT>', 'gan>', 'lis>', 'aSi>', 'sac>', 'lma>', 'nen>', 'aze>', 'nis>', 'lia>', 'ili>', 'bas>', 'ris>', 'ani>', 'eli>', 'uri>', 'asa>', 'bze>', 'oba>', 'bma>', 'ian>', 'iis>', 'ben>', 'bSi>', 'ken>', 'des>', 'mde>', 'oda>',  'ias>', 'iTa>', 'sis>', 'bic>', 'Sic>', 'bia>', 'ebT>', 'bsa>', 'zec>', 'diT>', 'bda>', 'mac>', 'bad>', 'ina>', 'Sia>', 'sas>', 'rad>', 'zea>', 'viT>', 'bul>', 'nia>', 'dmi>', 'mis>', 'ils>', 'eri>', 'Zis>', 'vas>', 'nac>', 'cia>', 'baa>']
    di[5] = ['ebis>', 'Tvis>', 'idan>', 'sTan>', 'ebiT>', 'bisa>', 'sgan>', 'dnen>', 'obis>', 'ebze>', 'buli>', 'ebma>',  'bTan>', 'ebSi>', 'iani>', 'eben>', 'ebas>', 'ilis>',  'amde>', 'deba>', 'baze>',  'ebic>', 'baSi>', 'sken>', 'ebsa>', 'ulia>', 'ebia>', 'obas>', 'agan>', 'boda>', 'asac>', 'isas>',  'anis>', 'beli>', 'admi>', 'ebul>', 'ebad>',  'reba>', 'ebda>','obiT>', 'bsac>', 'anac>', 'biTa>', 'ulma>', 'elis>', 'loba>', 'elma>', 'elia>',   'isac>', 'iTac>',  'bina>', 'eris>', 'acia>', 'leba>', 'urad>', 'iuri>', 'ilia>', 'nTan>', 'risa>',  'blad>', 'ania>','azec>']
    di[6] = ['sTvis>', 'isgan>', 'asTan>', 'ebisa>', 'aTvis>', 'ebuli>', 'ebTan>', 'lebis>', 'bidan>', 'rebis>',  'isken>', 'vilis>', 'eboda>', 'sadmi>', 'sagan>', 'ebeli>', 'bdnen>', 'ebian>', 'lobis>', 'Svils>', 'ebsac>', 'bulia>', 'ebaze>', 'nebis>', 'ebaSi>', 'ebiTa>', 'ebina>', 'esTan>', 'obaSi>','obisa>', 'lebma>', 'eblad>',  'iebis>', 'bamde>', 'visac>', 'odnen>', 'bisas>', 'basac>', 'rebas>', 'eebis>',  'ebasa>', 'lobas>', 'lebiT>', 'vebis>', 'isTan>', 'debiT>', 'lidan>', 'ridan>', 'ilTan>', 'ianis>', 'ebzec>', 'Tanac>', 'saken>', 'ilisa>',  'ebSic>', 'bodes>']
    di[7] = ['isTvis>', 'saTvis>', 'ebidan>', 'bisgan>',  'isagan>', 'basTan>', 'isadmi>', 'ebulia>', 'ebdnen>',  'bisken>', 'iasTan>', 'Tvisac>', 'deboda>',   'ebamde>', 'ebebis>', 'ebisas>', 'isaken>', 'ebulma>',  'ebinaT>', 'obidan>', 'ebiTac>','ebodes>',  'ebulad>', 'lobaSi>', 'TaTvis>',  'Tvisaa>','asTvis>']
    di[8] = ['ebisTvis>', 'bisaTvis>', 'isTvisac>', 'ebisagan>', 'obisTvis>', 'ebisadmi>', 'lebisgan>', 'isTanave>', 'isTvisaa>', 'ebisaken>']
    di[9] = [] 
    return di





def splitWord(word, di):
    for i in sorted(range(2,9), reverse=True):
        if len(word) < i:
            continue
        suff =  word[-i:]+">"
        
        
        if suff in di[len(suff)]:
            word = word[:len(word)-len(suff)+1]
            #print (suff, word)
        
    return word
    
    
def MakeTrie(words):
    t = Trie()
    for i in words:
        t[i] = True
    return t







    




        

    
            


            
