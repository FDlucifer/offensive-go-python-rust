def main():
    def dfs(u, fa):
        nonlocal graph, a, k, p, i
        res = 1
        for v in graph[u]:
            if v != fa and (a[i] < a[v] or (a[i] == a[v] and i < v)) and a[i] + k >= a[v]:
                res *= (dfs(v, u) + 1)
                res %= p
        return res
    n, k = [int(word) for word in input().strip().split()]
    graph = [[] for i in range(n + 1)]
    for _ in range(n - 1):
        u, v = [int(word) for word in input().strip().split()]
        graph[u].append(v)
        graph[v].append(u)
    a = [0] + [int(word) for word in input().strip().split()]
    ans = 0
    p = 10 ** 9 + 7
    for i in range(1, n + 1):
        ans += dfs(i, 0)
        ans %= p
    print(ans)
    

if __name__ == "__main__":
    main()