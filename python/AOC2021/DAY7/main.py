import sys
from functools import lru_cache

with open(sys.argv[1], "r") as f:
    nums = list(map(int, f.read().split(",")))

sums = [sum([abs(n - pos) for n in nums]) for pos in range(min(nums), max(nums) + 1)]
print(f"part 1: {min(sums)}")

@lru_cache()
def cost(x):
    # return sum(i+1 for i in range(x))
    return x*(x+1)//2

sums2 = [sum([cost(abs(n - pos)) for n in nums]) for pos in range(min(nums), max(nums) + 1)]
print(f"part 2: {min(sums2)}")
