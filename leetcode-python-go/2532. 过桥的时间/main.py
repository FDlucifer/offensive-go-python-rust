from typing import List
from heapq import heappush, heappop
from numpy import inf

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        ans = free = 0
        l, ll = [], []
        r, rr = [], []
        for i, (x, _, y, _) in enumerate(time): heappush(ll, (-x-y, -i))
        while n or r or rr:
            if not rr and (not r or r[0][0] > free) and (not n or not ll and (not l or l[0][0] > free)):
                cand = inf
                if n and l: cand = min(cand, l[0][0])
                if r: cand = min(cand, r[0][0])
                free = cand

            while r and r[0][0] <= free:
                _, i = heappop(r)
                heappush(rr, (-time[i][0] - time[i][2], -i))

            while l and l[0][0] <= free:
                _, i = heappop(l)
                heappush(ll, (-time[i][0] - time[i][2], -i))

            if rr:
                _, i = heappop(rr)
                free += time[-i][2]
                if n: heappush(l, (free + time[-i][3], -i))
                else: ans = max(ans, free)
            else:
                _, i = heappop(ll)
                free += time[-i][0]
                heappush(r, (free + time[-i][1], -i))
                n -= 1
        return ans


s = Solution()
n = 1
k = 3
time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
print(s.findCrossingTime(n,k,time))
