from typing import List
from collections import defaultdict
from heapq import heappop, heappush
from numpy import inf

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u,v,w in edges:
            adj[u].append([v, w])
            adj[v].append([u, w])

        def dijkstra(source, adj, skip_negative):
            pq = [[0, source]]
            dist = defaultdict(lambda: inf)
            dist[source] = 0
            parent = {}
            while pq:
                d, node = heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in adj[node]:
                    if w == -1:
                        if skip_negative:
                            continue
                        w = 1

                    d2 = d + w
                    if d2 < dist[nei]:
                        dist[nei] = d2
                        parent[nei] = node
                        heappush(pq, [d2, nei])

            return dist, parent

        distR, parentR = dijkstra(destination, adj, skip_negative=True)
        if distR.get(source, inf) < target:
            return []
        dist, parent = dijkstra(source, adj, skip_negative=False)
        if dist[destination] > target:
            return []

        path = [destination]
        while path[-1] != source:
            path.append(parent[path[-1]])
        path = path[::-1]

        edges = {(min(u,v), max(u,v)) : w for u, v, w in edges}

        walked = 0
        for u, v in zip(path, path[1:]):
            e = (min(u, v), max(u, v))
            if edges[e] == -1:
                edges[e] = max(target - distR.get(v, inf) - walked, 1)
                if edges[e] > 1:
                    break
            walked += edges[e]

        for e, w in edges.items():
            if w == -1:
                edges[e] = 2 * (10 ** 9)

        return [[u,v,w] for (u,v), w in edges.items()]


s = Solution()
n = 5
edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
source = 0
destination = 1
target = 5

# n = 3
# edges = [[0,1,-1],[0,2,5]]
# source = 0
# destination = 2
# target = 6

# n = 4
# edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]]
# source = 0
# destination = 2
# target = 6
print(s.modifiedGraphEdges(n,edges,source,destination,target))
