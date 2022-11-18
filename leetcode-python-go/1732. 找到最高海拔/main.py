from typing import List

gain = [-5,1,5,0,-7]

def largestAltitude(gain: List[int]) -> int:
    ans = total = 0
    for x in gain:
        total += x
        ans = max(ans, total)
    return ans


print(largestAltitude(gain))