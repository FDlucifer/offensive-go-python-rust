from sortedcontainers import SortedList
from typing import List
from collections import Counter

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        d = Counter(nums)
        sl = SortedList(d.values())
        while len(sl) >= 2:
            a = sl.pop()
            b = sl.pop()
            a -= 1
            b -= 1
            if a:
                sl.add(a)
            if b:
                sl.add(b)
        if not sl:
            return 0
        return sl.pop()


s = Solution()
nums = [2,3,4,4,4]
print(s.minLengthAfterRemovals(nums))
