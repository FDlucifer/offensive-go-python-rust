from typing import List
from numpy import inf

n = 5
ranges = [3,4,1,1,0,0]

def minTaps(n: int, ranges: List[int]) -> int:
    rightMost = list(range(n + 1))
    for i, r in enumerate(ranges):
        start = max(0, i - r)
        end = min(n, i + r)
        rightMost[start] = max(rightMost[start], end)

    last = ret = pre = 0
    for i in range(n):
        last = max(last, rightMost[i])
        if i == last:
            return -1
        if i == pre:
            ret += 1
            pre = last
    return ret


print(minTaps(n, ranges))