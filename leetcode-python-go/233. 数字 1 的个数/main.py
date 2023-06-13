from functools import cache

class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        @cache  # 记忆化搜索
        def f(i: int, cnt1: int, is_limit: bool) -> int:
            if i == len(s):
                return cnt1
            res = 0
            up = int(s[i]) if is_limit else 9  # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
            for d in range(up + 1):  # 枚举要填入的数字 d
                res += f(i + 1, cnt1+(d == 1), is_limit and d == up)
            return res
        return f(0, 0, True)


s = Solution()
n = 13
print(s.countDigitOne(n))
