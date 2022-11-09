from typing import List
from collections import deque

grid = ["@.a.#","###.#","b.A.B"]

def shortestPathAllKeys(grid: List[str]) -> int:
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    m, n = len(grid), len(grid[0])
    sx = sy = 0
    key_to_idx = dict()
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                sx, sy = i, j
            elif grid[i][j].islower():
                if grid[i][j] not in key_to_idx:
                    idx = len(key_to_idx)
                    key_to_idx[grid[i][j]] = idx

    q = deque([(sx, sy, 0)])
    dist = dict()
    dist[(sx, sy, 0)] = 0
    while q:
        x, y, mask = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
                if grid[nx][ny] == "." or grid[nx][ny] == "@":
                    if (nx, ny, mask) not in dist:
                        dist[(nx, ny, mask)] = dist[(x, y, mask)] + 1
                        q.append((nx, ny, mask))
                elif grid[nx][ny].islower():
                    idx = key_to_idx[grid[nx][ny]]
                    if (nx, ny, mask | (1 << idx)) not in dist:
                        dist[(nx, ny, mask | (1 << idx))] = dist[(x, y, mask)] + 1
                        if (mask | (1 << idx)) == (1 << len(key_to_idx)) - 1:
                            return dist[(nx, ny, mask | (1 << idx))]
                        q.append((nx, ny, mask | (1 << idx)))
                else:
                    idx = key_to_idx[grid[nx][ny].lower()]
                    if (mask & (1 << idx)) and (nx, ny, mask) not in dist:
                        dist[(nx, ny, mask)] = dist[(x, y, mask)] + 1
                        q.append((nx, ny, mask))
    return -1


print(shortestPathAllKeys(grid))