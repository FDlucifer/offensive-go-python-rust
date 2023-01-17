from typing import List
from collections import Counter

nums = [13,10,35,24,76]

def countNicePairs(nums: List[int]) -> int:
    n = len(nums)
    MOD = 1_000_000_007

    counter = Counter(num - int(str(num)[::-1]) for num in nums)
    res = 0
    for cnt in counter.values():
        res = (res + cnt * (cnt - 1) // 2) % MOD
    
    return res

print(countNicePairs(nums))