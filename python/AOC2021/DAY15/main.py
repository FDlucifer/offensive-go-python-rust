import sys
from heapq import heappop, heappush


def get_neigh(r, c):
    return [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

G = [[int(l) for l in line.strip()] for line in lines]


def find_short_path(G):
    queue = [(0, (0, 0))]
    locked = set()
    R = len(G)
    C = len(G[0])
    while queue:
        risk, pos = heappop(queue)
        if pos == (R - 1, C - 1):
            return risk
        if pos in locked:
            continue
        locked.add(pos)

        for r, c in get_neigh(*pos):
            if 0 <= r < R and 0 <= c < C:
                heappush(queue, (risk + G[r][c], (r, c)))


print(f"part 1: {find_short_path(G)}")

R = len(G)
C = len(G[0])
R2 = len(G) * 5
C2 = len(G[0]) * 5
G2 = [[0] * C2 for _ in range(R2)]
for r in range(len(G) * 5):
    for c in range(len(G[0]) * 5):
        G2[r][c] = G[r % R][c % C] + c // C + r // R
        if G2[r][c] > 9:
            G2[r][c] -= 9

print(f"part 2: {find_short_path(G2)}")
