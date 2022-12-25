n = 10

def minimumBoxes(n: int) -> int:
        res = 0
        left, right = 1, 2000
        while left <= right:
            mid = left + ((right - left) >> 1)
            if mid * (mid + 1) * (mid + 2) // 6 > n:
                right = mid - 1
            else:
                left = mid + 1
        res = right * (right + 1) // 2
        rest = n - right * (right + 1) * (right + 2) // 6
        if rest == 0:
            return res
        left = 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if mid * (mid + 1) // 2 >= rest:
                right = mid - 1
            else:
                left = mid + 1
        # print(rest, left)
        return res + left

print(minimumBoxes(n))