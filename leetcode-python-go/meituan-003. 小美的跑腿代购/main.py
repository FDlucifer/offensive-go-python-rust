import heapq

total, cur = map(int, input().split())
li, ret = [], []
for i in range(total):
    index = i
    price, wieght = map(int, input().split())
    heapq.heappush(li, [-(price + wieght * 2), index])

for i in range(cur):
    ret.append(heapq.heappop(li)[1])
print(' '.join(str(i + 1) for i in sorted(ret)))
