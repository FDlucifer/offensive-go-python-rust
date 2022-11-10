from typing import List
from collections import deque

grid = ["@.a.#","###.#","b.A.B"]

def shortestPathAllKeys(grid: List[str]) -> int:
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]   # 定义4个方向

    key_to_idx = dict() # 标记钥匙序号：主要作用是用这个序号来做位运算，以此达到钥匙计数和开房间的作用。
    sx = sy = 0     # 标记起点
    m, n = len(grid), len(grid[0])  # 行数，列数

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '@':   # 起点位置，记录到sx, sy变量
                sx, sy = i, j
            elif grid[i][j].islower():  # 是钥匙，记录钥匙的序号，从0开始递增
                idx = len(key_to_idx)
                key_to_idx[grid[i][j]] = idx
    
    dist = dict()   # 记录每个路径状态的步数，路径的状态是指到达某个点时，手中的钥匙状态的最短路径
    q = deque([(sx, sy, 0)])    # 将起点加入队列，起始状态手里没有钥匙，用0表示
    dist[(sx, sy, 0)] = 0   # 起点的步数为0

    while q:
        x, y, mask = q.popleft()    # x, y 为当前搜索的坐标，mask为当前拥有钥匙的状态，钥匙的状态可以理解为当前我们已经拥有了具体的哪几把钥匙。

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#': # 在矩阵里的点并且不是墙的时候，才去做进一步的判断
                if grid[nx][ny] == '.' or grid[nx][ny] == '@':  # 当我们到达的这个点是空房间或者起点时，需要进一步判断
                    if (nx, ny, mask) not in dist:  # 当我们到达这个点时，手里拥有钥匙的状态没有被记录过，那么就需要将这个点记录，并且加入到队列以便后续的搜索
                        dist[(nx, ny, mask)] = dist[(x, y, mask)] + 1   # 到达这个点的步数就是上一个点 +1
                        q.append((nx, ny, mask))    # 加入队列
                elif grid[nx][ny].islower():    # 当这个点是钥匙的时候
                    idx = key_to_idx[grid[nx][ny]]  # 这个钥匙的编号记为idx
                    if (nx, ny, mask | (1 << idx)) not in dist: # 当这个点的状态未被记录时，需要记录一下。mask | (1 << idx) 表示我们拥有了这把钥匙。
                        dist[(nx, ny, mask | (1 << idx))] = dist[(x, y, mask)] + 1
                        if (mask | (1 << idx)) == (1 << len(key_to_idx)) - 1:   # 搜集到了所有的钥匙，返回结果。
                            return dist[(nx, ny, mask | (1 << idx))]
                        q.append((nx, ny, mask | (1 << idx)))
                else:   # 到达点是一把锁
                    idx = key_to_idx[grid[nx][ny].lower()]  # 记录这把锁的钥匙
                    if mask & (1 << idx):   # 只有拥有这把钥匙才能打开这个锁
                        if (nx, ny, mask) not in dist:
                            dist[(nx, ny, mask)] = dist[(x, y, mask)] + 1
                            q.append((nx, ny, mask))

    return -1


print(shortestPathAllKeys(grid))