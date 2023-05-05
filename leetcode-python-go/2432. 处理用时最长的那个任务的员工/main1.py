from typing import List

n = 26
logs = [[1,1],[3,7],[2,12],[7,17]]

def hardestWorker(n: int, logs: List[List[int]]) -> int:
    # 初始化处理时间数组
    times = [0] * n
    # 初始化中间合并过程数组
    max_time, max_id = 0, n

    # 遍历 logs 数组，计算每个员工处理任务的总时间
    for i in range(len(logs)):
        id, leaveTime = logs[i]
        if i == 0:
            start = 0
            times[id] = leaveTime - start
        else:
            start = logs[i - 1][1]
            times[id] = leaveTime - start

        # 比较当前处理时间和最大处理时间
        if times[id] > max_time:
            max_time = times[id]
            max_id = id
        # 比较当前处理时间和最大处理时间并且最大处理时间相同时找出最小的id
        elif times[id] == max_time and id < max_id:
            max_id = id

    return max_id

print(hardestWorker(n, logs))
