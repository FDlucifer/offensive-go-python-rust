from typing import List

nums = [1,5,2,4,1]

def minOperations(nums: List[int]) -> int:
    pre = nums[0] - 1
    res = 0
    for i in nums:
        pre = max(pre + 1, i)
        res += pre - i
    return res

print(minOperations(nums))