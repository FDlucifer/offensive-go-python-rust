from typing import List

n = 4
k = 11

def findKthBit(n: int, k: int) -> str:
    if k == 1:
        return "0"
    
    mid = 1 << (n - 1)
    if k == mid:
        return "1"
    elif k < mid:
        return findKthBit(n - 1, k)
    else:
        k = mid * 2 - k
        return "0" if findKthBit(n - 1, k) == "1" else "1"



print(findKthBit(n, k))