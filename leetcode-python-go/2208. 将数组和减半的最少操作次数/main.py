from typing import List
import heapq

class Solution:
    def halveArray(self, nums):
        # 构建最大堆
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        total_sum = sum(nums)
        current_sum = 0
        operations = 0

        while current_sum < total_sum / 2:
            # 从堆中取出最大的元素
            max_num = -heapq.heappop(max_heap)

            # 减半并重新放回堆中
            max_num /= 2
            heapq.heappush(max_heap, -max_num)

            current_sum += max_num
            operations += 1

        return operations


s = Solution()
nums = [5,19,8,1]
print(s.halveArray(nums))
