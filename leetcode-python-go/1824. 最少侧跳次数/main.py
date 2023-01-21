from typing import List
from numpy import inf

obstacles = [0,1,2,3,0]

def minSideJumps(obstacles: List[int]) -> int:
    d = [1, 0, 1]
    for i in range(1, len(obstacles)):
        minCnt = inf
        for j in range(3):
            if j == obstacles[i] - 1:
                d[j] = inf
            else:
                minCnt = min(minCnt, d[j])
        for j in range(3):
            if j != obstacles[i] - 1:
                d[j] = min(d[j], minCnt + 1)
    return min(d)

print(minSideJumps(obstacles))