from typing import List

class Solution:
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        # 获取第一组点和第二组点的大小
        size1 = len(cost)
        size2 = len(cost[0])

        # 创建动态规划表，并初始化为正无穷
        dp = [[float('inf')] * (1 << size2) for _ in range(size1 + 1)]
        dp[0][0] = 0

        # 计算动态规划表
        for i in range(size1):
            for mask in range(1 << size2):
                for j in range(size2):
                    # 尝试连接第一组的点i和第二组的点j
                    # 更新连接后的状态和成本
                    dp[i + 1][mask | (1 << j)] = min(dp[i + 1][mask | (1 << j)], dp[i][mask] + cost[i][j])
                    dp[i + 1][mask] = min(dp[i + 1][mask], dp[i][mask] + cost[i][j])

        # 找到最小成本
        min_cost = float('inf')
        for mask in range(1 << size2):
            total_cost = dp[size1][mask]
            for j in range(size2):
                if not mask & (1 << j):
                    # 对于未连接的第二组的点，找到连接它们的最小成本
                    total_cost += min(cost[i][j] for i in range(size1))
            min_cost = min(min_cost, total_cost)

        # 返回最小成本
        return min_cost


s = Solution()
cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
print(s.connectTwoGroups(cost))

