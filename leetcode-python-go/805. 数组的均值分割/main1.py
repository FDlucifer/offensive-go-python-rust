from typing import List

nums = [1,2,3,4,5,6,7,8]

def splitArraySameAverage(nums: List[int]) -> bool:
    n = len(nums)
    m = n // 2
    s = sum(nums)
    if all(s * i % n for i in range(1, m + 1)):
        return False

    dp = [set() for _ in range(m + 1)]
    dp[0].add(0)
    for num in nums:
        for i in range(m, 0, -1):
            for x in dp[i - 1]:
                curr = x + num
                if curr * n == s * i:
                    return True
                dp[i].add(curr)
    return False


print(splitArraySameAverage(nums))