runes = [1,3,5,4,1,7]

from typing import List

def runeReserve(runes: List[int]) -> int:
    n = len(runes)
    dp = [1] * n
    runes.sort()
    for i in range(0, n):
        if abs(runes[i] - runes[i-1]) <= 1:
            dp[i] = max(dp[i], dp[i-1]+1)
    return max(dp)

print(runeReserve(runes))
