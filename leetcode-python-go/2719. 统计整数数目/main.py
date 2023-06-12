import string
from functools import cache

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        MOD = 10 ** 9 + 7
        def f(s: string) -> int:
            @cache  # 记忆化搜索
            def f(i: int, sum: int, is_limit: bool) -> int:
                if sum > max_sum:  # 非法
                    return 0
                if i == len(s):
                    return int(sum >= min_sum)
                res = 0
                up = int(s[i]) if is_limit else 9
                for d in range(up + 1):  # 枚举要填入的数字 d
                    res += f(i + 1, sum + d, is_limit and d == up)
                return res % MOD
            return f(0, 0, True)
        ans = f(num2) - f(num1) + (min_sum <= sum(map(int, num1)) <= max_sum)
        return ans % MOD


s = Solution()
num1 = "4179205230"
num2 = "7748704426"
min_num = 8
max_num = 46
print(s.count(num1,num2,min_num,max_num))
