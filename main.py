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

class GeoNLP:
    alphabet = {
            u'ა' : 'a', 
            u'ბ' : 'b',
            u'გ' : 'g',
            u'დ' : 'd',
            u'ე' : 'e',
            u'ვ' : 'v',
            u'ზ' : 'z',
            u'თ' : 'T',
            u'ი' : 'i',
            u'კ' : 'k',
            u'ლ' : 'l',
            u'მ' : 'm',
            u'ნ' : 'n',
            u'ო' : 'o',
            u'პ' : 'p',
            u'ჟ' : 'J',
            u'რ' : 'r',
            u'ს' : 's',
            u'ტ' : 't',
            u'უ' : 'u',
            u'ფ' : 'f',
            u'ქ' : 'q',
            u'ღ' : 'R',
            u'ყ' : 'y',
            u'შ' : 'S',
            u'ჩ' : 'C',
            u'ც' : 'c',
            u'ძ' : 'Z',
            u'წ' : 'w',
            u'ჭ' : 'W',
            u'ხ' : 'x',
            u'ჯ' : 'j',
            u'ჰ' : 'h'
            } 
            
    def getChar(self, char):
        char = unicode(char)
        if GeoNLP.alphabet.get(char, True) == True:
            return char
        return GeoNLP.alphabet[char]
    
    def getLetters(self, f = True):
        if f:
            return self.alphabet.values()
        else:
            return self.alphabet.keys()
    

     
def getWords(path):
    arr = [] 
    with open(path) as f:
        for line in f:
            arr.append(line[:-1])
    return arr
    


def NGramWord(word, n = 1):
    arr = []
    word = "<"+word+">"
    for i in range(len(word)-n+1):
        s = ""
        for j in range(n):
            s+=word[i+j]
        arr.append(s)
    return arr
    

 
def NGramFrequency(words, n = 2):
    arr = [] 
    for i in words:
        for j in NGramWord(i, n):
            arr.append(j)
    try:
        freqDist = nltk.FreqDist(arr)
    except Exception,e:
        freqDist = []
    return freqDist
    




def writeFreqInFile(freqDist, path, counter = True, count = 0):
    try:
        f = open(path,"w")
    except Exception,e:
        print "Error while opening file " + str(e)
        return
        
    try:
        for i in freqDist.keys():                
            if freqDist[i] > count:
                if counter is True:    
                    f.write(i + " " + str(freqDist[i])+"\n")
                else:
                    f.write(i+"\n")
    except Exception,e:
        print e




def WriteNormalizeFrequency(freqDist, path):
    s = sum(freqDist[i] for i in freqDist.keys())
    try:
        f = open(path, "w")
    except Exception,e:
        print "Error while opening the file"
        return
    
    for i in freqDist.keys():
        f.write(i + " " + str(freqDist[i]/s)+"\n")

     
def ReadFrequency(path):
    di = {}
    try:
        with open(path) as f:
            for line in f:
                arr = line.split()
                di[arr[0]] = float(arr[1])
    except Exception, e:
        print "Error " + str(e)
    return di


def InsertFreqIntoDict(freqDist, di):
    for i in freqDist.keys():
        di[i] = freqDist[i]
        

def NormalizeDict(di, ret = False):
    d = {} 
    try:
        s = sum([x for x in di.values()])
    except Exception, e:
        print "Error"
        return
    for i in di.keys():
        di[i] = di[i]/s
    

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



def MakeWordDict(words):
    di = {} 
    for i in words:
        di[i] = True
    return di


def In(dictionary, word):
    if dictionary.get(word) is True:
        return True
    return False
    



class BuildIndex:
    
    def __init__(self, words = []):
        self.word_key = {}
        self.index  = {}
        counter = 1
        for i in words:
            self.word_key[i] = counter
            counter+=1
        self.key_word = dict((v,k) for k, v in self.word_key.iteritems())
        
    def process(self,n = 2):
        for i in self.word_key.keys():
            for j in  NGramWord(i,n):
                if self.index.get(j):
                    self.index[j].add(self.word_key[i])
                else:
                    self.index[j] = set()
                    self.index[j].add(self.word_key[i])
                    
        
    def getLength(self,ngram):
        if self.index.get(ngram) is not None:
            return len(self.index.get(ngram))
        else:
            return 0
    
    def getWords(self, ngram):
        arr = []
        if self.index.get(ngram) is not None:
            for i in self.index.get(ngram): 
                arr.append(self.key_word[i])
        return arr
        
    def getInterSection(self, words):
        if len(words) == 0:
            return []
        
        s = set(self.getWords(words[0]))     
        for i in range(1, len(words)):
            s = s & set(self.getWords(words[i]))
        return list(s)
        
    
    def getUnion(self, words, f = True):
        arr = []
        for i in words:
            arr+=self.getWords(i)
        if f:
            freq = nltk.FreqDist(arr)
            return freq.keys()
        else:
            return list(set(arr))



