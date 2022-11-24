from typing import List

nums = [2,9,2,5,6]
left = 2
right = 8

def numSubarrayBoundedMax(nums: List[int], left: int, right: int) -> int:
    def count(lower: int) -> int:
        res = cur = 0
        for x in nums:
            if x <= lower:
                cur += 1
            else:
                cur = 0
            res += cur
        return res
    return count(right) - count(left - 1)


print(numSubarrayBoundedMax(nums, left, right))