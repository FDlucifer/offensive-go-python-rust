from typing import List

nums = [2,1,3]

mod=10**9+7
def sumSubseqWidths(nums: List[int]) -> int:
    nums.sort()
    n,ans,po=len(nums),0,1
    for i in range(n):
        ans=(ans+po*(nums[i]-nums[-i-1])+mod)%mod
        po=po*2%mod
    return ans


print(sumSubseqWidths(nums))