from collections import Counter

lowLimit = 1
highLimit = 10

def countBalls(lowLimit: int, highLimit: int) -> int:
    return max(Counter([sum(int(c) for c in str(i)) for i in range(lowLimit,highLimit+1)]).values())

print(countBalls(lowLimit, highLimit))