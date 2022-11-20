from typing import List

n = 50

def soupServings(n: int) -> float:
    n = (n + 24) // 25
    if n >= 179:
        return 1.0
    dp = [[0.0] * (n + 1) for _ in range(n + 1)]
    dp[0] = [0.5] + [1.0] * n
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][max(0, j - 1)] +
                        dp[max(0, i - 2)][max(0, j - 2)] + dp[max(0, i - 1)][max(0, j - 3)]) / 4
    return dp[n][n]


print(soupServings(n))