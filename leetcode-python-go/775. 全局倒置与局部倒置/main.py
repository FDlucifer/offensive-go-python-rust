from typing import List

nums = [1,0,2]

def isIdealPermutation(nums: List[int]) -> bool:
    min_suf = nums[-1]
    for i in range(len(nums) - 2, 0, -1):
        if nums[i - 1] > min_suf:
            return False
        min_suf = min(min_suf, nums[i])
    return True

print(isIdealPermutation(nums))