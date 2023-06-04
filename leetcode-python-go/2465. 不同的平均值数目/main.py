from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = []
        while len(nums) != 0:
            nums.sort()
            averages.append((nums[0] + nums[-1]) / 2)
            nums = nums[1:-1]

        return len(set(averages))


s = Solution()
nums = [4, 1, 4, 0, 3, 5]
print(s.distinctAverages(nums))
