from typing import List

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if edges == []: # edges为空时特判
            return 1
        elif edges != [] and target == 1 and t >=1: # target为1且t>=1时特判
            return 0

        graph = [[] for _ in range(n + 1)]  # 邻接表表示无向树
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * (n + 1)  # 记录顶点是否已访问

        def dfs(current_vertex, current_time, probability):
            if current_vertex == target:
                if current_time == t or (current_time < t and len(graph[current_vertex]) == 1):
                    return probability  # 当前顶点是目标顶点且达到时间限制或无法跳到其他未访问的顶点
                else:
                    return 0  # 当前顶点是目标顶点但还没有达到时间限制或还可以继续跳到其他未访问的顶点

            visited[current_vertex] = True  # 标记当前顶点为已访问

            count = sum(not visited[next_vertex] for next_vertex in graph[current_vertex])  # 统计当前顶点的未访问的邻居顶点数目

            if count == 0 or current_time == t:  # 当前顶点是叶子节点或已达到时间限制
                return 0

            result = 0

            for next_vertex in graph[current_vertex]:
                if not visited[next_vertex]:  # 遍历未访问的邻居顶点
                    jump_probability = 1 / count  # 计算从当前顶点跳到邻居顶点的概率
                    result += dfs(next_vertex, current_time + 1, probability * jump_probability)  # 递归调用 dfs 函数，并累加结果

            return result

        return dfs(1, 0, 1.0)  # 从顶点 1 开始跳跃，初始时间为 0，初始概率为 1.0

s = Solution()
n = 9
edges = [[2,1],[3,2],[4,3],[5,3],[6,5],[7,3],[8,4],[9,5]]
t = 9
target = 1
print(s.frogPosition(n, edges, t, target))
