order = "cba"
s = "abcd"

def customSortString(order: str, s: str) -> str:

    n = len(order)

    ch2idx = {
        ch: idx for idx, ch in enumerate(order)
    }

    pairs = [[ch2idx.get(ch, n), ch] for ch in s]

    return ''.join([ch for _, ch in sorted(pairs)])



print(customSortString(order, s))