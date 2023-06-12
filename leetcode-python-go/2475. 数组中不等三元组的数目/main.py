from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        for k in range(len(nums)):
            for j in range(k):
                for i in range(j):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        count += 1

        return count



s = Solution()
nums = [4,4,2,4,3]
print(s.unequalTriplets(nums))
