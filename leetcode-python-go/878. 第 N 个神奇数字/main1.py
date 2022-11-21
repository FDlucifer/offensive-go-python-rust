from math import lcm

n = 1
a = 2
b = 3

def nthMagicalNumber(n: int, a: int, b: int) -> int:
    MOD = 10 ** 9 + 7
    c = lcm(a, b)
    m = c // a + c // b - 1
    r = n % m
    res = c * (n // m) % MOD
    if r == 0:
        return res
    addA = a
    addB = b
    for _ in range(r - 1):
        if addA < addB:
            addA += a
        else:
            addB += b
    return (res + min(addA, addB) % MOD) % MOD

print(nthMagicalNumber(n, a, b))