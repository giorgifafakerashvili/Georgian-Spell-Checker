class Suffixes:
    
    @staticmethod
    def prefixes(arr):
        return filter(lambda x: len(x) > 0 and x[0] == "<", arr)
        
        
    
    @staticmethod
    def suffixes(arr):
        return filter(lambda x: len(x) > 0 and x[-1] == ">", arr)