from typing import List
from bisect import bisect_right

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            ans = max(ans, bisect_right(nums, nums[i] + k * 2) - i)
        return ans

s = Solution()
nums = [4,6,1,2]
k = 2
print(s.maximumBeauty(nums, k))
