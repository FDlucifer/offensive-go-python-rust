from typing import List
from collections import defaultdict

nums = [1,3,2,1,3,2,2]

def numberOfPairs(nums: List[int]) -> List[int]:
    n = len(nums)
    hashmap = [0 for _ in range(101)]
    for i in range(n):
        hashmap[nums[i]] += 1

    ans0 = 0
    for cnt in hashmap:
        ans0 += cnt // 2

    ans1 = n - ans0 * 2

    res = [ans0, ans1]

    return res

print(numberOfPairs(nums))