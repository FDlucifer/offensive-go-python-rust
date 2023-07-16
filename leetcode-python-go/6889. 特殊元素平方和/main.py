from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1,n+1):
            if n % i == 0:
                ans += nums[i-1] * nums[i-1]
        return ans


s = Solution()
nums = [1,2,3,4]
print(s.sumOfSquares(nums))
