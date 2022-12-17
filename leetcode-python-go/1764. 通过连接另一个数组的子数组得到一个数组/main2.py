from typing import List

groups = [[1,-1,-1],[3,-2,0]]
nums = [1,-1,0,1,-1,-1,3,-2,0]

def canChoose(groups: List[List[int]], nums: List[int]) -> bool:
    i, j = 0, 0

    while i < len(groups) and j < len(nums):
        if nums[j] != groups[i][0] or groups[i] != nums[j: j + (len(groups[i]))]:
            j += 1
        else:
            j += len(groups[i])
            i += 1
    
    return i == len(groups)

print(canChoose(groups, nums))