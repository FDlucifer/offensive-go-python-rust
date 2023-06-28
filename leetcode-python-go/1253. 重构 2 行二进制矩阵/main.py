from typing import List


class Solution:
    def reconstructMatrix(
        self, upper: int, lower: int, colsum: List[int]
    ) -> List[List[int]]:
        def gen(upper: int, lower: int, colsum: List[int]):
            col0 = [0] * len(colsum)
            col1 = [0] * len(colsum)
            for i, col in enumerate(colsum):
                if col == 0:
                    col0[i] = 0
                    col1[i] = 0
                elif col == 2:
                    col0[i] = 1
                    col1[i] = 1
                    upper -= 1
                    lower -= 1

            for j in range(len(colsum)):
                if col0[j] == 0 and col1[j] == 0 and colsum[j] == 1:
                    col0[j] = 1
                    upper -= 1
                    if upper == 0:
                        break

            for j in range(len(colsum)):
                if col0[j] == 0 and col1[j] == 0 and colsum[j] == 1:
                    col1[j] = 1
                    lower -= 1
                    if lower == 0:
                        break

            return [col0, col1]

        result = gen(upper, lower, colsum)
        if sum(result[0]) != upper or sum(result[1]) != lower:
            return []
        for e in range(len(colsum)):
            if result[0][e] + result[1][e] != colsum[e]:
                return []
        return result


s = Solution()
upper = 2
lower = 3
colsum = [2, 2, 1, 1]
print(s.reconstructMatrix(upper, lower, colsum))
