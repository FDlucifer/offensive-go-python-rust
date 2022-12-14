from typing import List

n = 3
edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries = [[0,1,2],[0,2,5]]

def distanceLimitedPathsExist(n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
    edgeList.sort(key=lambda e: e[2])

    # 并查集模板
    fa = list(range(n))
    def find(x: int) -> int:
        if fa[x] != x:
            fa[x] = find(fa[x])
        return fa[x]
    def merge(from_: int, to: int) -> None:
        fa[find(from_)] = find(to)

    ans, k = [False] * len(queries), 0
    # 查询的下标按照 limit 从小到大排序，方便离线
    for i, (p, q, limit) in sorted(enumerate(queries), key=lambda p: p[1][2]):
        while k < len(edgeList) and edgeList[k][2] < limit:
            merge(edgeList[k][0], edgeList[k][1])
            k += 1
        ans[i] = find(p) == find(q)
    return ans

print(distanceLimitedPathsExist(n, edgeList, queries))