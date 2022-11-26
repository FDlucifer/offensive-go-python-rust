from typing import List

nums = [-4,-1,0,3,10]

def sortedSquares(nums: List[int]) -> List[int]:
    return sorted(num * num for num in nums)


print(sortedSquares(nums))