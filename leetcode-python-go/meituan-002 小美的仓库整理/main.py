n = int(input())
w = list(map(int, input().split()))
q = list(map(int, input().split()))
fa = list(range(n + 1))
sum = [0] * (n + 1)
def find(x: int) -> int:
    if fa[x] != x:
        fa[x] = find(fa[x])
    return fa[x]

ans = [0] * n
for i in range(n - 1, 0, -1):
    x = q[i] - 1
    to = find(x + 1)
    fa[x] = to  # 合并 x 和 x+1
    sum[to] += sum[x] + w[x]
    ans[i - 1] = max(ans[i], sum[to])
print(*ans, sep='\n')
