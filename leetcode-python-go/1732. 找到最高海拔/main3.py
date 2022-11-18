from typing import List

gain = [-5,1,5,0,-7]

def largestAltitude(gain: List[int]) -> int:
    return max(sum(([0]+gain)[:i+1]) for i in range(1+len(gain)))


print(largestAltitude(gain))