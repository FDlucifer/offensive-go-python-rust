class Solution:
    def pivotInteger(self, n: int) -> int:
        def sum_of_range(m, n):
            return (n - m + 1) * (n + m) // 2

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            sum_mid = sum_of_range(mid, n)

            if mid * (mid + 1) == 2 * sum_mid:
                return mid
            elif mid * (mid + 1) < 2 * sum_mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1


s = Solution()
n = 4
print(s.pivotInteger(n))
