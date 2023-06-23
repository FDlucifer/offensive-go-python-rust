from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        remainder_count = {0: 1}  # 用于记录余数出现的次数，初始化余数0的次数为1

        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            if prefix_sum in remainder_count:
                count += remainder_count[prefix_sum]
                remainder_count[prefix_sum] += 1
            else:
                remainder_count[prefix_sum] = 1

        return count


s = Solution()
nums = [4,5,0,-2,-3,1]
k = 5
print(s.subarraysDivByK(nums, k))
