from typing import List

n = 3

def numTilings(n: int) -> int:
    mod = 10 ** 9 + 7
    f = [[0] * 3 for _ in range(n + 1)]
    f[0][0] = f[1][0] = 1
    for i in range(1, n):
        f[i + 1][0] = f[i][0] + f[i][1] + f[i][2] + f[i - 1][0]
        f[i + 1][1] = f[i - 1][0] + f[i][2]
        f[i + 1][2] = f[i - 1][0] + f[i][1]
    
    return f[n][0] % mod


print(numTilings(n))