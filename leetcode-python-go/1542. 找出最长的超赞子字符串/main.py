class Solution:
    def longestAwesome(self, s: str) -> int:
        mask = 0
        memo = {0: -1}
        max_length = 0
        for i in range(len(s)):
            mask ^= (1 << int(s[i]))
            if mask in memo:
                max_length = max(max_length, i - memo[mask])
            else:
                memo[mask] = i
            for j in range(10):
                if (mask ^ (1 << j)) in memo:
                    max_length = max(max_length, i - memo[mask ^ (1 << j)])
        return max_length


s1 = Solution()
s = "3242415"
print(s1.longestAwesome(s))
