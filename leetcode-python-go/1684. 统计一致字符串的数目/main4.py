from typing import List

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]


def countConsistentStrings(allowed: str, words: list[str]) -> int:
    return sum([len(set(i) - set(allowed)) == 0 for i in words])

print(countConsistentStrings(allowed, words))