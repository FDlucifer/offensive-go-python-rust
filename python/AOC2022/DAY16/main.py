import sys
from functools import cache


@cache
def solve(pos, time, opened, ele_wait=False):
    if time == 0:
        if ele_wait:
            return solve("AA", 26, opened)
        return 0
    score = max(solve(n, time - 1, opened, ele_wait) for n in maps[pos])

    if flows[pos] > 0 and pos not in opened:
        new_opened = set(opened)
        new_opened.add(pos)
        score = max(
            score,
            (time - 1) * flows[pos]
            + solve(pos, time - 1, frozenset(new_opened), ele_wait),
        )
    return score


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

flows = {}
maps = {}

for line in lines:
    toks = line.split(" ")
    valve = toks[1]
    flows[valve] = int(toks[4].split("=")[1].strip(";"))
    maps[valve] = [t.strip(",\n") for t in toks[9:]]

part1 = solve("AA", 30, frozenset())
print(f"part 1: {part1}")

part2 = solve("AA", 26, frozenset(), True)
print(f"part 2: {part2}")
