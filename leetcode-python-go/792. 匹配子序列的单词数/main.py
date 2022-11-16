from typing import List
from collections import defaultdict
from bisect import bisect_right

s = "abcde"
words = ["a","bb","acd","ace"]

def numMatchingSubseq(s: str, words: List[str]) -> int:
    pos = defaultdict(list)
    for i, c in enumerate(s):
        pos[c].append(i)
    ans = len(words)
    for w in words:
        if len(w) > len(s):
            ans -= 1
            continue
        p = -1
        for c in w:
            ps = pos[c]
            j = bisect_right(ps, p)
            if j == len(ps):
                ans -= 1
                break
            p = ps[j]
    return ans

print(numMatchingSubseq(s, words))