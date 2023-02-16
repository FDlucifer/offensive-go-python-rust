from typing import List
from collections import Counter

nums = [1,3,2,1,3,2,2]

def numberOfPairs(nums: List[int]) -> List[int]:
    cnt = sum(val // 2 for val in Counter(nums).values())
    return [cnt, len(nums) - cnt * 2]

print(numberOfPairs(nums))