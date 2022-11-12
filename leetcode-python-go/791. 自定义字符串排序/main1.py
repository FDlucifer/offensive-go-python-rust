from collections import Counter

order = "cba"
s = "abcd"


def customSortString(order: str, s: str) -> str:
    freq = Counter(s)
    ans = list()
    for ch in order:
        if ch in freq:
            ans.extend([ch] * freq[ch])
            freq[ch] = 0
    for (ch, k) in freq.items():
        if k > 0:
            ans.extend([ch] * k)
    return "".join(ans)


print(customSortString(order, s))