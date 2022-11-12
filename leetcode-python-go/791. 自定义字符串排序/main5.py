order = "cba"
s = "abcd"

def customSortString(order: str, s: str) -> str:
    arr=[30]*26
    for i in range(len(order)):
        arr[ord(order[i])-97]=i
    return ''.join(sorted(list(s),key=lambda x:arr[ord(x)-97]))


print(customSortString(order, s))