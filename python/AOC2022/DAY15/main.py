import sys


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_tuning_freq(sensors):
    for sx, sy, d in sensors:
        for dx in range(d+2):
            dy = d + 1 - dx
            for x, y in [(sx+dx, sy+dy), (sx+dx, sy-dy), (sx-dx, sy+dy), (sx-dx, sy-dy)]:
                if not (0<=x<=4_000_000 and 0<=y<=4_000_000):
                    continue
                if check_point(x, y, sensors):
                    return 4_000_000 * x + y

def check_point(x, y, sensors):
    for sx, sy, d in sensors:
        if dist(x, y, sx, sy) <= d:
            return False
    return True

target_row = 2_000_000
target_row_empty = set()
target_row_beacons = set()
sensors = set()

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

for line in lines:
    toks = line.split(" ")
    sx = int(toks[2][2:-1])
    sy = int(toks[3][2:-1])
    bx = int(toks[8][2:-1])
    by = int(toks[9][2:])
    d = dist(sx, sy, bx, by)
    sensors.add((sx,sy,d))

    y_dist = abs(sy - target_row)
    x_dist = d - y_dist
    for x in range(sx - x_dist, sx + x_dist + 1):
        target_row_empty.add(x)
    if by == target_row:
        target_row_beacons.add(bx)

part1 = len(target_row_empty) - len(target_row_beacons)
print(f"part 1: {part1}")

print(f"part 2: {find_tuning_freq(sensors)}")
