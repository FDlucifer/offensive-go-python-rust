class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        nums = []
        for i in range(1, n + 1):
            if i ** x <= n:
                nums.append(i ** x)
            else:
                break
        dp = [0] * (n + 1)
        dp[0] = 1
        mod = 10 ** 9 + 7
        for num in nums:
            for i in range(n, 0, -1):
                if i >= num:
                    dp[i] = (dp[i] + dp[i - num]) % mod
        return dp[n]


s = Solution()
n = 10
x = 2
print(s.numberOfWays(n,x))
