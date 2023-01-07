from typing import List

nums = [1,1,4,2,3]
x = 5

def minOperations(nums: List[int], x: int) -> int:
    n = len(nums)
    total = sum(nums)

    if total < x:
        return -1
    
    right = 0
    lsum, rsum = 0, total
    ans = n + 1
    for left in range(-1, n - 1):
        if left != -1:
            lsum += nums[left]
        while right < n and lsum + rsum > x:
            rsum -= nums[right]
            right += 1
        if lsum + rsum == x:
            ans = min(ans, (left + 1) + (n - right))
    
    return -1 if ans > n else ans

print(minOperations(nums, x))
