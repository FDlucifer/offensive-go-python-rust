from typing import List

nums = [2,1,3]

mod=10**9+7
po=[1]+[0]*100000
for i in range(1,100001):
    po[i]=po[i-1]*2%mod

def sumSubseqWidths(nums: List[int]) -> int:
    count=[0]*100005
    for a in nums:
        count[a]+=1
    maxSum,minSum,num=0,0,0
    for i in range(1,100001):
        if count[i]:
            maxSum=(maxSum+po[num]*(po[count[i]]-1)*i)%mod
            num+=count[i]
    num=0
    for i in range(100000,0,-1):
        if count[i]:
            minSum=(minSum+po[num]*(po[count[i]]-1)*i)%mod
            num+=count[i]
    return (maxSum-minSum+mod)%mod


print(sumSubseqWidths(nums))