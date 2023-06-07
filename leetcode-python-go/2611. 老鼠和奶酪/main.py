from typing import List


class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        scores = [(reward1[i] - reward2[i], i) for i in range(len(reward1))]
        scores.sort(reverse=True)  # 按照得分差降序排序
        return sum(reward1[i] for _, i in scores[:k]) + sum([reward2[i] for _, i in scores[k:]]) # 返回前k个reward1的总和加上计算剩余reward2的总和


s = Solution()
reward1 = [1, 4, 4, 6, 4]
reward2 = [6, 5, 3, 6, 1]
k = 1
print(s.miceAndCheese(reward1, reward2, k))
