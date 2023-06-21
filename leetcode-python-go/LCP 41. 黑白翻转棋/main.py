from typing import List
from collections import deque

class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        m = len(chessboard)
        n = len(chessboard[0])
        direct = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

        def dfs(si, sj):
            res = 0
            stack = deque([(si, sj)])
            is_x = set()
            is_x.add((si, sj))
            while stack:
                for _ in range(len(stack)):
                    ti, tj = stack.popleft()
                    for di, dj in direct:
                        olis = []
                        i, j = ti + di, tj + dj
                        while m > i > -1 < j < n and chessboard[i][j] != '.':
                            if (i, j) in is_x or chessboard[i][j] == 'X':
                                res += len(olis)
                                stack.extend(olis)
                                is_x.update(olis)
                                break
                            elif chessboard[i][j] == 'O':
                                olis.append((i, j))
                                i += di
                                j += dj
            return res
        ans = 0
        for i in range(m):
            for j in range(n):
                if chessboard[i][j] == '.':
                    t = dfs(i, j)
                    ans = max(ans, t)
        return ans


s = Solution()
chessboard = [".X.",".O.","XO."]
print(s.flipChess(chessboard))
