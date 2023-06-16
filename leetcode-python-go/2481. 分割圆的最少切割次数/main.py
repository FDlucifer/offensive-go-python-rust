class Solution:
    def numberOfCuts(self, n: int) -> int:
        return 0 if n == 1 else n // 2 if n % 2 == 0 else n

s = Solution()
n = 4
print(s.numberOfCuts(n))
