from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = {0: -1}
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            remainder = curr_sum % k

            if remainder in prefix_sum and i - prefix_sum[remainder] >= 2:
                return True

            if remainder not in prefix_sum:
                prefix_sum[remainder] = i

        return False


s = Solution()
nums = [23,2,4,6,7]
k = 6
print(s.checkSubarraySum(nums, k))
