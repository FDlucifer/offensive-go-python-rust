from typing import List
import heapq


edges = [[0,1,10],[0,2,1],[1,2,2]]
maxMoves = 6
n = 3

def reachableNodes(edges: List[List[int]], maxMoves: int, n: int) -> int:
    path,dis=[[] for i in range(n)],[10**9]*n
    for e in edges:
        path[e[0]].append([e[1],e[2]])
        path[e[1]].append([e[0],e[2]])
    #下面先求出每个原图中的点到0的最短距离：
    dis[0]=0
    q=[[0,0]] #[编号，距离]
    while q:
        a=heapq.heappop(q)
        for b in path[a[1]]:
            d=a[0]+b[1]+1
            if d<dis[b[0]]:
                dis[b[0]]=d
                heapq.heappush(q,[dis[b[0]],b[0]])
    return sum(a<=maxMoves for a in dis)+sum(min(e[2],max(0,maxMoves-dis[e[0]])+max(0,maxMoves-dis[e[1]])) for e in edges)


print(reachableNodes(edges, maxMoves, n))