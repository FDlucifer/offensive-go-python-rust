from typing import List
from functools import lru_cache

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(i, j):
            res = 1
            for x, y in [[i-1, j+1], [i, j+1], [i+1, j+1]]:
                if 0<=x<m and 0<=y<n and grid[x][y] > grid[i][j]:
                    res = max(res, 1+dfs(x, y))
            return res

        return max(dfs(i, 0) for i in range(m))-1


# 示例测试
solution = Solution()
grid1 = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
grid2 = [[3,2,4],[2,1,9],[1,1,7]]
print(solution.maxMoves(grid1))  # 输出: 3
print(solution.maxMoves(grid2))  # 输出: 0
