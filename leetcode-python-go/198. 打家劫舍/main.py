from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]

        # 创建一个dp数组来保存每个房屋的最大偷窃金额
        dp = [0] * n

        # 初始化前两个房屋的最大偷窃金额
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # 从第三个房屋开始计算最大偷窃金额
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # 最终答案是dp数组的最后一个元素
        return dp[-1]

s = Solution()
nums = [1,2,3,1]
print(s.rob(nums))
