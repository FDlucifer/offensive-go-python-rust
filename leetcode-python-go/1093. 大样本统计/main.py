from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        # 统计总数、最小值、最大值
        total_count = sum(count)
        min_value = float('inf')
        max_value = float('-inf')

        # 查找中位数
        middle = (total_count + 1) // 2
        median_value = None
        count_sum = 0
        for i, val in enumerate(count):
            count_sum += val
            if median_value is None and count_sum >= middle:
                if total_count % 2 == 1 or count_sum > middle:
                    median_value = i
                else:
                    j = i + 1
                    while count[j] == 0:
                        j += 1
                    median_value = (i + j) / 2

            if val > 0:
                min_value = min(min_value, i)
                max_value = max(max_value, i)

        # 计算平均值
        sum_value = sum(i * val for i, val in enumerate(count))
        mean_value = sum_value / total_count

        # 查找众数
        mode_value = count.index(max(count))

        return [float(min_value), float(max_value), mean_value, float(median_value), float(mode_value)]


s = Solution()
count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
print(s.sampleStats(count))
