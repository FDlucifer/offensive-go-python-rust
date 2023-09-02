class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False

        s1_odd_chars = []  # 存储s1中的奇数位置字符
        s1_even_chars = []  # 存储s1中的偶数位置字符
        s2_odd_chars = []  # 存储s2中的奇数位置字符
        s2_even_chars = []  # 存储s2中的偶数位置字符

        for i in range(len(s1)):
            if i % 2 == 0:
                s1_even_chars.append(s1[i])
                s2_even_chars.append(s2[i])
            else:
                s1_odd_chars.append(s1[i])
                s2_odd_chars.append(s2[i])

        # 对字符进行排序，因为字符的具体顺序不重要
        s1_odd_chars.sort()
        s2_odd_chars.sort()
        s1_even_chars.sort()
        s2_even_chars.sort()

        # 如果奇数位置和偶数位置的字符都相同，则可以通过操作使字符串相等
        return s1_odd_chars == s2_odd_chars and s1_even_chars == s2_even_chars


s = Solution()
s1 = "abcdba"
s2 = "cabdab"
print(s.checkStrings(s1, s2))
