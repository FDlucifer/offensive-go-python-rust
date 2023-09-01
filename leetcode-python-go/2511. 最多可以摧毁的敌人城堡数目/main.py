from typing import List

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        control = []  # 存储所有你控制的城堡的下标
        no_control = []  # 存储所有没有城堡的空位置的下标
        max_destroyed = 0 # 最多 可以摧毁的敌人城堡数目

        # 找到你控制的城堡和没有城堡的空位置的下标
        for i in range(n):
            if forts[i] == 1:
                control.append(i)
            elif forts[i] == -1:
                no_control.append(i)

        # 遍历你控制的城堡和没有城堡的空位置的下标
        for i in control:
            for j in no_control:
                # 判断i和j之间的所有值是否都为0
                if all(forts[k] == 0 for k in range(min(i, j) + 1, max(i, j))):
                    destroyed = sum(1 for k in range(min(i, j) + 1, max(i, j)) if forts[k] == 0)
                    max_destroyed = max(max_destroyed, destroyed) # 如果i和j之间的所有值全都为0，则更新max_destroyed为i和j之间的所有0个数的最大值

        return max_destroyed



s = Solution()
forts = [1,0,0,-1,0,0,0,0,1]
print(s.captureForts(forts))
