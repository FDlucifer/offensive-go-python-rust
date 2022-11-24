from typing import List

nums = [2,9,2,5,6]
left = 2
right = 8

def numSubarrayBoundedMax(nums: list[int], left: int, right: int) -> int:
    lastAlp = [0] * len(nums)
    smallThanLeft = 0
    if left <= nums[0] <= right:
        lastAlp[0] = 1
    elif nums[0] < left:
        smallThanLeft += 1
    for i in range(1, len(nums)):
        if nums[i] < left:
            smallThanLeft += 1
            lastAlp[i] = lastAlp[i - 1]
        elif left <= nums[i] <= right:
            lastAlp[i] = lastAlp[i - 1] + smallThanLeft + 1
            smallThanLeft = 0
        else:
            smallThanLeft = 0
    return sum(lastAlp)

print(numSubarrayBoundedMax(nums, left, right))