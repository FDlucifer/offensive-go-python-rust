from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if (
                        i != j
                        and i != k
                        and j != k
                        and nums[i] + nums[j] + nums[k] == 0
                    ):
                        ans.append(sorted([nums[i], nums[j], nums[k]]))

        return list(set(map(tuple, ans)))


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))
