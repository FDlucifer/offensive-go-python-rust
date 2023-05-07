from typing import List

class Solution:
    def rampartDefensiveLine(self, rampart: List[List[int]]) -> int:
        n = len(rampart)
        lo = 1
        hi = int(1e8)
        while lo <= hi:
            mid = (lo + hi) >> 1
            cl = rampart[0][1]
            can = True
            for l, r in rampart[1:-1]:
                if l < cl:
                    can = False
                    break
                lspace = l - cl
                if lspace >= mid:
                    cl = r
                else:
                    cl = r + mid - lspace
            if rampart[-1][0] < cl:
                can = False
            if can:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi

# 示例
if __name__ == '__main__':
    s = Solution()
    rampart1 = [[0,3],[4,5],[7,9]]
    print(s.rampartDefensiveLine(rampart1)) # 输出 3

    rampart2 = [[1,2],[5,8],[11,15],[18,25]]
    print(s.rampartDefensiveLine(rampart2)) # 输出 4
