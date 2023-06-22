from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = 0
        count = 0
        prefixSumCounts = defaultdict(int)
        prefixSumCounts[0] = 1

        for num in nums:
            prefixSum += num
            count += prefixSumCounts[prefixSum - k]
            prefixSumCounts[prefixSum] += 1

        return count

s = Solution()
nums = [1,1,1]
k = 2
print(s.subarraySum(nums, k))
