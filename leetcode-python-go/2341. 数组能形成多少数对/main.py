from typing import List
from collections import defaultdict

nums = [1,3,2,1,3,2,2]

def numberOfPairs(nums: List[int]) -> List[int]:
    cnt = defaultdict(bool)
    res = 0
    for num in nums:
        cnt[num] = not cnt[num]
        if not cnt[num]:
            res += 1
    return [res, len(nums) - 2 * res]

print(numberOfPairs(nums))