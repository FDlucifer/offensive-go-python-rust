from typing import List

nums = [3,4,5,1,2]

def check(nums: List[int]) -> bool:
    return sum(v > nums[(i + 1) % len(nums)] for i, v in enumerate(nums)) <= 1

print(check(nums))