from typing import List
from numpy import inf

n = 5
ranges = [3,4,1,1,0,0]

def minTaps(n: int, ranges: List[int]) -> int:
    intervals = []
    for i, r in enumerate(ranges):
        start = max(0, i - r)
        end = min(n, i + r)
        intervals.append((start, end))
    intervals.sort()

    dp = [inf] * (n + 1)
    dp[0] = 0
    for start, end in intervals:
        if dp[start] == inf:
            return -1
        for j in range(start, end + 1):
            dp[j] = min(dp[j], dp[start] + 1)
    return dp[n]

print(minTaps(n, ranges))