from typing import List
from collections import Counter, defaultdict

nums = [13,10,35,24,76]

def countNicePairs(nums: List[int]) -> int:
    nums_counter = Counter((num - int(str(num)[::-1]) for num in nums))
    return sum((v - 1) * v // 2 for v in nums_counter.values()) % 1000000007

print(countNicePairs(nums))