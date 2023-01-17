from typing import List
from collections import Counter

nums = [13,10,35,24,76]

def countNicePairs(nums: List[int]) -> int:
    res = 0
    cnt = Counter()
    for i in nums:
        j = int(str(i)[::-1])
        res += cnt[i - j]
        cnt[i - j] += 1
    return res % (10 ** 9 + 7)

print(countNicePairs(nums))