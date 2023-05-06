croakOfFrogs = "crcoakroak"

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    c,r,o,a,k = 0,0,0,0,0
    ret = 0
    for i in croakOfFrogs:
        if i == 'c':
            c += 1
            ret = max(c-k,ret)
        elif c > r and i == 'r':
            r += 1
        elif r > o and i == 'o':
            o += 1
        elif o > a and i == 'a':
            a += 1
        elif a > k and i == 'k':
            k += 1
        else:return -1
    return ret if c==r and c==o and c==a and c==k else -1

print(minNumberOfFrogs(croakOfFrogs))
