from typing import List

nums = [-1,0,3,5,9,12]
target = 9

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right - left) // 2 + left
        num = nums[mid]
        if num == target:
            return mid
        elif num > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(search(nums, target))