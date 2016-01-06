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
  