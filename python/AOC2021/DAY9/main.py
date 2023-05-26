import sys
import math

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# G = [[int(c) for c in line.strip()] for line in lines]
G = {(x, y): int(v) for y, line in enumerate(lines) for x, v in enumerate(line.strip())}
Gx = max([x for x, y in G.keys()])
Gy = max([y for x, y in G.keys()])


def get_neigh(p):
    deltas = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    return [
        (p[0] + d[0], p[1] + d[1])
        for d in deltas
        if 0 <= p[0] + d[0] <= Gx and 0 <= p[1] + d[1] <= Gy
    ]


lows = []
for point in G:
    if all([G[p] > G[point] for p in get_neigh(point)]):
        lows.append(point)


p1 = sum([G[p] + 1 for p in lows])
print(f"part 1: {p1}")

basins = [set([p]) for p in lows]
for h in range(9):
    for x in range(Gx + 1):
        for y in range(Gy + 1):
            if G[(x, y)] == h:
                if any([(x, y) in s for s in basins]):
                    continue
                touch = [
                    s for s in basins
                    if any([(nx, ny) in s for nx, ny in get_neigh((x, y))])
                ]
                if len(touch) == 1:
                    touch[0].add((x, y))

p2 = math.prod(sorted([len(s) for s in basins])[-3:])
print(f"part 2: {p2}")
