import sys

with open(sys.argv[1], "r") as f:
    grid = [list(line.strip()) for line in f.readlines()]


R = len(grid)
C = len(grid[0])

t = 0
while True:
    next_grid = [row[:] for row in grid]
    for r in range(R):
        for c in range(C):
            if grid[r][c] == ">" and grid[r][(c + 1) % C] == ".":
                next_grid[r][(c + 1) % C] = ">"
                next_grid[r][c] = "."
    next_grid2 = [row[:] for row in next_grid]
    for r in range(R):
        for c in range(C):
            if next_grid[r][c] == "v" and next_grid[(r + 1) % R][c] == ".":
                next_grid2[(r + 1) % R][c] = "v"
                next_grid2[r][c] = "."

    t += 1
    if grid == next_grid2:
        break
    grid = next_grid2

print(f"part 1: {t}")
