import sys


def solve(lines, part2=False):
    # parse input
    grid = set()
    for line in lines:
        points = line.split(" -> ")
        prev = None
        for point in points:
            c, r = list(map(int, point.split(",")))
            if prev:
                if c - prev[0]:
                    for i in range(min(c, prev[0]), max(c, prev[0]) + 1):
                        grid.add((i, r))
                elif r - prev[1]:
                    for i in range(min(r, prev[1]), max(r, prev[1]) + 1):
                        grid.add((c, i))
                else:
                    assert False
            prev = (c, r)

    last_row = max(g[1] for g in grid)

    # drop sand
    num = 0
    while True:
        sand = (500, 0)
        while True:
            if (sand[0], sand[1] + 1) not in grid:
                sand = (sand[0], sand[1] + 1)
            elif (sand[0] - 1, sand[1] + 1) not in grid:
                sand = (sand[0] - 1, sand[1] + 1)
            elif (sand[0] + 1, sand[1] + 1) not in grid:
                sand = (sand[0] + 1, sand[1] + 1)
            else:
                grid.add(sand)
                break
            if sand[1] == last_row + 1:
                if not part2:
                    return num
                grid.add(sand)
                break
        num += 1
        if sand == (500, 0):
            return num


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

part1 = solve(lines)
print(f"part 1: {part1}")

part2 = solve(lines, part2=True)
print(f"part 2: {part2}")
