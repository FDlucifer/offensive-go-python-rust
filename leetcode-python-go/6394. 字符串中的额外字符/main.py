from typing import List
from numpy import inf

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        tmp = set(dictionary)
        n = len(s)
        dp = [inf] * (n + 1)
        dp[0] = 0
        for i in range(n):
            dp[i+1] = min(dp[i] + 1, dp[i+1])
            for j in range(i, n):
                if s[i:j+1] in tmp:
                    dp[j+1] = min(dp[j+1], dp[i])
        return dp[-1]

lu = Solution()
s = "tudvcqvpljnavjzgfi"
dictionary = ["nset","vc","mzse","vbae","qp","ir","vp","uz","b","h","jkgh","mfsh","y","wll","xgw","pox","vxz","uye","qv","dbwf","ljn","jl","yqt","wyh","z","qaaz","zu","zdrb","cyp","vtj","k","d","bya","v","ccd","fd","ssx","dwwi","yo","gmg","wlah","echx","jzgf","p"]
print(lu.minExtraChar(s, dictionary))
