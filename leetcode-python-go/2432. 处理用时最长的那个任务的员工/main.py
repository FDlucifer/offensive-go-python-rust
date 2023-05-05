from typing import List

n = 26
logs = [[1,1],[3,7],[2,12],[7,17]]

def hardestWorker(n: int, logs: List[List[int]]) -> int:
    # 初始化处理时间数组
    times = [0] * n
    # 初始化中间合并过程数组
    timesid = []
    logsi0 = []

    # 遍历 logs 数组，计算每个员工处理任务的总时间
    for i in range(len(logs)):
        id, leaveTime = logs[i]
        if i == 0:
            start = 0
            times[id] = leaveTime - start
        else:
            start = logs[i - 1][1]
            times[id] = leaveTime - start
        timesid.append(times[id])
        logsi0.append(logs[i][0])

    # zip()函数合并logsi0, timesid为一个二维数组
    result = list(zip(logsi0, timesid))

    # 找到二维数组中result[...][1]的最大值
    max_val = max(x[1] for x in result)

    # 找到result[...][1]的最大值对应的最小索引
    min_idx = float('inf')
    for i, x in enumerate(result):
        if x[1] == max_val and x[0] < min_idx:
            min_idx = x[0]

    # 返回result[...][1]的最大值对应的最小索引即为答案
    return min_idx

print(hardestWorker(n, logs))
