from typing import List

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]

def countConsistentStrings(allowed: str, words: List[str]) -> int:
    mask = 0
    for c in allowed:
        mask |= 1 << (ord(c) - ord('a'))
    res = 0
    for word in words:
        mask1 = 0
        for c in word:
            mask1 |= 1 << (ord(c) - ord('a'))
        res += (mask1 | mask) == mask
    return res


print(countConsistentStrings(allowed, words))