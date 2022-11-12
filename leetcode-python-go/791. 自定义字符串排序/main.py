from collections import defaultdict

order = "cba"
s = "abcd"

def customSortString(order: str, s: str) -> str:
    val = defaultdict(int)
    for i, ch in enumerate(order):
        val[ch] = i + 1
    
    return "".join(sorted(s, key=lambda ch: val[ch]))


print(customSortString(order, s))