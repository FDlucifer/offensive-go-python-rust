class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digit_sum = 0
        for i, s in enumerate(str(n)):
            if i % 2 == 0:
                digit_sum += int(s)
            else:
                digit_sum -= int(s)
        return digit_sum


s = Solution()
n = 521
print(s.alternateDigitSum(n))
