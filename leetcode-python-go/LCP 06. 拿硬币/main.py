from typing import List
import math


class Solution:
    def minCount(self, coins: List[int]) -> int:
        times = 0
        for c in coins:
            times += math.ceil(c / 2)
        return times



s = Solution()
coins = [4,2,1]
print(s.minCount(coins))
