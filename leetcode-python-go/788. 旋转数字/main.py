from typing import List
from functools import cache

DIFFS = (0, 0, 1, -1, -1, 1, 1, -1, 0, 1)


class Solution:
    def rotatedDigits(self, n: int) -> int:
        s = str(n)

        @cache
        def f(i: int, has_diff: bool, is_limit: bool) -> int:
            if i == len(s):
                return has_diff
            res = 0
            up = int(s[i]) if is_limit else 9
            for d in range(up + 1):
                if DIFFS[d] != -1:
                    res += f(i + 1, has_diff or DIFFS[d], is_limit and d == up)
            return res

        return f(0, False, True)


s = Solution()
n = 10
print(s.rotatedDigits(n))
