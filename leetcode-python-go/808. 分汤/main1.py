from functools import cache

n = 50

def soupServings(n: int) -> float:
    n = (n + 24) // 25
    if n >= 179:
        return 1.0
    @cache
    def dfs(a: int, b: int) -> float:
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1.0
        if b <= 0:
            return 0.0
        return (dfs(a - 4, b) + dfs(a - 3, b - 1) +
                dfs(a - 2, b - 2) + dfs(a - 1, b - 3)) / 4
    return dfs(n, n)


print(soupServings(n))