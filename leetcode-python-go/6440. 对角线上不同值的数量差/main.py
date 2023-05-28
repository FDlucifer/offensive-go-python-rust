from typing import List

class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        m, n = len(grid), len(grid[0])
        for i in range(m):
            ans.append([])
            for j in range(n):
                s, t = set(), set()
                for k in range(1, min(i, j) + 1):
                    s.add(grid[i - k][j - k])
                for k in range(1, min(m - i, n - j)):
                    t.add(grid[i + k][j + k])
                ans[-1].append(abs(len(s) - len(t)))
        return ans

grid = [[1,2,3],[3,1,5],[3,2,1]]
s = Solution()
print(s.differenceOfDistinctValues(grid))
