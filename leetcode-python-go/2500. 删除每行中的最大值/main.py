from typing import List

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        # 按升序对每一行排序
        sorted_grid = [sorted(row) for row in grid]

        # 在每一列中找到最大值
        max_values = [max(col) for col in zip(*sorted_grid)]

        # 计算最大值的总和
        return sum(max_values)

s = Solution()
grid = [[1,2,4],[3,3,1]]
print(s.deleteGreatestValue(grid))
