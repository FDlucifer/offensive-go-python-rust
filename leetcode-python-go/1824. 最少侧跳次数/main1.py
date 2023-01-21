from typing import List
from numpy import inf

obstacles = [0,1,2,3,0]

def minSideJumps(obstacles: List[int]) -> int:
    # 一开始变换赛道的距离，由于需要保存的状态只有有限个，所以可以使用滚动数组
    d = [1, 0, 1]

    for i in range(1, len(obstacles)):
        # 每一步状态转移分变换不变换，一共九条路径，但由于我们不需要输出路径，因此在变换赛道的部分，我们不需要记录从哪条路径过去的
        minCnt = inf
        # 不变换赛道
        for j in range(3):
            if j == obstacles[i] - 1:
                d[j] = inf
            else:
                # d[j] 不变，我们这里需要计算minCnt，为下一种情况做准备
                minCnt = min(minCnt, d[j])
        
        # 变换赛道
        for j in range(3):
            # 当然只需要计算这一种情况，遇到obstacle就是inf
            if j != obstacles[i] - 1:
                d[j] = min(d[j], minCnt + 1)
    
    return min(d)

print(minSideJumps(obstacles))