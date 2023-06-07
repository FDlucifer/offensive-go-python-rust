import sys
from functools import lru_cache

with open(sys.argv[1], "r") as f:
    p1, p2 = [int(l.split()[-1]) - 1 for l in f.readlines()]

s1, s2 = 0, 0
rolls = 0

while True:
    rolls += 3
    p1 = (p1 + rolls * 3 - 3) % 10
    s1 += p1 + 1
    if s1 >= 1000:
        print(f"part 1: {rolls * s2}")
        break

    rolls += 3
    p2 = (p2 + rolls * 3 - 3) % 10
    s2 += p2 + 1
    if s2 >= 1000:
        print(f"part 1: {rolls * s1}")
        break

with open(sys.argv[1], "r") as f:
    p1, p2 = [int(l.split()[-1]) - 1 for l in f.readlines()]

s1, s2 = 0, 0
rolls = 0

@lru_cache(maxsize=None)
def turn(p1, s1, p2, s2, player):
    if s1 >= 21:
        return (1, 0)
    elif s2 >= 21:
        return (0, 1)
    w1, w2 = 0, 0
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            for k in [1, 2, 3]:
                if player == 1:
                    np1 = (p1 + i + j + k) % 10
                    ns1 = s1 + np1 + 1
                    nw1, nw2 = turn(np1, ns1, p2, s2, 2)
                    w1 += nw1
                    w2 += nw2
                else:
                    np2 = (p2 + i + j + k) % 10
                    ns2 = s2 + np2 + 1
                    nw1, nw2 = turn(p1, s1, np2, ns2, 1)
                    w1 += nw1
                    w2 += nw2
    return (w1, w2)


print(f"part 2: {max(turn(p1,s1,p2,s2,1))}")
