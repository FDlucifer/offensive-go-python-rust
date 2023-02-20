from typing import List
from collections import Counter

ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]

def bestHand(ranks: List[int], suits: List[str]) -> str:

    if len(set(suits)) == 1:
        return 'Flush'

    counter = Counter(ranks)

    if len(counter) == 5:
        return 'High Card'
    
    if any(cnt >= 3 for cnt in counter.values()):
        return 'Three of a Kind'

    return 'Pair'

print(bestHand(ranks, suits))