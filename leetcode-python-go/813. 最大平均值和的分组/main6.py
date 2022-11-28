from typing import List
from itertools import accumulate
from functools import cache

nums = [9,1,2,3,9]
k = 3

def largestSumOfAverages(nums: List[int], k: int) -> float:
    @cache
    def dfs(depth, k): # depth从1开始，返回将nums[depth-1:]分成k份的最大值
        if k == 1:
            max_res = (prefix_sum[-1] - prefix_sum[depth - 1]) / (len(prefix_sum) - depth)
            return max_res
        max_res = -1
        for i in range(depth, len(prefix_sum) - k + 1): # 预留足够的长度，保证能分成k块
            avg = (prefix_sum[i] - prefix_sum[depth - 1]) / (i - depth + 1)
            max_res = max(max_res, avg + dfs(i + 1, k - 1))
        return max_res

    prefix_sum = list(accumulate(nums, initial=0))
    return dfs(1, k)


print(largestSumOfAverages(nums,k))