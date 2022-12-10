from typing import List

cuboids = [[50,45,20],[95,37,53],[45,23,12]]

def maxHeight(cuboids: List[List[int]]) -> int:
    candidates = []
    for c in cuboids:
        candidates += permuteUnique(c)
    n = len(candidates)
    candidates.sort()
    f = [0] * n
    for i in range(n):
        a, b, c = candidates[i]
        for j in range(i):
            pa, pb, pc = candidates[j]
            if pa <= a and pb <= b and pc <= c:
                f[i] = max(f[i], f[j])
        f[i] += c
    return max(f)

def permuteUnique(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    res = []

    def backtrack(idx=0):
        if idx == n:
            res.append(nums[:])
            return
        backtrack(idx + 1)
        for i in range(idx):
            if nums[i] == nums[idx]:
                break
            nums[i], nums[idx] = nums[idx], nums[i]
            backtrack(idx + 1)
            nums[i], nums[idx] = nums[idx], nums[i]

    backtrack()
    return res

print(maxHeight(cuboids))