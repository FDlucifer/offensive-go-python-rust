from typing import List
from collections import Counter

ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]

def bestHand(ranks: List[int], suits: List[str]) -> str:
    return "Flush" if len(set(suits)) == 1 else "Three of a Kind" if max(Counter(ranks).values()) >= 3 else "Pair" if max(Counter(ranks).values()) >= 2 else "High Card"

print(bestHand(ranks, suits))