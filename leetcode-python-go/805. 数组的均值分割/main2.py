from typing import List
import collections

nums = [1,2,3,4,5,6,7,8]

def splitArraySameAverage(nums: List[int]) -> bool:
    n, s = len(nums), sum(nums)

    def helper(arr):
        candidates = collections.defaultdict(list)
        candidates[0].append(0)
        n = len(arr)
        size = 1 << n
        f = [0] * size
        for mask in range(1, size):
            lowbit = mask & -mask
            f[mask] = f[mask - lowbit] + arr[lowbit.bit_length() - 1]
            candidates[bin(mask).count("1")].append(f[mask])
        for k in candidates:
            candidates[k].sort()
        return candidates
    
    left, right = helper(nums[:n // 2]), helper(nums[n // 2:])
    for i in range(1, n // 2 + 1):
        if (i * s) % n == 0:
            target = i * s // n
            for j in range(i + 1):
                if not (j in left and (i - j in right)):
                    continue
                left_candidates = left[j]
                right_candidates = right[i - j]
                l, r = 0, len(right_candidates) - 1
                while l < len(left_candidates) and r >= 0:
                    cur = left_candidates[l] + right_candidates[r]
                    if cur == target:
                        return True
                    elif cur < target:
                        l += 1
                    else:
                        r -= 1
    return False

print(splitArraySameAverage(nums))