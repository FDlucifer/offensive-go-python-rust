from typing import List

class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        ans = []
        for c in range(len(nums) - 1):
            ans.append(abs(nums[c] - nums[c+1]))
        return min(ans)

s = Solution()
nums = [78,36,2,70,64,24,34,63,21,49]
print(s.findValueOfPartition(nums))
