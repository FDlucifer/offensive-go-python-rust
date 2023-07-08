from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 对输入列表进行排序
        result = []

        for i in range(len(nums) - 2):
            if nums[i] > 0:  # 停止条件优化
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # 去除重复的元素

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # 去除重复的元素
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # 去除重复的元素
                    left += 1
                    right -= 1

        return result


s = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(s.threeSum(nums))
