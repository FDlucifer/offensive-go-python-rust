class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        def countBits(num):
            count = 0
            while num > 0:
                count += num & 1
                num >>= 1
            return count

        if num1 < num2:
            return -1

        for steps in range(101):
            diff = num1 - 1 * num2 * steps
            bits = countBits(diff)
            if bits <= steps and steps <= diff:
                return steps

        return -1


s = Solution()
num1 = 5
num2 = -21
print(s.makeTheIntegerZero(num1, num2))
