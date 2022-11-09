from typing import List

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]

def countConsistentStrings(allowed: str, words: List[str]) -> int:
    ans=len(words)
    for w in words:
        for c in w:
            if c not in allowed:
                ans-=1
                break
    return ans

print(countConsistentStrings(allowed, words))