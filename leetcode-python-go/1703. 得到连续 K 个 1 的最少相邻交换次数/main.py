from typing import List

nums = [1,0,0,0,0,0,1,1]
k = 3

def minMoves(nums: List[int], k: int) -> int:
    idxs=[i for i,v in enumerate(nums) if v==1]
    cur=sum(abs(idxs[i]-idxs[k//2])-abs(i-k//2) for i in range(k))
    res=cur
    for i in range(k,len(idxs)):
        midIdxIdx=i-k+k//2
        cur-=idxs[midIdxIdx]-idxs[i-k]-(midIdxIdx-(i-k)) # pop最左边的元素
        midIdxIdx=i-k+1+(k-1)//2
        cur+=idxs[i]-idxs[midIdxIdx]-(i-midIdxIdx) # append到最右边
        res=min(res,cur)
    return res

print(minMoves(nums, k))