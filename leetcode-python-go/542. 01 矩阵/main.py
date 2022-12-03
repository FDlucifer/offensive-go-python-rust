from typing import List
import collections

mat = [[0,0,0],[0,1,0],[1,1,1]]

def updateMatrix(matrix: List[List[int]]) -> List[List[int]]:
    m, n = len(matrix), len(matrix[0])
    dist = [[0] * n for _ in range(m)]
    zeroes_pos = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 0]
    # 将所有的 0 添加进初始队列中
    q = collections.deque(zeroes_pos)
    seen = set(zeroes_pos)

    # 广度优先搜索
    while q:
        i, j = q.popleft()
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                dist[ni][nj] = dist[i][j] + 1
                q.append((ni, nj))
                seen.add((ni, nj))
    
    return dist

print(updateMatrix(mat))