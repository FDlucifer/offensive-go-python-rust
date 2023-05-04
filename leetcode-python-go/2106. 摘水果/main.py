from typing import List
from bisect import bisect_left

fruits = [[1,9],[2,10],[3,1],[5,6],[6,3],[8,2],[9,2],[11,4],[18,10],[22,8],[25,2],[26,2],[30,4],[31,5],[33,9],[34,1],[39,10]]
startPos = 19
k = 9

def maxTotalFruits(fruits: List[List[int]], startPos: int, k: int) -> int:
    left = bisect_left(fruits, [startPos - k])  # 向左最远能到 fruits[left][0]
    right = bisect_left(fruits, [startPos + 1])  # startPos 右边最近水果（因为下面求的是左闭右开区间）
    ans = s = sum(c for _, c in fruits[left:right])  # 从 fruits[left][0] 到 startPos 的水果数
    while right < len(fruits) and fruits[right][0] <= startPos + k:
        s += fruits[right][1]  # 枚举最右位置为 fruits[right][0]
        while fruits[right][0] * 2 - fruits[left][0] - startPos > k and \
                fruits[right][0] - fruits[left][0] * 2 + startPos > k:
            s -= fruits[left][1]  # fruits[left][0] 无法到达
            left += 1
        ans = max(ans, s)  # 更新答案最大值
        right += 1  # 继续枚举下一个最右位置
    return ans

print(maxTotalFruits(fruits, startPos, k))
