from math import lcm

n = 1
a = 2
b = 3

MOD = 10 ** 9 + 7

def nthMagicalNumber(n: int, a: int, b: int) -> int:
    _lcm = lcm(a, b)

    def check(x):
        return x // a + x // b - x // _lcm            

    left, right = 2, 10 ** 18
    while left <= right:
        mid = left + ((right - left) >> 1)
        if check(mid) >= n:
            right = mid - 1
        else:
            left = mid + 1
    return left % MOD

print(nthMagicalNumber(n, a, b))