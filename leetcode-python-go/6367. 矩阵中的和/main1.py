from typing import List

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ans = []
        for num in nums:
            num.sort()
            ans.append(num)

        max_values = [max(column) for column in zip(*ans)]
        return sum(max_values)


s = Solution()
nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
print(s.matrixSum(nums))
