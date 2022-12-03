s = "dfa12321afd"

def secondHighest(s: str) -> int:
    max1,max2=-1,-1
    for c in s:
        if ord(c)<58:
            a=int(c)
            if a>max1:
                max1,max2=a,max1
            elif max2<a<max1:
                max2=a
    return max2

print(secondHighest(s))