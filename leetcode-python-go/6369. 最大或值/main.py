from typing import List

class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre, suf = [0] * n, [0] * n
        for i in range(n):
            if i:
                pre[i] = pre[i - 1] | nums[i]
            else:
                pre[i] = nums[i]
        for i in reversed(range(n)):
            if i + 1 < n:
                suf[i] = suf[i + 1] | nums[i]
            else:
                suf[i] = nums[i]
        ans = 0
        for i in range(n):
            res = (pre[i - 1] if i else 0) | (suf[i + 1] if i + 1 < n else 0)
            res |= nums[i] << k
            ans = max(ans, res)
        return ans


if __name__ == "__main__":
    nums = [8,1,2]
    k = 2
    s = Solution()
    print(s.maximumOr(nums, k))
