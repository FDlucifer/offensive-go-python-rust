#  获取原始数据
n,m,xs,ys,xt,yt = map(int,input().split())
hasa, hasb, xs, ys, xt, yt = [], [], xs-1, ys-1, xt-1, yt-1  # 原始坐标转换成下标索引要-1
for i in range(n): hasa.append(list(map(int,input().split())))
for i in range(n): hasb.append(list(map(int,input().split())))

#  定义一个函数检测当前是左右走还是上下走
def can_pass(x,y,t):
    ab = hasa[x][y] + hasb[x][y]
    k = t//ab
    return t < k*ab + hasa[x][y]  # True表示上下，False表示左右

#  定义一个函数判断某一个点的周围是否都访问过了，如果是该点以后不用访问了
def judge_over(x,y): 
    return (x==0 or dp[x-1][y]) and (x==n-1 or dp[x+1][y]) and (y==0 or dp[x][y-1]) and (y==m-1 or dp[x][y+1])

dp = [[0] * m for _ in range(n)]  # 表示坐标是否已经成功访问，最早访问的轮数的数组
dp[xs][ys] = 1  # 起点在轮数1时已到达
cnt = 2  # 此后轮数为2（为了避开初始值0与题目要求设置差1，输出时-1即可）
start_list = {(xs, ys)}  # 起点集合
while dp[xt][yt] == 0:  # 如果题目没有表示一定能到达，需要加上(`and start_list is not None`)避免无限循环
    nstart_list = set()  # 用于更新start_list的临时变量
    for x, y in start_list:  # 对所有起点遍历
        if can_pass(x,y,cnt-2):  # 上下通行
            nx, ny = x-1, y
            if nx>=0 and dp[nx][ny]==0:  # 若未越界未访问
                dp[nx][ny] = cnt  # 更新为已访问
                nstart_list.add((nx,ny))  # 加入起点（下同）
            nx = x+1
            if nx<n and dp[nx][ny]==0:
                dp[nx][ny] = cnt
                nstart_list.add((nx,ny))
        else:  # 左右通行
            nx, ny = x, y-1
            if ny>=0 and dp[nx][ny]==0:
                dp[nx][ny] = cnt
                nstart_list.add((nx,ny))
            ny = y+1
            if ny<m and dp[nx][ny]==0:
                dp[nx][ny] = cnt
                nstart_list.add((nx,ny))
        if not judge_over(x,y):  # 剪枝判断
            nstart_list.add((x,y))
    cnt += 1
    start_list = nstart_list
print(dp[xt][yt]-1)
