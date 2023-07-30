from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for i in hours:
            if i >= target:
                count += 1
        return count


s = Solution()
hours = [0,1,2,3,4]
target = 2
print(s.numberOfEmployeesWhoMetTarget(hours, target))
