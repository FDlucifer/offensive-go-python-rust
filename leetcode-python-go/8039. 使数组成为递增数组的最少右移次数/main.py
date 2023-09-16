from typing import List

class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        n = len(nums)
        for shift in range(n):
            nums_removed = nums[-shift:] + nums[:-shift]
            is_increasing = nums_removed == sorted(nums)
            if is_increasing:
                return shift
        return -1




s = Solution()
nums = [3,4,5,1,2]
print(s.minimumRightShifts(nums))
