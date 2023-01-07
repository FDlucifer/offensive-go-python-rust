from typing import List
from math import inf

nums = [1,1,4,2,3]
x = 5

def minOperations(nums: List[int], x: int) -> int:
    # 前缀和，后缀和
    pre = [0]
    last = [0]
    n = len(nums)
    dic_last = {0:n}
    for i in range(n):
        pre.append(pre[-1]+nums[i])
        last.append(last[-1]+nums[n-i-1])
        dic_last[last[i+1]] = n-i-1


    res = inf
    for i in range(n+1):
        num = pre[i]
        l = i # l表示左方的数量
        if x - num in dic_last:
            r = dic_last[x-num]
            if l-1 < r:
                res = min(res, l+n-r)
    
    return res if res!=inf else -1
            

print(minOperations(nums, x))
