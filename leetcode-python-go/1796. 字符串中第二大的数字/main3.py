s = "dfa12321afd"

def secondHighest(s: str) -> int:
    u1 = u2 = -1
    for c in map(int, filter(str.isdigit, s)):
        if u1 < c:
            u1, u2 = c, u1
        elif u1 != c and u2 < c:
            u2 = c
    return u2

print(secondHighest(s))