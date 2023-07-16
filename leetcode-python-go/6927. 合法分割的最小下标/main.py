from typing import List
from collections import Counter

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_freq = max(cnt.values())

        for num in nums:
            if cnt[num] == max_freq:
                chosen = num

        c1, c2 = 0, cnt[chosen]
        n = len(nums)
        for i in range(n-1):
            if nums[i] == chosen:
                c1 += 1
                c2 -= 1
            if c1 * 2 > i + 1 and c2 * 2 > n - 1 - i: return i
        return -1

s = Solution()
nums = [1,2,2,2]
print(s.minimumIndex(nums))
