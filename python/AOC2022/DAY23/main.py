#!/usr/bin/env python3

import sys
from collections import defaultdict


def score(elves):
    minr = min(r for r, c in elves)
    maxr = max(r for r, c in elves)
    minc = min(c for r, c in elves)
    maxc = max(c for r, c in elves)

    return (maxr - minr + 1) * (maxc - minc + 1) - len(elves)


with open(sys.argv[1], "r") as f:
    lines = f.readlines()


moves = [
    ((-1, -1), (-1, 0), (-1, 1)),  # N
    ((1, -1), (1, 0), (1, 1)),  # S
    ((-1, -1), (0, -1), (1, -1)),  # W
    ((-1, 1), (0, 1), (1, 1)),  # E
]

elves = set()
num_elves = 0
for r, row in enumerate(lines):
    for c, char in enumerate(row):
        if char == "#":
            elves.add((r, c))
            num_elves += 1


round = 0
while True:
    next_moves = defaultdict(list)
    # for each elf
    for r, c in elves:

        # check if no neighbors
        if (
            sum(
                [
                    sum([1 for dr in range(-1, 2) if (r + dr, c + dc) in elves])
                    for dc in range(-1, 2)
                ]
            )
            == 1
        ):
            continue

        # check for next move
        for m in range(4):
            potential_move = moves[(m + round) % 4]
            if sum(1 for dr, dc in potential_move if (r + dr, c + dc) in elves) == 0:
                next_moves[(r + potential_move[1][0], c + potential_move[1][1])].append(
                    (r, c)
                )
                break

    # execute moves
    for move_to, move_from in next_moves.items():
        if len(move_from) == 1:
            elves.add(move_to)
            elves.remove(move_from[0])

    # increment round, check for solutions
    round += 1
    if round == 10:
        part1 = score(elves)
        print(f"Part 1: {part1}")

    if len(next_moves) == 0:
        break


part2 = round
print(f"Part 2: {part2}")
