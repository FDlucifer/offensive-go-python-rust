from typing import List

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        def countDistinctElements(arr):
            return len(set(arr))

        n = len(nums)
        distinct_elements = len(set(nums))
        result = 0
        left = 0
        window = {}

        for right in range(n):
            window[nums[right]] = window.get(nums[right], 0) + 1

            while countDistinctElements(window) == distinct_elements:
                result += n - right
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1

        return result


s = Solution()
nums = [1,3,1,2,2]
print(s.countCompleteSubarrays(nums))
