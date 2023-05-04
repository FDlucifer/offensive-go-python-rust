from typing import List
from bisect import bisect_left

fruits = [[1,9],[2,10],[3,1],[5,6],[6,3],[8,2],[9,2],[11,4],[18,10],[22,8],[25,2],[26,2],[30,4],[31,5],[33,9],[34,1],[39,10]]
startPos = 19
k = 9

def maxTotalFruits(fruits: List[List[int]], startPos: int, k: int) -> int:
    left = 0
    right = 0
    n = len(fruits)
    sum = 0
    ans = 0

    def step(left: int, right: int) -> int:
        if fruits[right][0] <= startPos:
            return startPos - fruits[left][0]
        elif fruits[left][0] >= startPos:
            return fruits[right][0] - startPos
        else:
            return min(abs(startPos - fruits[right][0]), abs(startPos - fruits[left][0])) + \
                fruits[right][0] - fruits[left][0]

    # 每次固定住窗口右边界
    while right < n:
        sum += fruits[right][1]
        # 移动左边界
        while left <= right and step(left, right) > k:
            sum -= fruits[left][1]
            left += 1

        ans = max(ans, sum)
        right += 1

    return ans


print(maxTotalFruits(fruits, startPos, k))
