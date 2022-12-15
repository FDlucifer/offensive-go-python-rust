s = "leetcode"
k = 2

def getLucky(s: str, k: int) -> int:
    x, ans = int(''.join(map(lambda x: str(ord(x) - 96), s))), 0
    while k:
        val = 0
        while x:
            val += x % 10
            x //= 10
        x = ans = val
        k -= 1
    return ans

print(getLucky(s,k))