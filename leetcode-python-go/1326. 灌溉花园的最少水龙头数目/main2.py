from typing import List
from numpy import inf

n = 5
ranges = [3,4,1,1,0,0]

def minTaps(n: int, ranges: List[int]) -> int:
    # nums: 每个位置最大跳跃长度
    nums = [0] * (n + 1)
    for i in range(n + 1):
        l, r = max(0, i - ranges[i]), i + ranges[i]
        nums[l] = max(nums[l], r - l)
        nums[i] = max(nums[i], r - i)
    
    step = 1 
    ne = 0 # 下一次可以跳的最远位置
    cur = nums[0] # 本次可以跳的最远位置
    for i in range(n):
        if i > cur: return -1 # 无法跳跃
        ne = max(ne, i + nums[i])
        if i == cur: 
            cur = ne
            step += 1
    return step if cur >= n else -1 # 判断下无法到达终点


print(minTaps(n, ranges))