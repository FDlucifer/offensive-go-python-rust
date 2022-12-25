n = 10

def minimumBoxes(n: int) -> int:
    i, j, low, high = 0, 0, 1, min(n, 100000)
    while low < high:
        mid = (low + high) >> 1
        isum = mid * (mid + 1) * (mid + 2) // 6
        if isum >= n:
            high = mid
        else:
            low = mid + 1
    i, low, high = low, 1, low
    n -= (i - 1) * i * (i + 1) // 6
    while low < high:
        mid = (low + high) >> 1
        isum = mid * (mid + 1) // 2
        if isum >= n:
            high = mid
        else:
            low = mid + 1
    j = low
    return (i - 1) * i // 2 + j  

print(minimumBoxes(n))