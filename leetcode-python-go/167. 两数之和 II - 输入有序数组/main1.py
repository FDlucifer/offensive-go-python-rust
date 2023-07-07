from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement] + 1, i + 1]
            num_dict[num] = i

s = Solution()
numbers = [2,7,11,15]
target = 9
print(s.twoSum(numbers, target))
