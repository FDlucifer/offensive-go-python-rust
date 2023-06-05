import sys

with open(sys.argv[1], "r") as f:
    line = f.read()

TXmin, TXmax = list(map(int, line[15:].strip().split(",")[0].split("..")))
TYmin, TYmax = list(map(int, line[15:].strip().split(",")[1].split("=")[1].split("..")))

maxmaxy = 0
good = []
for DX in range(TXmax + 1):
    for DY in range(-100, 1000):
        x, y = 0, 0
        dx, dy = DX, DY
        maxy = 0
        for t in range(TXmax):
            x += dx
            y += dy
            maxy = max(maxy, y)
            dx = max(0, dx - 1)
            dy -= 1
            if TXmin <= x <= TXmax and TYmin <= y <= TYmax:
                maxmaxy = max(maxy, maxmaxy)
                good.append((DX, DY))
                print(DX, DY)
                break
            if x > TXmax:
                break
            if dy < 0 and y < TYmin:
                break

print(f"part 1: {maxmaxy}")
print(f"part 2: {len(good)}")
