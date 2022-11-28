from typing import List
from functools import cache

nums = [9,1,2,3,9]
k = 3

def largestSumOfAverages(nums: List[int], k: int) -> float:
    n = len(nums)
    @cache
    def solve(i: int, k: int) -> float:
        if i == n or k == 0:  # 边界条件
            return float('-inf') if i < n else 0
        else:  # 枚举第k组区间 nums[i,j]
            ret = _sum = 0
            for j in range(i, n):
                _sum += nums[j]
                ret = max(ret, _sum / (j-i+1) + solve(j + 1, k - 1))
            return ret
    return solve(0, k)


print(largestSumOfAverages(nums,k))