class Trie:

    def __init__(self):
        self.path = {}
        self.value = None
        self.value_valid = False

    def __setitem__(self, key, value):
        current = self
        
        for letter in key:
            if letter not in current.path:
                current.path[letter] = Trie()
            current = current.path[letter]
        
        
        
        current.value_valid = True
        current.value = value
            

    def __delitem__(self, key):
        head = key[0]
        if head in self.path:
            node = self.path[head]
            if len(key) > 1:
                remains = key[1:]
                node.__delitem__(remains)
            else:
                node.value_valid = False
                node.value = None
            if len(node) == 0:
                del self.path[head]
    
    
  
                    

    def __getitem__(self, key):
        
        current = self                
        for letter in key:
            
            if letter in current.path:
                current = current.path[letter]
            else:
                return 0
        
        if current.value_valid:
            return current.value
        else:
            return 0

    def __contains__(self, key):
        if self.__getitem__(key):
            return True
        return False
        

    def __len__(self):
        n = 1 if self.value_valid else 0
        for k in self.path.keys():
            n = n + len(self.path[k])
        return n

    def get(self, key, default=None):
        
        if self.__getitem__(key):
            return self.__getitem__(key)
        else:
            return default
        

    def nodeCount(self):
        n = 0
        for k in self.path.keys():
            n = n + 1 + self.path[k].nodeCount()
        return n

    def keys(self, prefix=[]):
        return self.__keys__(prefix)
        

    def __keys__(self, prefix=[], seen=[]):
        result = []
        if self.value_valid:
            isStr = True
            val = ""
            for k in seen:
                if type(k) != str or len(k) > 2:
                    isStr = False
                    break
                else:
                    val += k
            if isStr:
                result.append(val)
            else:
                result.append(prefix)
        if len(prefix) > 0:
            head = prefix[0]
            prefix = prefix[1:]
            if head in self.path:
                nextpaths = [head]
            else:
                nextpaths = []
        else:
            nextpaths = self.path.keys()                
        for k in nextpaths:
            nextseen = []
            nextseen.extend(seen)
            nextseen.append(k)
            result.extend(self.path[k].__keys__(prefix, nextseen))
        return result
        
        
    def __iter__(self):
        for k in self.keys():
            yield k
        raise StopIteration



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
    


class hybernate:
    vowels = ["a","e", "i", "o", "u"]
    
    def __init__(self, string):
        if len([x for x in string if x in hybernate.vowels]) <= 1:
            self.text = [string]
        else:            
            self.string = string
            self.ans = []
            self.text = ""
            self.f(string)
            self.g()
        
    
    
    def f(self,string):
        
        if len(string) < 2:
            return
        splites = [[string[:i], string[i:]] for i in range(len(string)+1)][2:-2]
        splites = filter(lambda x: len(set(x[0]) & set(hybernate.vowels)) and len(set(x[1]) & set(hybernate.vowels)), splites)
            
        
        for x,y in splites:
            if x[-1] not in hybernate.vowels and y[0] in hybernate.vowels and y[1] not in  hybernate.vowels:
                splites.remove([x,y])
                continue
                
            if x[-2] == x[-1]:
                splites.remove([x,y])
                continue
                
            if len(y) >= 2:
                if y[0] == y[1]:
                    splites.remove([x,y])
                    
                    
        if len(splites) > 0:
            self.ans.append(splites[0])
            if splites == []:
                return
            else:
                self.f(splites[0][1])
    
    
    def g(self):
        if len(self.ans) > 0:
            for i in range(len(self.ans)):
                if i == len(self.ans) - 1:
                    self.text += self.ans[i][0] + "-" + self.ans[i][1]
                else:
                    self.text += self.ans[i][0] + "-"
    
    def get(self):
        return self.text
        
    def getlist(self):
        try:
            return self.text.split("-")
        except AttributeError:
            return self.text
    

    
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



class WordGenerator:
    
    letters = GeoNLP().getLetters()
    
    def __init__(self, word = ""):
        self.word = word
    
    def splites(self):
        return [(self.word[:i], self.word[i:]) for i in range(len(self.word)+1)]
        
    def deletes(self):
        arr = [] 
        for i in range(len(self.word)):
            w = self.word[:i] + self.word[i+1:]
            arr.append(w)
        return arr
     
    def add(self):
        arr = [] 
        for i in range(len(self.word)+1):
            for char in WordGenerator.letters:
                ad = self.word[:i] + char + self.word[i:]
                arr.append(ad)
        return arr
    
    def changes(self):
        arr = [] 
        for i in range(len(self.word)):
            for char in WordGenerator.letters:
                ch = self.word[:i] + char + self.word[i+1:]
                if ch != self.word:                
                    arr.append(ch)
        return arr
    
    def transposes(self):
        arr = [] 
        for i in range(len(self.word)-1):
            t =  self.word[:i] + self.word[i+1] + self.word[i] + self.word[i+2:]
            arr.append(t)
        return arr
    
    def deleteNGrams(self, n = 2):
        arr = [] 
        for i in range(len(self.word)-n+1):
            d = self.word[:i] + self.word[i+n:]
            arr.append(d)
        return arr
        
    
    def transposeNGrams(self, n = 2):
        arr = [] 
        for i in range(len(self.word)-(2*n)+1):
            t = self.word[:i] + self.word[i+n:i+2*n] + self.word[i:i+n] + self.word[i+2*n:]
            arr.append(t)
        return arr
    
    def all(self, f = True):
        arr = []
        #map(lambda x: arr.append(x), self.transposes())
        map(lambda x: arr.append(x), self.add())        
        map(lambda x: arr.append(x), self.deletes())
        map(lambda x: arr.append(x), self.changes())
           
         
        map(lambda x: arr.append(x), self.transposeNGrams(1))
        map(lambda x: arr.append(x), self.transposeNGrams(2))
        map(lambda x: arr.append(x), self.transposeNGrams(3))
        
        if f:
            return list(set(arr))
        else:
            return arr
    


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







    




        

    
            


            
