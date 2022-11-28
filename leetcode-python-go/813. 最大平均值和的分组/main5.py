from typing import List
import itertools

nums = [9,1,2,3,9]
k = 3

def largestSumOfAverages(nums: List[int], k: int) -> float:
    n = len(nums)
    f = [[float("-inf")] * (k + 1) for _ in range(n + 1)]
    f[0][0] = 0
    pre = [0] + list(itertools.accumulate(nums))
    for i in range(n):
        for j in range(1, k + 1):
            for kk in range(i + 1):
                f[i + 1][j] = max(f[i + 1][j], f[kk][j - 1] + (pre[i + 1] - pre[kk]) / (i - kk + 1))
    return f[n][k]


print(largestSumOfAverages(nums,k))