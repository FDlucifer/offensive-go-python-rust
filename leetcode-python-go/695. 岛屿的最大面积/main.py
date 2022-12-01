from typing import List

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

def dfs(grid, cur_i, cur_j) -> int:
    if cur_i < 0 or cur_j < 0 or cur_i == len(grid) or cur_j == len(grid[0]) or grid[cur_i][cur_j] != 1:
        return 0
    grid[cur_i][cur_j] = 0
    ans = 1
    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        next_i, next_j = cur_i + di, cur_j + dj
        ans += dfs(grid, next_i, next_j)
    return ans

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    ans = 0
    for i, l in enumerate(grid):
        for j, n in enumerate(l):
            ans = max(dfs(grid, i, j), ans)
    return ans


print(maxAreaOfIsland(grid))