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