class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        counts = {0: -1}
        bitmask = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in vowels:
                bitmask ^= vowels[char]

            if bitmask not in counts:
                counts[bitmask] = i
            else:
                max_length = max(max_length, i - counts[bitmask])

        return max_length


s1 = Solution()
s = "eleetminicoworoep"
print(s1.findTheLongestSubstring(s))
