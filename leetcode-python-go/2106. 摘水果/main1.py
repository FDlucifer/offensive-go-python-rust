from typing import List
from bisect import bisect_left

fruits = [[1,9],[2,10],[3,1],[5,6],[6,3],[8,2],[9,2],[11,4],[18,10],[22,8],[25,2],[26,2],[30,4],[31,5],[33,9],[34,1],[39,10]]
startPos = 19
k = 9

def maxTotalFruits(fruits: List[List[int]], startPos: int, k: int) -> int:
    left = bisect_left(fruits, [startPos - k])  # 向左最远能到 fruits[left][0]
    ans = s = 0
    for pos, amount in fruits[left:]:
        if pos > startPos + k: break
        s += amount
        while pos * 2 - fruits[left][0] - startPos > k and \
                pos - fruits[left][0] * 2 + startPos > k:
            s -= fruits[left][1]  # fruits[left][0] 无法到达
            left += 1
        ans = max(ans, s)  # 更新答案最大值
    return ans


print(maxTotalFruits(fruits, startPos, k))
