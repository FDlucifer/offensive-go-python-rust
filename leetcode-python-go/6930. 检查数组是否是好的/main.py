from typing import List

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        num_max = max(nums)
        nums_good = [num for num in range(1, num_max+1)] + [num_max]
        if nums == nums_good:
            return True
        return False


s = Solution()
nums = [1, 3, 3, 2]
print(s.isGood(nums))
