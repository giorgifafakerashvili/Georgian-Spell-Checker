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
