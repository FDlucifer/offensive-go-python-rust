from typing import List
import re

groups = [[1,-1,-1],[3,-2,0]]
nums = [1,-1,0,1,-1,-1,3,-2,0]


def canChoose(groups: List[List[int]], nums: List[int]) -> bool:
    return not not re.search(r'(?<=[ [])' + r',( [ \-\d]+,)* '.join(str(ls)[1:-1] for ls in groups) + r'(?=[,\]])', str(nums))

print(canChoose(groups, nums))