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
 