from typing import List

nums = [1,0,2]

def isIdealPermutation(nums: List[int]) -> bool:
    return all(abs(x - i) <= 1 for i, x in enumerate(nums))


print(isIdealPermutation(nums))