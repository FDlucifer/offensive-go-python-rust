class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        carry = 0
        p1, p2 = len(num1) - 1, len(num2) - 1

        while p1 >= 0 or p2 >= 0:
            x1 = int(num1[p1]) if p1 >= 0 else 0
            x2 = int(num2[p2]) if p2 >= 0 else 0
            digit_sum = x1 + x2 + carry
            carry = digit_sum // 10
            result += str(digit_sum % 10)
            p1 -= 1
            p2 -= 1

        if carry:
            result += str(carry)

        return result[::-1]


s = Solution()
num1 = "11"
num2 = "123"
print(s.addStrings(num1, num2))
