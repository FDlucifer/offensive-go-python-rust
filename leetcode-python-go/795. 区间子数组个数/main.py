from typing import List

nums = [2,9,2,5,6]
left = 2
right = 8

def numSubarrayBoundedMax(nums: List[int], left: int, right: int) -> int:
    res = 0
    last2 = last1 = -1
    for i, x in enumerate(nums):
        if left <= x <= right:
            last1 = i
        elif x > right:
            last2 = i
            last1 = -1
        if last1 != -1:
            res += last1 - last2
    return res


print(numSubarrayBoundedMax(nums, left, right))