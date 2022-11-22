from collections import Counter

lowLimit = 1
highLimit = 10

def countBalls(lowLimit: int, highLimit: int) -> int:
    count = Counter(sum(map(int, str(i))) for i in range(lowLimit, highLimit + 1))
    return max(count.values())

print(countBalls(lowLimit, highLimit))