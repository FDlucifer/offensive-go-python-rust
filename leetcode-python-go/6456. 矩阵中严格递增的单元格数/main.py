from typing import List

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        p = []
        for i in range(n):
            for j in range(m):
                p.append((mat[i][j], i, j))
        p = sorted(p)
        l, r = 0, 0
        x, y = [0] * n, [0] * m
        f = [1] * (n * m)
        while l < len(p):
            while r < len(p) and p[r][0] == p[l][0]:
                r += 1
            for i in range(l, r):
                f[i] += max(x[p[i][1]], y[p[i][2]])
            for i in range(l, r):
                x[p[i][1]] = max(f[i], x[p[i][1]])
                y[p[i][2]] = max(f[i], y[p[i][2]])
            l = r
        return max(max(x), max(y))

s = Solution()
mat = [[3,1,6],[-9,5,7]]
print(s.maxIncreasingCells(mat))
