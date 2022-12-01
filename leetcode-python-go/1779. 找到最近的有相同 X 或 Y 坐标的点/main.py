from typing import List

x = 3
y = 4
points = [[1,2],[3,1],[2,4],[2,3],[4,4]]

def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    n = len(points)
    best, bestid = float("inf"), -1
    for i, (px, py) in enumerate(points):
        if x == px:
            if (dist := abs(y - py)) < best:
                best = dist
                bestid = i
        elif y == py:
            if (dist := abs(x - px)) < best:
                best = dist
                bestid = i
    
    return bestid

print(nearestValidPoint(x, y, points))