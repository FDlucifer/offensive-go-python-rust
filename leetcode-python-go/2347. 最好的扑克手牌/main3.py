from typing import List
import collections

ranks = [4,4,2,4,4]
suits = ["d","a","a","b","c"]

def bestHand(ranks: list[int], suits: list[str]) -> str:
    return max(
        [
            (all(suit == suits[0] for suit in suits), 4, "Flush"),
            ((m := max(collections.Counter(ranks).values())) >= 3, 3, "Three of a Kind"),
            (m == 2, 2, "Pair"),
            (m == 1, 1, "High Card")
        ]
    )[2]

print(bestHand(ranks, suits))