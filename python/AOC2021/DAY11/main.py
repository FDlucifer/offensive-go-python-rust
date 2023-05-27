import sys

def flash(r,c):
    cnt = 1
    G[r][c] = 0
    for dr in [-1,0,1]:
        for dc in [-1,0,1]:
            if 0 <= r + dr < 10 and 0 <= c + dc < 10 and G[r+dr][c+dc] != 0:
                G[r+dr][c+dc] += 1
                if G[r+dr][c+dc] > 9:
                    cnt += flash(r+dr, c+dc)
    return cnt

with open(sys.argv[1], 'r') as f:
    G = [[int(i) for i in line.strip()] for line in f.readlines()]

num_flashes = 0
t = 0
while True:
    new_flashes = 0
    if t == 100:
        print(f"part 1: {num_flashes}")
    for r in range(10):
        for c in range(10):
            G[r][c] += 1
    for r in range(10):
        for c in range(10):
            if G[r][c] > 9:
                new_flashes += flash(r,c)
    num_flashes += new_flashes
    t += 1
    if new_flashes == 100:
        print(f"part 2: {t}")
        break
