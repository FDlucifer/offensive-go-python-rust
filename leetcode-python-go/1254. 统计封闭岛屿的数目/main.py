from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            if grid[i][j] == 1:
                return True
            grid[i][j] = 1
            top = dfs(grid, i - 1, j)
            bottom = dfs(grid, i + 1, j)
            left = dfs(grid, i, j - 1)
            right = dfs(grid, i, j + 1)
            return top and bottom and left and right

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 and dfs(grid, i, j):
                    count += 1

        return count



s = Solution()
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
print(s.closedIsland(grid))
