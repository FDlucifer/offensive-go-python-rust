from functools import cache

class Solution:
    def findIntegers(self, n: int) -> int:
        s = str(bin(n))[2:]
        @cache  # 记忆化搜索
        def f(i: int, pre1: int, is_limit: bool) -> int:
            if i == len(s):
                return 1
            up = int(s[i]) if is_limit else 1
            res = f(i + 1, False, is_limit and up == 0)
            if not pre1 and up == 1:
                res += f(i + 1, True, is_limit)
            return res
        return f(0, False, True)

s = Solution()
n = 5
print(s.findIntegers(n))
