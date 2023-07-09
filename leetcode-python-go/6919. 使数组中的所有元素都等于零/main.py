from typing import List

class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        tag = [0] * (n + 1)
        sh = 0
        for i in range(n):
            sh += tag[i]
            if nums[i] - sh < 0:
                return False
            x = nums[i] - sh
            if x:
                if i + k > n:
                    return False
                sh += x
                tag[i + k] -= x
        return True



s = Solution()
nums = [2,2,3,1,1,0]
k = 3
print(s.checkArray(nums, k))
