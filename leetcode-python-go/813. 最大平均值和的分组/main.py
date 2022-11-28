from typing import List
import itertools

nums = [9,1,2,3,9]
k = 3

def largestSumOfAverages(nums: List[int], k: int) -> float:
    n = len(nums)
    prefix = list(itertools.accumulate(nums, initial=0))
    dp = [[0.0] * (k + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i][1] = prefix[i] / i
    for j in range(2, k + 1):
        for i in range(j, n + 1):
            for x in range(j - 1, i):
                dp[i][j] = max(dp[i][j], dp[x][j - 1] + (prefix[i] - prefix[x]) / (i - x))
    return dp[n][k]


print(largestSumOfAverages(nums,k))