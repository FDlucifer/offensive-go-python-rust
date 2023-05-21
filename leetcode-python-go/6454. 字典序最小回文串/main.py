str = "egcfe"

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        n = len(s)
        chars = list(s)  # 将字符串转换为字符数组
        left, right = 0, n - 1

        while left < right:
            if chars[left] != chars[right]:
                # 将较小字符替换为较大字符，使得字典序最小
                chars[left] = min(chars[left], chars[right])
                chars[right] = chars[left]
            left += 1
            right -= 1

        return ''.join(chars)  # 将字符数组转换为字符串


s = Solution()
print(s.makeSmallestPalindrome(str))
