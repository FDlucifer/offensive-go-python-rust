from typing import List

class Solution:
    def pondSizes(self, land):
        def explore(row, col):
            if row < 0 or row >= len(land) or col < 0 or col >= len(land[0]) or land[row][col] != 0:
                return 0
            size = 1
            land[row][col] = -1
            size += explore(row - 1, col - 1)
            size += explore(row - 1, col)
            size += explore(row - 1, col + 1)
            size += explore(row, col - 1)
            size += explore(row, col + 1)
            size += explore(row + 1, col - 1)
            size += explore(row + 1, col)
            size += explore(row + 1, col + 1)
            return size

        sizes = []
        for row in range(len(land)):
            for col in range(len(land[0])):
                if land[row][col] == 0:
                    size = explore(row, col)
                    sizes.append(size)
        sizes.sort()
        return sizes


s = Solution()
land = [[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]
print(s.pondSizes(land))
