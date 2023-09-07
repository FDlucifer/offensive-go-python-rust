# Python 3.10.6 linux

from typing import List
import bisect
from math import sqrt

class Solution:
    def repairCars(self, A: List[int], cars: int) -> int:
        return bisect.bisect_left(range(10**14), cars, key=lambda x: sum(int(sqrt(x / a)) for a in A))


s = Solution()
ranks = [5,1,8]
cars = 6
print(s.repairCars(ranks, cars))
