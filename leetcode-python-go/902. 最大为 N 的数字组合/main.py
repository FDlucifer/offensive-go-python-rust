from typing import List
from functools import cache

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        @cache
        def f(i: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num)
            res = 0
            if not is_num:
                res = f(i+1, False, False)
            up = s[i] if is_limit else "9"
            for d in digits:
                if d > up:
                    break
                res += f(i+1, is_limit and d == up, True)
            return res
        return f(0, True, False)



s = Solution()
digits = ["1","3","5","7"]
n = 100
print(s.atMostNGivenDigitSet(digits, n))
