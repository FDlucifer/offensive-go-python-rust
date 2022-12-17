from typing import List

graph = [[4,3,1],[3,2,4],[3],[4],[]]

def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    from collections import deque
    ans = []
    q = deque([[0], ])  # path
    while q:
        path = q.popleft()
        if path[-1] == len(graph) - 1:
            ans.append(path)
            continue
        for v in graph[path[-1]]:
            q.append(path + [v])
    return ans

print(allPathsSourceTarget(graph))