from typing import List

n = 3
edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
queries = [[0,1,2],[0,2,5]]

def union(a:int,b:int,group:List[int])->None:
    a,b=find(a,group),find(b,group)
    group[b]=a
def find(a:int,group:List[int])->int:
    if a!=group[a]:
        group[a]=find(group[a],group)
    return group[a]

def distanceLimitedPathsExist(n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
    group,m,o,edgeList=[i for i in range(n)],len(queries),len(edgeList),sorted(edgeList,key=lambda x:x[2])
    ans,j,queries=[None]*m,0,sorted([[i]+queries[i] for i in range(m)],key=lambda x:x[3])
    for i in range(m):
        while j<o and edgeList[j][2]<queries[i][3]:
            union(edgeList[j][0],edgeList[j][1],group)
            j+=1
        ans[queries[i][0]]=find(group[queries[i][1]],group)==find(group[queries[i][2]],group)
    return ans

print(distanceLimitedPathsExist(n, edgeList, queries))