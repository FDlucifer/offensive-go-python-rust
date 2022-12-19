from typing import List

n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2

class UnionFindSet:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    # # 递归版
    # def find(self, x: int) -> int:
    #     if self.parent[x] != x:
    #         self.parent[x] = self.find(self.parent[x])
        
    #     return self.parent[x]

    # 非递归版
    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        
        while x != root:
            x, self.parent[x] = self.parent[x], root

        return root

    def union(self, x: int, y: int) -> None:
        xroot, yroot = self.find(x), self.find(y)

        if xroot != yroot:
            if self.rank[xroot] < self.rank[yroot]:
                xroot, yroot = yroot, xroot

            self.parent[yroot] = xroot

            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
            
    def is_connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


def validPath(
    n: int, 
    edges: List[List[int]], 
    source: int, 
    destination: int
) -> bool:

    ufs = UnionFindSet(n)

    for u, v in edges:
        ufs.union(u, v)

    return ufs.is_connected(source, destination)
        
print(validPath(n, edges, source, destination))