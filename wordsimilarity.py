def WordSimilarity(word, arr, ngrams = 1, n = 10):
    
    l = []
    c = 0
    for i in arr:
        l.append((distance.jaccard(NGramWord(i,ngrams),NGramWord(word,ngrams)), i))
    
    l.sort()
    return [(x,y) for x, y in l][:n]
    