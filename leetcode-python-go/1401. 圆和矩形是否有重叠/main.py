import math

class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        if xCenter < x1 - radius or xCenter > x2 + radius:
            return False
        if yCenter < y1 - radius or yCenter > y2 + radius:
            return False
        if x1 <= xCenter <= x2 and y1 <= yCenter <= y2:
            return True

        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        distance = math.sqrt((xCenter - closest_x) ** 2 + (yCenter - closest_y) ** 2)
        return distance <= radius


s = Solution()
radius = 1
xCenter = 0
yCenter = 0
x1 = 1
y1 = -1
x2 = 3
y2 = 1
print(s.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2))
