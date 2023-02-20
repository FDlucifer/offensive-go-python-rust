from typing import List
from collections import Counter

ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]

def bestHand(ranks: List[int], suits: List[str]) -> str:
    if len(set(suits)) == 1:
        return "Flush"
    h = Counter(ranks)
    if len(h) == 5:
        return "High Card"
    for [a, b] in h.items():
        if b > 2:
            return "Three of a Kind"
    return "Pair"

print(bestHand(ranks, suits))