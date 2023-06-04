from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        a, b = nums.index(1), nums.index(len(nums))
        if a < b:
            return a + len(nums) - b - 1
        else:
            return a + len(nums) - b - 2

s = Solution()
# nums = [2,1,4,3]
# nums = [2,4,1,3]
nums = [1,3,4,2,5]
# nums = [3,2,1]
# nums = [3,1,2,4]
# nums = [3,2,1,4]
print(s.semiOrderedPermutation(nums))
