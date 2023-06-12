import sys
from itertools import product

with open(sys.argv[1], "r") as f:
    lines = [x.strip() for x in f.readlines()]

consts = []
for i in range(0, len(lines), 18):
    c1 = int(lines[i + 5].split()[-1])
    c2 = int(lines[i + 15].split()[-1])
    consts.append((c1, c2))


def solve(prod):
    for digits in prod:
        digits = iter(digits)
        pin = [0 if c[0] < 9 else next(digits) for c in consts]
        print(f"\r{''.join([str(x) for x in pin])}", end="")
        z = 0

        for i, w in enumerate(pin):
            c1, c2 = consts[i]
            if c1 > 9:
                z = z * 26 + w + c2
            else:
                pin[i] = (z % 26) + c1
                if not (0 < pin[i] < 10):
                    break
                z = z // 26
        if z == 0:
            return "".join([str(x) for x in pin])


print(f"\rpart 1: {solve(product(range(9,0,-1), repeat=7))}")
print(f"\rpart 2: {solve(product(range(1,10), repeat=7))}")
