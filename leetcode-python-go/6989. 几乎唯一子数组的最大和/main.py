from typing import List

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        max_sum = 0
        window = []
        unique_count = 0
        element_count = {}

        for right in range(n):
            # 维护窗口内的元素计数
            if nums[right] not in element_count or element_count[nums[right]] == 0:
                unique_count += 1
            element_count[nums[right]] = element_count.get(nums[right], 0) + 1

            # 将当前元素加入滑动窗口
            window.append(nums[right])

            # 如果窗口大小大于k，移除左侧元素并更新计数
            while len(window) > k:
                left_element = window.pop(0)
                element_count[left_element] -= 1
                if element_count[left_element] == 0:
                    unique_count -= 1

            # 如果不同元素数量大于等于m，计算窗口内元素的和
            if unique_count >= m:
                max_sum = max(max_sum, sum(window))

        return max_sum


s = Solution()
nums = [1,2,2]
m = 2
k = 2
print(s.maxSum(nums, m, k))
