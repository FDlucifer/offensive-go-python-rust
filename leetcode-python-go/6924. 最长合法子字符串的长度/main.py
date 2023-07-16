from typing import List

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        n = len(word)
        maxi = [n] * n
        for i in range(n):
            for j in range(10):
                if i + j > n: break
                if word[i:i+j+1] in forbidden:
                    maxi[i] = i+j
                    break
        for i in range(n-1, 0, -1):
            maxi[i-1] = min(maxi[i], maxi[i-1])
        return max(v - i for i, v in enumerate(maxi))


s = Solution()
word = "cbaaaabc"
forbidden = ["aaa","cb"]
print(s.longestValidSubstring(word, forbidden))
