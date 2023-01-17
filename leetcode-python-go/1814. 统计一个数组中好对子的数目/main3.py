from typing import List
from collections import Counter, defaultdict

nums = [13,10,35,24,76]

def countNicePairs(nums: List[int]) -> int:
    d = defaultdict(int)
    for num in nums:
        n = 0
        x = num
        while x:
            n = n*10 + x%10
            x = x//10
        d[num-n] += 1
    ans = 0
    for k in d:
        ans += d[k]*(d[k] - 1)//2
    return ans % 1000000007

print(countNicePairs(nums))