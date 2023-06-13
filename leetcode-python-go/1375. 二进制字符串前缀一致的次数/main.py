from typing import List

# class Solution:
#     def numTimesAllBlue(self, flips: List[int]) -> int:
#         count = 0
#         initstr = [0] * len(flips)
#         for i,val in enumerate(flips):
#             initstr[val-1] = 1
#             prestr = initstr[0:i+1]
#             substr = initstr[i+1:]
#             if 0 not in prestr and 1 not in substr:
#                 count += 1
#         return count

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0  # 用于计数所有前缀一致的次数
        max_flipped = 0  # 记录当前翻转位的最大下标

        for i, val in enumerate(flips):
            max_flipped = max(max_flipped, val)  # 更新当前翻转位的最大下标
            if max_flipped == i + 1:  # 如果翻转位的最大下标等于当前迭代的索引加一，即前面的[1, i] 内的所有位都是 1
                count += 1  # 增加计数

        return count


s = Solution()
flips = [3,2,4,1,5]
print(s.numTimesAllBlue(flips))
