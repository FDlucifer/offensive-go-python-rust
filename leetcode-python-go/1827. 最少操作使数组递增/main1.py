from typing import List

nums = [1,5,2,4,1]

def minOperations(nums: List[int]) -> int:
    n = len(nums)

    res = 0
    for i in range(1, n):
        if nums[i] <= nums[i - 1]:
            res += nums[i - 1] - nums[i] + 1
            nums[i] = nums[i - 1] + 1

    return res
        

print(minOperations(nums))