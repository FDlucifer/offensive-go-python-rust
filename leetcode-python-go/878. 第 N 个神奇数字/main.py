from math import lcm

n = 1
a = 2
b = 3

def nthMagicalNumber(n: int, a: int, b: int) -> int:
    MOD = 10 ** 9 + 7
    l = min(a, b)
    r = n * min(a, b)
    c = lcm(a, b)
    while l <= r:
        mid = (l + r) // 2
        cnt = mid // a + mid // b - mid // c
        if cnt >= n:
            r = mid - 1
        else:
            l = mid + 1
    return (r + 1) % MOD



print(nthMagicalNumber(n, a, b))