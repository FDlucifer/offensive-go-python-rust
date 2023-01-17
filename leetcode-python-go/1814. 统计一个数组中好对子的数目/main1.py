from typing import List
from collections import Counter

nums = [13,10,35,24,76]

def countNicePairs(nums: List[int]) -> int:
    """
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
    => nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])
    令 arr[i] = nums[i] - rev(nums[i])
        arr[i] == arr[j], 0 <= i < j < n
    """
    n = len(nums)
    MOD = 1_000_000_007

    arr = sorted(num - int(str(num)[::-1]) for num in nums)
    
    res, i = 0, 0
    while i < n:
        j = i + 1
        while j < n and arr[j] == arr[i]:
            j += 1

        res = (res + (j - i) * (j - i - 1) // 2) % MOD

        i = j

    return res

print(countNicePairs(nums))