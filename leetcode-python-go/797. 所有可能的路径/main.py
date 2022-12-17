from typing import List

graph = [[4,3,1],[3,2,4],[3],[4],[]]

def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    ans = list()
    stk = list()

    def dfs(x: int):
        if x == len(graph) - 1:
            ans.append(stk[:])
            return
        
        for y in graph[x]:
            stk.append(y)
            dfs(y)
            stk.pop()
    
    stk.append(0)
    dfs(0)
    return ans

print(allPathsSourceTarget(graph))