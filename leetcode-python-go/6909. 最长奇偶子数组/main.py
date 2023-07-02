from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                li = nums[i:j + 1]
                if li[0]%2 == 0 and all(li[k]%2 != li[k - 1]%2 for k in range(1,len(li))) and all(li[k] <= threshold for k in range(len(li))):
                    ans = max(ans, len(li))
        return ans


s = Solution()
nums = [3,2,5,4]
threshold = 5
print(s.longestAlternatingSubarray(nums, threshold))
