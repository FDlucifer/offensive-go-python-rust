from typing import List

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return (min(x, y) * 2 + int(x != y) + z) * 2


s = Solution()
x = 1
y = 34
z = 1
print(s.longestString(x,y,z))
