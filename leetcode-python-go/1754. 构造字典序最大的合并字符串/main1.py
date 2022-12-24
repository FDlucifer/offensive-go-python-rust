word1 = "abcabc"
word2 = "abdcaba"

def largestMerge(word1: str, word2: str) -> str:
    res = ""
    i = j = 0 
    m, n = len(word1), len(word2) 

    while i < m and j < n: 
        if ord(word1[i]) > ord(word2[j]): 
            res += word1[i]
            i += 1 
        elif ord(word1[i]) < ord(word2[j]): 
            res += word2[j]
            j += 1
        else: 
            a = i+1 
            b = j+1  
            while a < m and b < n and word1[a] == word2[b]: 
                a += 1 
                b += 1 
            while a == m and b < n and word1[-1] == word2[b]: 
                b += 1 
            while a < m and b == n and word1[a] == word2[-1]: 
                a += 1 
            while i < m and j < n and word1[i] == word2[j]: 
                if a < m and b < n: 
                    if ord(word1[a]) > ord(word2[b]): 
                        res += word1[i]
                        i += 1 
                    else: 
                        res += word2[j]
                        j += 1 
                elif a == m and b == n: 
                    res += word1[i]
                    i += 1  
                elif a < m: 
                    if ord(word1[a]) > ord(word2[-1]): 
                        res += word1[i]
                        i += 1 
                    else: 
                        res += word2[j]
                        j += 1 
                else: 
                    if ord(word1[-1]) > ord(word2[b]): 
                        res += word1[i]
                        i += 1 
                    else: 
                        res += word2[j]
                        j += 1    

    while i < m: 
        res += word1[i]
        i += 1 
    while j < n: 
        res += word2[j]
        j += 1 
    
    return res 

print(largestMerge(word1, word2))