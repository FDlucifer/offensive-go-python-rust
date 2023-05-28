class Solution:
    def minimumCost(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                ans += min(i, len(s) - i)
        return ans

s = "000000010"
aaa = Solution()
print(aaa.minimumCost(s))
