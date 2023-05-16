import sys
from functools import cmp_to_key


def compare(p1, p2):
    if isinstance(p1, int) and isinstance(p2, int):
        if p1 < p2:
            return -1
        if p1 == p2:
            return 0
        return 1

    if isinstance(p1, int):
        p1 = [p1]
    if isinstance(p2, int):
        p2 = [p2]
    for x1, x2 in zip(p1, p2):
        res = compare(x1, x2)
        if res == 0:
            continue
        return res

    if len(p1) < len(p2):
        return -1
    if len(p2) < len(p1):
        return 1
    return 0


with open(sys.argv[1], "r") as f:
    data = f.read().strip()

part1 = 0
for i, pair in enumerate(data.split("\n\n")):
    p1, p2 = list(map(eval, pair.split("\n")))
    if compare(p1, p2) == -1:
        part1 += i + 1


print(f"part 1: {part1}")

lines = [eval(line) for line in data.split("\n") if line]
lines.extend([[[2]], [[6]]])

part2 = 1
for i, line in enumerate(sorted(lines, key=cmp_to_key(compare))):
    if line in [[[2]], [[6]]]:
        part2 *= i + 1

print(f"part 2: {part2}")
