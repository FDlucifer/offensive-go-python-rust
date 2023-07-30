from itertools import permutations

class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def g(a: str, b: str) -> str:
            if a.find(b) != -1:
                return a
            i = min(len(a), len(b))
            while a[len(a) - i :] != b[:i]:
                i -= 1
            return a + b[i:]

        def f(a: str, b: str, c: str) -> str:
            return g(g(a, b), c)

        ans = f(a, b, c)
        for x in [f(a, c, b), f(b, a, c), f(b, c, a), f(c, a, b), f(c, b, a)]:
            if len(x) < len(ans) or (len(x) == len(ans) and x < ans):
                ans = x
        return ans


s = Solution()
a = "xyyyz"
b = "xzyz"
c = "zzz"
print(s.minimumString(a,b,c))
