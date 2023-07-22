class Solution:
    def sortVowels(self, s: str) -> str:
        # 定义一个函数，用于判断字符是否为元音字母
        def is_vowel(char):
            return char.lower() in {'a', 'e', 'i', 'o', 'u'}

        # 从字符串s中提取出元音字母并进行排序
        vowels = sorted([char for char in s if is_vowel(char)])

        # 将排序后的元音字母按照原来的位置插入到字符串s中
        result = ''
        vowel_index = 0
        for char in s:
            if is_vowel(char):
                result += vowels[vowel_index]
                vowel_index += 1
            else:
                result += char

        return result


lu = Solution()
s = "lEetcOde"
print(lu.sortVowels(s))
