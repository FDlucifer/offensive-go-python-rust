class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(num_str):
            n = len(num_str)
            half_n = n // 2
            left_half = num_str[:half_n]
            right_half = num_str[half_n:]
            return sum(map(int, left_half)) == sum(map(int, right_half))

        count = 0
        for num in range(low, high + 1):
            num_str = str(num)
            if len(num_str) % 2 == 0 and isSymmetric(num_str):
                count += 1

        return count


s = Solution()
low = 1
high = 100
print(s.countSymmetricIntegers(low, high))
