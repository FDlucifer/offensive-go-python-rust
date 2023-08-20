from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        i = 0  # 指向 words 数组中的单词索引
        j = 0  # 指向 s 字符串中的字符索引

        while i < len(words) and j < len(s):
            if words[i][0] == s[j]:
                i += 1
            j += 1

        return i == len(words) and j == len(s)

s1 = Solution()
words = ["alice","bob","charlie"]
s = "abc"
print(s1.isAcronym(words, s))
