from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        return sum(max(nums[i] - nums[i-1], 0) for i in range(1, len(nums))) + nums[0]


s = Solution()
nums = [4,2,5,3]
print(s.maxAlternatingSum(nums))
