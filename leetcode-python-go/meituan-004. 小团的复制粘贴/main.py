n = int(input())
A = list(map(int, input().split()))
B = [-1] * n
m = int(input())
ops = list()
for _ in range(m):
    ops.append(list(map(int, input().split())))


def myquery(ops, n, A, B, m):
    query = []
    for i in range(m):
        op = ops[i]
        if op[0] == 2:
            query.append(B[op[1]-1])
        elif op[0] == 1:
            k, a, b = op[1], op[2]-1, op[3]-1
            if b + k > n:
                k = n - b
            B[b:b+k] = A[a:a+k]
    return query


res = myquery(ops, n, A, B, m)
for num in res:
    print(num)
