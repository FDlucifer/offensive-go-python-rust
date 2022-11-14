x, y = map(int, input().split())
nums = list(map(int, input().split()))

# 按数字大小进行索引降序排序（原因方便下面 ans 赋值）
sort = sorted(range(x + y), key=nums.__getitem__, reverse=True)
if y > x:
    ans = ['B'] * (x + y)
    # X 队总和越大，整体队伍综合实力越大
    for i in range(x):            # 选 x 个最大值
        ans[sort[i]] = 'A'
elif y == x:
    ans = ['A'] * x + ['B'] * y
else:
    ans = ['B'] * (x + y)
    # X 队总和越小，整体队伍综合实力越大
    for i in range(x):           # 选 x 个最小值
        ans[sort[~i]] = 'A'  # Python 取负数索引写法

print(''.join(ans))
