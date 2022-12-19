from typing import List

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

def validPath(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    pa = list(range(n))
    def find(x):
        if pa[x]!=x:
            pa[x] = find(pa[x])
        return pa[x]
    
    for u,v in edges:
        pa[find(u)] = find(v)
    
    return find(source) == find(destination)
    
print(validPath(n, edges, source, destination))