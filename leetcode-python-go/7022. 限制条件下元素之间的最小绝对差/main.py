from typing import List

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        abs_var = []
        n = len(nums)
        for i in range(n):
            if i + x <= n - 1:
                j = n - 1 - i - x
                abs_var.append(abs(nums[i] - nums[i + x]))
                g = 1  # Move g initialization here
                while j > 0:
                    abs_var.append(abs(nums[i] - nums[i + x + g]))
                    g += 1  # Increment g here
                    j -= 1
        return min(abs_var)


s = Solution()
nums = [17,111,61,199,38]
x = 2
print(s.minAbsoluteDifference(nums, x))
