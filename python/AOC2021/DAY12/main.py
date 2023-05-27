import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

paths = defaultdict(list)

for line in lines:
    a, b = line.strip().split("-")
    if a != "end" and b != "start":
        paths[a].append(b)
    if b != "end" and a != "start":
        paths[b].append(a)


def walk(visited):
    if visited[-1] == "end":
        return 1

    count = 0
    for cave in paths[visited[-1]]:
        if not cave in visited or cave.upper() == cave:
            count += walk(visited + [cave])

    return count


print(f"part 1: {walk(['start'])}")


def walk2(visited, small_done):
    if visited[-1] == "end":
        return 1

    count = 0
    for cave in paths[visited[-1]]:
        if cave.upper() == cave:
            count += walk2(visited + [cave], small_done)
        else:
            times_visited = len([n for n in visited if n == cave])
            if times_visited == 0:
                count += walk2(visited + [cave], small_done)
            elif not small_done:
                count += walk2(visited + [cave], True)
    return count


print(f"part 2: {walk2(['start'], False)}")
