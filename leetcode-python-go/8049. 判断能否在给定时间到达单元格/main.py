class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t != 1
        d = max(abs(sx - fx), abs(sy - fy))
        return t >= d

s = Solution()
sx = 2
sy = 4
fx = 7
fy = 7
t = 6
print(s.isReachableAtTime(sx,sy,fx,fy,t))
