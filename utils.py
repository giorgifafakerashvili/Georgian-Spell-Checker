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
    
def MakeWordDict(words):
    di = {} 
    for i in words:
        di[i] = True
    return di


def In(dictionary, word):
    if dictionary.get(word) is True:
        return True
    return False
    