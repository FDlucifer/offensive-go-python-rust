from typing import List

nums = [1,5,2,4,1]

def minOperations(nums: List[int]) -> int:
    ans=0
    for i in range(1,len(nums)):
        ans+=max(0,nums[i-1]+1-nums[i])
        nums[i]=max(nums[i],nums[i-1]+1)
    return ans
        

print(minOperations(nums))