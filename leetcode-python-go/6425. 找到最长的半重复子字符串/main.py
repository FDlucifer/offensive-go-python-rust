class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        def check(x):
            m = len(x)
            res = 0
            for i in range(1, m):
                if x[i] == x[i-1]:
                    res += 1
            return res <= 1

        ans = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                st = s[i:j+1]
                if check(st):
                    ans = max(ans, len(st))
        return ans

lu = Solution()
s = "5494"
print(lu.longestSemiRepetitiveSubstring(s))
