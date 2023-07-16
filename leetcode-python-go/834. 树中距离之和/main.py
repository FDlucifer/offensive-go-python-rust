from typing import List

from collections import defaultdict
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # 构建邻接表表示树的结构
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # 存储每个节点的子节点个数和距离之和
        count = [1] * n  # 子节点个数
        distance = [0] * n  # 距离之和

        def dfs(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(child, node)
                count[node] += count[child]
                distance[node] += distance[child] + count[child]

        def dp(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue
                # 根据父节点的距离之和和子节点个数计算当前节点的距离之和
                distance[child] = distance[node] - count[child] + n - count[child]
                dp(child, node)

        # 从根节点开始DFS计算节点的子节点个数和距离之和
        dfs(0, -1)
        # 从根节点开始DP计算节点的距离之和
        dp(0, -1)

        return distance



s = Solution()
n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
print(s.sumOfDistancesInTree(n, edges))
