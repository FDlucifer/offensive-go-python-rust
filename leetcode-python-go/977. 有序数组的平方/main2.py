from typing import List

nums = [-4,-1,0,3,10]


def sortedSquares(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * n
    
    i, j, pos = 0, n - 1, n - 1
    while i <= j:
        if nums[i] * nums[i] > nums[j] * nums[j]:
            ans[pos] = nums[i] * nums[i]
            i += 1
        else:
            ans[pos] = nums[j] * nums[j]
            j -= 1
        pos -= 1
    
    return ans

print(sortedSquares(nums))