M, N, Q = map(int, input().split())
Shelf = [False] * (N + 1)
Books = [0] * (M + 1)
for _ in range(Q):
    nums = list(map(int, input().split()))
    op = nums[0]
    if op == 1:
        x, y = nums[1:]
        if Books[x] != -1 and not Shelf[y] and not Shelf[Books[x]]:
            Books[x] = y
    elif op == 2:
        Shelf[nums[1]] = True
    elif op == 3:
        Shelf[nums[1]] = False
    elif op == 4:
        res, x = -1, nums[1]
        if Books[x] > 0 and not Shelf[Books[x]]:
            Books[x], res = -1, Books[x]
        print(res)
    elif op == 5:
        x = nums[1]
        if Books[x] == -1:
            Books[x] = 0