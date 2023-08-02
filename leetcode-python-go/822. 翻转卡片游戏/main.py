from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        exclude_set = set()
        n = len(fronts)

        for i in range(n):
            if fronts[i] == backs[i]:
                exclude_set.add(fronts[i])

        min_possible_number = float('inf')

        for num in fronts + backs:
            if num not in exclude_set and num < min_possible_number:
                min_possible_number = num

        return min_possible_number if min_possible_number != float('inf') else 0



s = Solution()
fronts = [1,2,4,4,7]
backs = [1,3,4,1,3]
print(s.flipgame(fronts, backs))
