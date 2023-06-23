from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        if remainder == 0:
            return 0

        prefix_sum = 0
        prefix_remainder_map = {0: -1}
        min_length = len(nums)
        curr_remainder = 0

        for i, num in enumerate(nums):
            prefix_sum += num
            curr_remainder = prefix_sum % p
            target_remainder = (curr_remainder - remainder + p) % p

            if target_remainder in prefix_remainder_map:
                subarray_length = i - prefix_remainder_map[target_remainder]
                min_length = min(min_length, subarray_length)

            prefix_remainder_map[curr_remainder] = i

        if min_length < len(nums):
            return min_length
        else:
            return -1


s = Solution()
nums = [6,3,5,2]
p = 9
print(s.minSubarray(nums, p))
