class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if s1[:2] == s2[2:] and s2[:2] == s1[2:]:
            return True
        elif s1[0] == s2[0] and s1[2] == s2[2] and s1[1] == s2[3] and s1[3] == s2[1]:
            return True
        elif s1[1] == s2[1] and s1[3] == s2[3] and s1[0] == s2[2] and s1[2] == s2[0]:
            return True
        elif s1 == s2:
            return True
        return False


s = Solution()
s1 = "abcd"
s2 = "cdab"
print(s.canBeEqual(s1, s2))
