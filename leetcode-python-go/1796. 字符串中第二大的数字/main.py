s = "dfa12321afd"

def secondHighest(s: str) -> int:
    first = second = -1
    for c in s:
        if c.isdigit():
            num = int(c)
            if num > first:
                second = first
                first = num
            elif second < num < first:
                second = num
    return second

print(secondHighest(s))