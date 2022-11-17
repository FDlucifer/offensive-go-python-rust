from typing import List

nums = [2,1,3]

MOD = 10 ** 9 + 7
pow2 = [1]
for i in range(100000):
    pow2.append(pow2[-1] * 2 % MOD)


def sumSubseqWidths(nums: List[int]) -> int:
    n = len(nums)
    nums.sort()
    res = 0
    for i in range(n):
        res = (res + nums[i] * (pow2[i] - pow2[n - i - 1] + MOD)) % MOD
    return res


print(sumSubseqWidths(nums))