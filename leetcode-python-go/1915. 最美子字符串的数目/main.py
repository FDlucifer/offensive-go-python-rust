class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024  # 计数数组，用于记录每个前缀的奇数字符出现次数的状态
        count[0] = 1  # 空字符串的状态为0
        mask = 0  # 当前前缀的状态

        result = 0

        for char in word:
            # 计算当前字符对应的二进制位
            bit = ord(char) - ord('a')

            # 更新当前前缀的状态
            mask ^= 1 << bit

            # 计算与当前前缀状态相差一个字符的状态
            result += count[mask]

            # 计算与当前前缀状态相差一个字符的状态（每个字符出现偶数次）
            for i in range(10):
                result += count[mask ^ (1 << i)]

            # 更新计数数组
            count[mask] += 1

        return result



s = Solution()
word = "aba"
print(s.wonderfulSubstrings(word))
