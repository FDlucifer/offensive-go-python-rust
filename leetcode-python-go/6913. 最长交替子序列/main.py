from typing import List


class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i in range(n - 1):
            if nums[i + 1] - nums[i] == 1:
                for j in range(i, n - 1):
                    if nums[j + 1] - nums[j] == pow(-1, j - i):
                        ans = max(ans, j - i + 2)
                    else:
                        break
        return ans


s = Solution()
nums = [2,3,4,3,4]
print(s.alternatingSubarray(nums))
