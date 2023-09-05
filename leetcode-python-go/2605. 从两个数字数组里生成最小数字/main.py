from typing import List

class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if set(nums1) & set(nums2):
            min_common_num = min(list(set(nums1) & set(nums2))) # 如果两个数组存在共同元素，则选取其中最小的一个数
            return min_common_num
        else:
            return min(min(nums1), min(nums2)) * 10 + max(min(nums1), min(nums2)) # 否则将分别将两个数组中的最小值里的较小值作为十位，较大值作为个位


s = Solution()
nums1 = [4,1,3]
nums2 = [5,7]
# nums1 = [3,5,2,6]
# nums2 = [3,1,7]
print(s.minNumber(nums1, nums2))
