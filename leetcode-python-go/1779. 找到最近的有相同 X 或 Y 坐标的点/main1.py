from typing import List

x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]

def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    return min([(abs(x - i) + abs(y - j), index) for index, (i, j) in enumerate(points) if i == x or j == y], default=(-1, -1))[1]

print(nearestValidPoint(x, y, points))