from typing import List

mod = 1000000007
class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ans, mn = 0, 0
        for num in nums:
            ans = (ans + num * num * (mn + num)) % mod
            mn = (mn * 2 + num) % mod
        return ans

if __name__ == "__main__":
    nums = [2,1,4]
    s = Solution()
    print(s.sumOfPower(nums))
