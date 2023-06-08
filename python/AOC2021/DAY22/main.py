import sys
import re
import math
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

g = set()
for line in lines:
    status, coords = line.split()
    x0, x1, y0, y1, z0, z1 = list(map(int, re.findall("-?\d+", coords)))
    x0 = max(x0, -50)
    x1 = min(x1, 50)
    y0 = max(y0, -50)
    y1 = min(y1, 50)
    z0 = max(z0, -50)
    z1 = min(z1, 50)
    for x in range(x0, x1 + 1):
        for y in range(y0, y1 + 1):
            for z in range(z0, z1 + 1):
                if status == "on":
                    g.add((x, y, z))
                else:
                    g.discard((x, y, z))

print(f"part 1: {len(g)}")


def get_overlap(c1, c2):
    if any(r1[0] > r2[1] or r2[0] > r1[1] for r1, r2 in zip(c1, c2)):
        return None
    return tuple([(max(r1[0], r2[0]), min(r1[1], r2[1])) for r1, r2 in zip(c1, c2)])


cubes = defaultdict(int)
for line in lines:
    status, coords = line.split()
    x0, x1, y0, y1, z0, z1 = list(map(int, re.findall("-?\d+", coords)))
    c_new = ((x0, x1), (y0, y1), (z0, z1))

    new_cubes = defaultdict(int)
    for c in cubes:
        overlap = get_overlap(c_new, c)
        if overlap:
            new_cubes[overlap] -= cubes[c]

    if status == "on":
        new_cubes[c_new] += 1

    for c in new_cubes:
        cubes[c] += new_cubes[c]

total = 0
for c in cubes:
    total += math.prod([r[1] - r[0] + 1 for r in c]) * cubes[c]

print(f"part 2: {total}")
