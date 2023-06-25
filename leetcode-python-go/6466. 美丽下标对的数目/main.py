from typing import List
import math


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def has_common_divisor(a, b):
            return math.gcd(a, b) == 1

        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if has_common_divisor(int(str(nums[i])[0]), int(str(nums[j])[-1])):
                    count += 1

        return count


s = Solution()
nums = [1799,259,1453,374,1854,2212,2104,2221]
print(s.countBeautifulPairs(nums))
