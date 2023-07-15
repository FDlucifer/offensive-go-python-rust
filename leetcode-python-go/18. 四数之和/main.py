from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        for a in range(n):
            for b in range(a+1,n):
                for c in range(b+1, n):
                    for d in range(c+1, n):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target and a != b != c != d:
                            arr = sorted([nums[a], nums[b], nums[c], nums[d]])
                            ans.append(arr)
        return list(set(map(tuple, ans)))


s = Solution()
nums = [-5,5,4,-3,0,0,4,-2]
target = 4
print(s.fourSum(nums, target))
