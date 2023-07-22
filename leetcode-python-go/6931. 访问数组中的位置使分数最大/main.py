from typing import List

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        maxx = [-float("inf")] * 2
        maxx[nums[0] % 2] = nums[0]
        n = len(nums)
        for i in range(1, n):
            curMax = -float("inf")
            for j in range(2):
                curMax = max(curMax, maxx[j] + nums[i] - (x if j != nums[i] % 2 else 0))
            maxx[nums[i] % 2] = max(maxx[nums[i] % 2], curMax)
        return max(maxx)


s = Solution()
nums = [2,3,6,1,9,2]
x = 5
print(s.maxScore(nums, x))
