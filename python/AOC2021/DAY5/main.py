import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

grid = defaultdict(int)
grid2 = defaultdict(int)
for line in lines:
    p1, p2 = line.split(" -> ")
    p1 = tuple(map(int, p1.split(",")))
    p2 = tuple(map(int, p2.split(",")))

    p1, p2 = sorted([p1, p2])
    if p1[0] == p2[0] or p1[1] == p2[1]:
        for i in range(p1[0], p2[0] + 1):
            for j in range(p1[1], p2[1] + 1):
                grid[(i, j)] += 1
                grid2[(i, j)] += 1

    else:
        slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
        j = p1[1]
        for i in range(p1[0], p2[0] + 1):
            grid2[(i, j)] += 1
            j += slope


part1 = len([coord for coord, num in grid.items() if num > 1])
print(f"part 1: {part1}")

part2 = len([coord for coord, num in grid2.items() if num > 1])
print(f"part 2: {part2}")
