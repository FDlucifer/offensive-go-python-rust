from typing import List
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        return sum(Counter(tuple(row) for row in grid)[tuple(col)] for col in list(map(list, zip(*grid))))

s = Solution()
grid = [[3,3,3,6,18,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[1,1,1,11,19,1,1,1,1,1],[3,3,3,18,19,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3],[3,3,3,1,6,3,3,3,3,3],[3,3,3,3,1,3,3,3,3,3]]
# grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(s.equalPairs(grid))
