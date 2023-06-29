class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] == " " or sentence[-1] == " ":
            return False
        sentence_arr = sentence.split(" ")
        if sentence_arr[0][0] == sentence_arr[-1][-1] and len(sentence_arr) > 1:
            for i in range(len(sentence_arr) - 1):
                if sentence_arr[i][-1] != sentence_arr[i + 1][0]:
                    return False
            return True
        elif sentence_arr[0][0] == sentence_arr[-1][-1] and len(sentence_arr) == 1:
            return True
        else:
            return False


s = Solution()
sentence = "leetcode exercises sound delightful"
print(s.isCircularSentence(sentence))
