from typing import List

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]

def countConsistentStrings(allowed: str, words: List[str]) -> int:
    return sum(all([c in allowed for c in w]) for w in words)

print(countConsistentStrings(allowed, words))