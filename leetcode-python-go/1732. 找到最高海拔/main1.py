from typing import List
import itertools

gain = [-5,1,5,0,-7]

def largestAltitude(gain: List[int]) -> int:
    return max(itertools.accumulate(gain, initial=0))


print(largestAltitude(gain))