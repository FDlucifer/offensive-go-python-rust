import sys
from collections import Counter
import json
import math

with open(sys.argv[1], "r") as f:
    data = f.read().strip()

# read in data
scanners = []
for raw_scanner_data in data.split("\n\n"):
    scanners.append(
        [tuple(map(int, line.split(","))) for line in raw_scanner_data.split("\n")[1:]]
    )

# generate orientations
def orient_point(x, y, z):
    return [
        (x, y, z),
        (z, y, -x),
        (-x, y, -z),
        (-z, y, x),
        (-y, x, z),
        (z, x, y),
        (y, x, -z),
        (-z, x, -y),
        (y, -x, z),
        (z, -x, -y),
        (-y, -x, -z),
        (-z, -x, y),
        (x, -z, y),
        (y, -z, -x),
        (-x, -z, -y),
        (-y, -z, x),
        (x, -y, -z),
        (-z, -y, -x),
        (-x, -y, z),
        (z, -y, x),
        (x, z, -y),
        (-y, z, -x),
        (-x, z, y),
        (y, z, x),
    ]


def generate_orientations(scanner):
    return list(zip(*[orient_point(*p) for p in scanner]))


# solve problem
def find_overlap(known, scanners):
    for scanner in scanners:
        for orientation in generate_orientations(scanner):
            distances = Counter()
            for p1 in known:
                for p2 in orientation:
                    distances[str([a - b for a, b in zip(p1, p2)])] += 1
            most_common = distances.most_common(1)[0]
            if most_common[1] >= 12:
                off = json.loads(most_common[0])
                return (
                    scanner,
                    [(x + off[0], y + off[1], z + off[2]) for x, y, z in orientation],
                    off,
                )


known = set(scanners[0])
scanners = scanners[1:]
scanner_locations = [[0, 0, 0]]
while scanners:
    found_scanner, found_orient, offset = find_overlap(known, scanners)
    for m in found_orient:
        known.add(m)
    scanners.remove(found_scanner)
    scanner_locations.append(offset)

print(f"part 1: {len(known)}")

max_dist = 0
for i in range(len(scanner_locations)):
    for j in range(len(scanner_locations)):
        if i < j:
            max_dist = max(
                sum(
                    [
                        abs(x - y)
                        for x, y in zip(scanner_locations[i], scanner_locations[j])
                    ]
                ),
                max_dist,
            )

print(f"part 2: {max_dist}")
