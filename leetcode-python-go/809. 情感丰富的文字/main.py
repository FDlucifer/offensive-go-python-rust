from typing import List

S = "heeellooo"
words = ["hello", "hi", "helo"]

def expressiveWords(s: str, words: List[str]) -> int:
    def expand(s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                return False
            ch = s[i]
            cnti = 0
            while i < len(s) and s[i] == ch:
                cnti += 1
                i += 1
            cntj = 0
            while j < len(t) and t[j] == ch:
                cntj += 1
                j += 1
            
            if cnti < cntj:
                return False
            if cnti != cntj and cnti < 3:
                return False
        
        return i == len(s) and j == len(t)
    
    return sum(int(expand(s, word)) for word in words)



print(expressiveWords(S, words))