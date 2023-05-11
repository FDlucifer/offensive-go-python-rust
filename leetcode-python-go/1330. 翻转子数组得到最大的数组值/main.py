from typing import List
from numpy import inf
from itertools import tee

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        base = d = 0
        mx, mn = -inf, inf
        for a, b in pairwise(nums):
            base += abs(a - b)
            mx = max(mx, min(a, b))
            mn = min(mn, max(a, b))
            d = max(d, abs(nums[0] - b) - abs(a - b),  # i=0
                       abs(nums[-1] - a) - abs(a - b))  # j=n-1
        return base + max(d, 2 * (mx - mn))


if __name__ == "__main__":
    s = Solution()
    nums = [2,4,9,24,2,1,10]
    print(s.maxValueAfterReverse(nums))

