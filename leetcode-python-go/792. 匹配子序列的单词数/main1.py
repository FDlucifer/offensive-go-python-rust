from typing import List
from collections import defaultdict

s = "abcde"
words = ["a","bb","acd","ace"]

def numMatchingSubseq(s: str, words: List[str]) -> int:
    p = defaultdict(list)
    for i, w in enumerate(words):
        p[w[0]].append((i, 0))
    ans = 0
    for c in s:
        q = p[c]
        p[c] = []
        for i, j in q:
            j += 1
            if j == len(words[i]):
                ans += 1
            else:
                p[words[i][j]].append((i, j))
    return ans

print(numMatchingSubseq(s, words))