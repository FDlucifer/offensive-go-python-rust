from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        S = len(s) + 1
        ints = list(map(lambda c: ord(c) - ord("a"), s))

        dp = [0] * S
        for i in range(1, S):
            dp[i] = dp[i - 1] ^ (1 << ints[i - 1]) # dp中存储s中的子字符串里拥有的奇数个字母种类数量的1作为前缀

        ones = lambda x: bin(x).count("1")
        return [ones(dp[r + 1] ^ dp[l]) >> 1 <= k for l, r, k in queries]


s1 = Solution()
s = "abcda"
queries = [[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]
print(s1.canMakePaliQueries(s, queries))
