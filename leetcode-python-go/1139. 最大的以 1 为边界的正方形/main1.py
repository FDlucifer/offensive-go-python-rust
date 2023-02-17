from typing import List

grid = [[1,1,1],[1,0,1],[1,1,1]]


def largest1BorderedSquare(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    limit = min(m, n)

    prefix_2d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix_2d[i][j] = (
                prefix_2d[i][j - 1] + 
                prefix_2d[i - 1][j] -
                prefix_2d[i - 1][j - 1] +
                grid[i - 1][j - 1]
            )
        
    def edge(r1: int, c1: int, r2: int, c2: int) -> int:
        return (
            prefix_2d[r2 + 1][c2 + 1] - 
            prefix_2d[r2 + 1][c1] -
            prefix_2d[r1][c2 + 1] +
            prefix_2d[r1][c1]
        )

    max_val = 0
    for x in range(m):
        for y in range(n):
            if grid[x][y] == 1:
                
                if max_val >= limit - min(x, y) + 1:
                    break

                val = 1
                for r in range(2, limit + 1):
                    nx, ny = x + r - 1, y + r - 1

                    if nx >= m or ny >= n:
                        break
                    
                    a = edge(x, y, x, ny)
                    b = edge(x, y, nx, y)
                    c = edge(x, ny, nx, ny)
                    d = edge(nx, y, nx, ny)

                    if a == b == c == d == r:
                        val = max(val, r)

                max_val = max(max_val, val)

    return max_val * max_val

print(largest1BorderedSquare(grid))