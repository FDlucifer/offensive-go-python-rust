from typing import List
from collections import Counter, defaultdict

nums = [13,10,35,24,76]

def countNicePairs(nums: List[int]) -> int:
    # 反转 数组映射
    return sum((v-1)*v//2 for _,v in Counter([i-int(str(i)[::-1]) for i in nums]).items())%(10**9+7)

print(countNicePairs(nums))