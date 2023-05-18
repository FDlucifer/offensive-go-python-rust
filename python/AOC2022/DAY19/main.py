import sys
import re
from collections import deque
import math


def solve(blueprint, t):
    raw_costs = list(map(int, re.findall(r"\d+", blueprint)))
    costs = (
        (raw_costs[1], 0, 0, 0),
        (raw_costs[2], 0, 0, 0),
        (raw_costs[3], raw_costs[4], 0, 0),
        (raw_costs[5], 0, raw_costs[6], 0),
    )

    queue = deque()
    queue.append((t, (0, 0, 0, 0), (1, 0, 0, 0)))
    seen = set()
    best = 0
    max_spend = [max(cost[i] for cost in costs) for i in range(4)]

    while queue:
        t, stuff, robots = queue.popleft()
        min_geodes_left = stuff[3] + (t * robots[3])
        if min_geodes_left > best:
            best = min_geodes_left

        if t == 0 or (t, stuff, robots) in seen:
            continue
        seen.add((t, stuff, robots))

        for resource in range(4):
            # we have enough of this bot?
            if resource != 3 and robots[resource] >= max_spend[resource]:
                continue

            # do we have the bots to get to where we need to be to build this resource next
            if any(
                robots[rid] == 0 for rid, cost in enumerate(costs[resource]) if cost
            ):
                continue
            wait = max(
                [
                    math.ceil((cost - stuff[rid]) / robots[rid])
                    for rid, cost in enumerate(costs[resource])
                    if cost
                ]
                + [0]
            )

            if t - wait - 1 <= 0:
                continue

            next_stuff = [
                stuff[i] + (robots[i] * (wait + 1)) - costs[resource][i]
                for i in range(4)
            ]
            next_robots = list(robots)
            next_robots[resource] += 1
            for i in range(3):
                next_stuff[i] = min(next_stuff[i], max_spend[i] * (t - wait - 1))

            queue.append((t - wait - 1, tuple(next_stuff), tuple(next_robots)))

    return best


with open(sys.argv[1], "r") as f:
    lines = f.readlines()


part1 = 0
for i, line in enumerate(lines):
    part1 += (i + 1) * solve(line, 24)

print(f"part 1: {part1}")

part2 = 1
for line in lines[:3]:
    part2 *= solve(line, 32)
print(f"part 2: {part2}")
