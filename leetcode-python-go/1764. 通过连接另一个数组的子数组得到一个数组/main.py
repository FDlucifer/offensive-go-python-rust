from typing import List

groups = [[1,-1,-1],[3,-2,0]]
nums = [1,-1,0,1,-1,-1,3,-2,0]

def canChoose(groups: List[List[int]], nums: List[int]) -> bool:
    k = 0
    for g in groups:
        while k + len(g) <= len(nums):
            if nums[k: k + len(g)] == g:
                k += len(g)
                break
            k += 1
        else:
            return False
    return True

print(canChoose(groups, nums))