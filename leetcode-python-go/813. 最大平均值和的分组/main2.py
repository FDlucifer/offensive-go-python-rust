from typing import List

nums = [9,1,2,3,9]
k = 3

negInf=-10**7

def largestSumOfAverages(nums: List[int], k: int) -> float:
    n=len(nums)
    ans=[[0]*(k+1) for j in range(n+1)] #ans[i][j]表示的是前i项分成j组的最大平均和
    for i in range(1,n+1):
        ans[i][0]=negInf
        for j in range(1,k+1):
            for p in range(i):
                ans[i][j]=max(ans[i][j],ans[p][j-1]+sum(nums[p:i])/(i-p))
    return ans[n][k]


print(largestSumOfAverages(nums,k))