from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
#         dp = [0, 0, 0]
#         for a in nums:
#             for i in dp[:]:
#                 dp[(i + a) % 3] = max(dp[(i + a) % 3], i + a)
#         return dp[0]
        dp = [0] * 3
        for num in nums:
            for addnum in [num + i for i in dp]:
                dp[addnum % 3] = max(dp[addnum % 3], addnum)
        return dp[0]

s = Solution()
nums = [5,2,2,2]
print(s.maxSumDivThree(nums))
