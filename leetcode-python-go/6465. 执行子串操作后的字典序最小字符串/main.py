class Solution:
    def smallestString(self, s: str) -> str:
        s = list(s)
        c = 0
        for i in range(len(s)):
            if s[i] != 'a':
                s[i] = chr(ord(s[i]) - 1)
                c = 1
            else:
                if c:
                    break
        if not c:
            s[-1] = 'z'
        return "".join(s)


s1 = Solution()
s = "aab"
print(s1.smallestString(s))
