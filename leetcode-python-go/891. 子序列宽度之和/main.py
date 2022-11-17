from typing import List

nums = [2,1,3]

def sumSubseqWidths(nums: List[int]) -> int:
    nums.sort()
    res = 0
    MOD = 10 ** 9 + 7
    x, y = nums[0], 2
    for j in range(1, len(nums)):
        res = (res + nums[j] * (y - 1) - x) % MOD
        x = (x * 2 + nums[j]) % MOD
        y = y * 2 % MOD
    return (res + MOD) % MOD


print(sumSubseqWidths(nums))