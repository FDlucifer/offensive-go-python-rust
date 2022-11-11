from typing import List
import collections

INF = 10 ** 9

n, a, b = map(int, input().split())
a -= 1              #编号统一成从0开始
b -= 1

adjvex = collections.defaultdict(list)
for _ in range(n - 1):
    x, y = map(int, input().split())
    x -= 1          #编号统一成从0开始
    y -= 1
    adjvex[x].append(y)
    adjvex[y].append(x)


def get_min_dist(sx: int) -> List[int]:
    dist = [INF for _ in range(n)]
    q = collections.deque()
    dist[sx] = 0
    q.append(sx)
    while q:
        x = q.popleft()
        for y in adjvex[x]:
            if (d := dist[x] + 1) < dist[y]:
                dist[y] = d
                q.append(y)
    return dist

dista = get_min_dist(a)
distb = get_min_dist(b)

res = 0
for x in range(n):
    if dista[x] > distb[x]:     #追的人远，被追的人近
        res = max(res, dista[x])
print(res)