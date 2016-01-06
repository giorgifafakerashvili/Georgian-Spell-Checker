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
    
    
def MakeTrie(words):
    t = Trie()
    for i in words:
        t[i] = True
    return t

def splitWord(word, di):
    for i in sorted(range(2,9), reverse=True):
        if len(word) < i:
            continue
        suff =  word[-i:]+">"
        
        
        if suff in di[len(suff)]:
            word = word[:len(word)-len(suff)+1]
            #print (suff, word)
        
    return word

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