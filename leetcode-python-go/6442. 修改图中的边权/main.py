from heapq import heappop, heappush

n = 5
edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
source = 0
destination = 1
target = 5

class Solution(object):
    def modifiedGraphEdges(self, n, edges, source, destination, target):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :type target: int
        :rtype: List[List[int]]
        """
        nei = [set() for _ in range(n)]
        xx = []
        rs = []
        for a, b, w in edges:
            if w!=-1:
                nei[a].add((b, w))
                nei[b].add((a, w))
                rs.append([a, b, w])
            else:
                xx.append((a, b))
        INF = 2000000000
        dd  =[INF]*n
        s, e = source, destination
        def dij():
            for i in range(n): dd[i]=INF
            dd[s]=0
            h = [(0, s)]
            while True:
                while h:
                    d, i = h[0]
                    if dd[i]==d: break
                    heappop(h)
                if not h: break
                d, a = heappop(h)
                for b, w in nei[a]:
                    nd = d+w
                    if dd[b]<=nd: continue
                    heappush(h, (nd, b))
                    dd[b]=nd
        dij()
        if dd[e]<target: return []
        i = 0
        m = len(xx)
        while i<m and dd[e]>target:
            a, b = xx[i]
            i+=1
            nei[a].add((b, 1))
            nei[b].add((a, 1))
            dij()
            if dd[e]<=target:
                rs.append([a, b, 1+target-dd[e]])
                break
            rs.append([a, b, 1])
        if dd[e]>target: return []
        while i<m:
            a, b = xx[i]
            rs.append([a, b, INF])
            i+=1
        return rs

s = Solution()
print(s.modifiedGraphEdges(n, edges, source, destination, target))
