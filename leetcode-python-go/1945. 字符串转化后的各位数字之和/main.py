s = "leetcode"
k = 2

def getLuckys(s: str, k: int) -> int:
    digits = "".join(str(ord(ch) - ord("a") + 1) for ch in s)

    for i in range(k):
        if len(digits) == 1:
            break
        total = sum(int(ch) for ch in digits)
        digits = str(total)
    
    return int(digits)

print(getLuckys(s,k))