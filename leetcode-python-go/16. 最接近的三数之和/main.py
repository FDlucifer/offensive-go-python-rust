from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    sum3 = sum([nums[i], nums[j], nums[k]])
                    abssum3 = abs(sum3 - target)
                    ans.append([abssum3, sum3])

        ans = list(set(map(tuple, ans)))
        # 找出第一列最小值
        min_value = min(row[0] for row in ans)

        # 找出第一列最小值对应的第二列的值
        result = [row[1] for row in ans if row[0] == min_value]
        return result[0]


s = Solution()
nums = [1, 1, 1, 0]
target = -100
print(s.threeSumClosest(nums, target))
