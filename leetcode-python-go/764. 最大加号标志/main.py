from typing import List

n = 5
mines = [[4, 2]]

def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:
    dp = [[n] * n for _ in range(n)]
    banned = set(map(tuple, mines))
    for i in range(n):
        # left
        count = 0
        for j in range(n):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = min(dp[i][j], count)
        # right
        count = 0
        for j in range(n - 1, -1, -1):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = min(dp[i][j], count)
    for j in range(n):
        # up
        count = 0
        for i in range(n):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = min(dp[i][j], count)
        # down
        count = 0
        for i in range(n - 1, -1, -1):
            count = 0 if (i, j) in banned else count + 1
            dp[i][j] = min(dp[i][j], count)
    return max(map(max, dp))


print(orderOfLargestPlusSign(n, mines))