from typing import List

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        score = []

        def find_max_and_remove(arr):
            max_val = max(arr)
            arr.remove(max_val)
            return max_val

        def recursive_matrix_sum(matrix):
            if not matrix:
                return

            max_vals = []
            for arr in matrix:
                max_vals.append(find_max_and_remove(arr))

            score.append(max(max_vals))

            new_matrix = [arr for arr in matrix if arr]
            recursive_matrix_sum(new_matrix)

        recursive_matrix_sum(nums)
        return sum(score)


if __name__ == "__main__":
    s = Solution()
    nums = [[7,2,1],[6,4,2],[6,5,3],[3,2,1]]
    print(s.matrixSum(nums))
