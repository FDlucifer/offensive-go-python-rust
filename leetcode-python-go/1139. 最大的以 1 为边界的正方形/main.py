grid = [[1,1,1],[1,0,1],[1,1,1]]

def largest1BorderedSquare(grid):
    m, n = len(grid), len(grid[0])
    left = [[0] * (n + 1) for _ in range(m + 1)]
    up = [[0] * (n + 1) for _ in range(m + 1)]
    maxBorder = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if grid[i - 1][j - 1]:
                left[i][j] = left[i][j - 1] + 1
                up[i][j] = up[i - 1][j] + 1
                border = min(left[i][j], up[i][j])
                while left[i - border + 1][j] < border or up[i][j - border + 1] < border:
                    border -= 1
                maxBorder = max(maxBorder, border)
    return maxBorder ** 2

print(largest1BorderedSquare(grid))