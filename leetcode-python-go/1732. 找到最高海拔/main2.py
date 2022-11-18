from typing import List

gain = [-5,1,5,0,-7]

def largestAltitude(gain: List[int]) -> int:
    ans,h=0,0
    for a in gain:
        h+=a
        ans=max(ans,h)
    return ans


print(largestAltitude(gain))