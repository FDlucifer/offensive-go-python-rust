#!/usr/bin/env python3

import sys
from collections import deque
from functools import cache


@cache
def get_storms(t):
    current = set()
    for r, row in enumerate(lines[1:-1]):
        for c, char in enumerate(row[1:-1]):
            if char in "<v>^":
                dr, dc = DIRS[char]
                current.add(((r + dr * t) % numr, (c + dc * t) % numc))
    return current


DIRS = {"<": (0, -1), "v": (1, 0), ">": (0, 1), "^": (-1, 0)}

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# parse input
numr = len(lines) - 2  # not counting walls
numc = len(lines[0]) - 3  # not counting walls and trailing \n
start = (-1, lines[0].index(".") - 1)
end = (numr, lines[-1].index(".") - 1)

# bfs
queue = deque()
# state = (time, me_r, me_c, leg)
queue.append((0, *start, 0))
seen = set()
part1, part2 = None, None

while not part2:
    t, r, c, leg = queue.popleft()
    if (t, r, c, leg) in seen:
        continue
    seen.add((t, r, c, leg))

    # check for moves
    storms = get_storms(t + 1)
    if (r, c) not in storms:
        queue.append((t + 1, r, c, leg))
    for dr, dc in DIRS.values():
        # if can reach the end and it's leg 0 or 2, do it
        if (r + dr, c + dc) == end and leg in [0, 2]:
            if leg == 0:
                if not part1:
                    part1 = t + 1
                    print(f"Part 1: {part1}")
                queue.append((t + 1, r + dr, c + dc, 1))
            else:
                part2 = t + 1
                break
        # if can reach the start and it's leg 1, do it
        elif (r + dr, c + dc) == start and leg == 1:
            queue.append((t + 1, *start, 2))
            break
        # check for points in bounds that can be moved to
        elif 0 <= r + dr < numr and 0 <= c + dc < numc:
            if (r + dr, c + dc) not in storms:
                queue.append((t + 1, r + dr, c + dc, leg))

print(f"Part 2: {part2}")
