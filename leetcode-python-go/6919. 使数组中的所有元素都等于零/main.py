from typing import List

class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        f1 = [1] * n
        f2 = [1] * n
        for i in range(1, n):
            if nums1[i] >= nums1[i - 1]:
                f1[i] = max(f1[i], f1[i - 1] + 1)
            if nums1[i] >= nums2[i - 1]:
                f1[i] = max(f1[i], f2[i - 1] + 1)
            if nums2[i] >= nums1[i - 1]:
                f2[i] = max(f2[i], f1[i - 1] + 1)
            if nums2[i] >= nums2[i - 1]:
                f2[i] = max(f2[i], f2[i - 1] + 1)
        return max(f1 + f2)



s = Solution()
nums = [2,2,3,1,1,0]
k = 3
print(s.checkArray(nums, k))
