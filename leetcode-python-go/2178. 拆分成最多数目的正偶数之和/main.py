from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []

        result = []
        k = 2
        max_sum = 0
        while max_sum < finalSum:
            max_sum += k
            k += 2

        diff = max_sum - finalSum
        for i in range(2, k, 2):
            if i != diff:
                result.append(i)

        return result


s = Solution()
finalSum = 12
print(s.maximumEvenSplit(finalSum))
