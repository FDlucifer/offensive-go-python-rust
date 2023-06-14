from functools import cache
from string import ascii_lowercase


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        lps = [0]
        k = 0
        for i in range(1, len(evil)):
            while k and evil[k] != evil[i]: k = lps[k-1]
            if evil[k] == evil[i]: k += 1
            lps.append(k)

        @cache
        def fn(i, k, lower, upper):
            """Return number of good strings at position i and k prefix match."""
            if k == len(evil): return 0 # boundary condition
            if i == n: return 1
            lo = ascii_lowercase.index(s1[i]) if lower else 0
            hi = ascii_lowercase.index(s2[i]) if upper else 25

            ans = 0
            for x in range(lo, hi+1):
                kk = k
                while kk and evil[kk] != ascii_lowercase[x]:
                    kk = lps[kk-1]
                if evil[kk] == ascii_lowercase[x]: kk += 1
                ans += fn(i+1, kk, lower and x == lo, upper and x == hi)
            return ans

        return fn(0, 0, True, True) % 1_000_000_007


s = Solution()
n = 2
s1 = "aa"
s2 = "da"
evil = "b"
print(s.findGoodStrings(n,s1,s2,evil))
