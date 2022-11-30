from collections import Counter

s1 = "ab"
s2 = "eidbaooo"

def checkInclusion(s1: str, s2: str) -> bool:
    start, end = 0, 0
    n2 = len(s2)
    n1 = len(s1)
    while end <= n2:
        while len(s2[start: end]) >= n1:
            if Counter(s2[start: end]) == Counter(s1):
                return True
            start += 1
        end += 1
    return False

print(checkInclusion(s1, s2))