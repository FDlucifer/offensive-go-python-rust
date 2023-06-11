from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        min_val = min(nums)
        max_val = max(nums)

        for num in nums:
            if num != min_val and num != max_val:
                return num

        return -1

s = Solution()
nums = [3,2,1,4]
print(s.findNonMinOrMax(nums))
