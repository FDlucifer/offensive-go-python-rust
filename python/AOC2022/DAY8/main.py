import sys

def is_visible(grid, r, c):
    if c == 0 or c == C-1 or r == 0 or r == R-1:
        return 1
    # look left:
    if all(grid[r][cc] < grid[r][c] for cc in range(c)):
        return 1
    # look right
    if all(grid[r][cc] < grid[r][c] for cc in range(c+1, C)):
        return 1
    # look up
    if all(grid[rr][c] < grid[r][c] for rr in range(r)):
        return 1
    # look down
    if all(grid[rr][c] < grid[r][c] for rr in range(r+1, R)):
        return 1
    return 0

def scenic_score(grid, r, c):
    if c == 0 or c == C-1 or r == 0 or r == R-1:
        return 0

    for dc in range(1, c+1):
        if grid[r][c - dc] >= grid[r][c]:
            break
    left = dc

    for dc in range(1, C - c):
        if grid[r][c + dc] >= grid[r][c]:
            break
    right = dc

    for dr in range(1, r+1):
        if grid[r - dr][c] >= grid[r][c]:
            break
    top = dr

    for dr in range(1, R - r):
        if grid[r + dr][c] >= grid[r][c]:
            break
    bottom = dr
    return left * right * top * bottom

with open(sys.argv[1], "r") as f:
    grid = [list(map(int, line.strip())) for line in f.readlines()]

R = len(grid)
C = len(grid[0])

part1 = 0
part2 = 0
for r in range(R):
    for c in range(C):
        part1 += is_visible(grid, r, c)
        part2 = max(part2, scenic_score(grid, r, c))

print(f"part 1: {part1}")
print(f"part 2: {part2}")
