s = "0100"

def minOperations(s: str) -> int:
    n = len(s)

    # cnt1: 生成 '01' 交替字符串的操作次数
    # cnt2: 生成 `10` 交替字符串的操作次数
    cnt1, cnt2 = 0, 0

    for i in range(n):
        cnt1 += (i & 1 and s[i] == '0') + (i & 1 == 0 and s[i] == '1')
        cnt2 += (i & 1 and s[i] == '1') + (i & 1 == 0 and s[i] == '0')

    return cnt1 if cnt1 < cnt2 else cnt2

print(minOperations(s))