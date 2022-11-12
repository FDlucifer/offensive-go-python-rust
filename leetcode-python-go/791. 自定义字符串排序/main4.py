from collections import Counter

order = "cba"
s = "abcd"


def customSortString(order: str, s: str) -> str:
    counter=Counter(s)
    res=[]
    for ch in order:
        cnt=counter.get(ch,0)
        if cnt:
            res.extend([ch]*cnt)
            counter[ch]=0
    for ch,cnt in counter.items():
        if cnt>0:
            res.extend([ch]*cnt)
    return ''.join(res)



print(customSortString(order, s))