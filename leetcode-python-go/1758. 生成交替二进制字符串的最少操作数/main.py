s = "0100"

def minOperations(s: str) -> int:
    cnt = sum(int(c) != i % 2 for i, c in enumerate(s))
    return min(cnt, len(s) - cnt)

print(minOperations(s))