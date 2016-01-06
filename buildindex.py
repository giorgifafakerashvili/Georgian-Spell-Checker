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

