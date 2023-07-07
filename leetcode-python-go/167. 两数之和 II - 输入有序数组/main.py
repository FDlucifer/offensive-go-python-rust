from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(1, len(numbers)):
            for j in range(i + 1, len(numbers) + 1):
                if numbers[i - 1] + numbers[j - 1] == target:
                    return [i, j]


s = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(s.twoSum(numbers, target))
