order = "cba"
s = "abcd"


def customSortString(order: str, s: str) -> str:
    memo={ch:i for i,ch in enumerate(order)}
    return ''.join(sorted(s,key=lambda x:memo.get(x,-1)))


print(customSortString(order, s))