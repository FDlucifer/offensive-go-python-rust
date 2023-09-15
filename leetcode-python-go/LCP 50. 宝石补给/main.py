from typing import List

class Solution:
    def giveGem(self, gem, operations):
        # 创建一个列表来表示每位勇者的宝石数量
        heroes = gem[:]

        # 模拟赠送操作
        for operation in operations:
            x, y = operation
            # 计算要赠送的宝石数量（向下取整）
            gems_to_send = heroes[x] // 2
            # 更新勇者的宝石数量
            heroes[x] -= gems_to_send
            heroes[y] += gems_to_send

        # 找到拥有最多宝石和最少宝石的勇者
        max_gems = max(heroes)
        min_gems = min(heroes)

        # 返回宝石数量之差
        return max_gems - min_gems



s = Solution()
gem = [3,1,2]
operations = [[0,2],[2,1],[2,0]]
print(s.giveGem(gem, operations))
