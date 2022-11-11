from typing import List

n = 3

def numTilings(n: int) -> int:
    MOD = 10 ** 9 + 7

    def multiply(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        rows, columns, temp = len(a), len(b[0]), len(b)
        c = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                for k in range(temp):
                    c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD
        return c

    def matrixPow(mat: List[List[int]], n: int) -> List[List[int]]:
        ret = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
        while n:
            if n & 1:
                ret = multiply(ret, mat)
            n >>= 1
            mat = multiply(mat, mat)
        return ret

    mat = [
        [0, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [1, 1, 1, 1],
    ]
    res = matrixPow(mat, n)
    return res[3][3]



print(numTilings(n))