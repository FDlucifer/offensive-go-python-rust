s = "0100"

def minOperations(s: str) -> int:
    n = len(s)

    # cnt1: 生成 '01' 交替字符串的操作次数
    # cnt2: 生成 '10' 交替字符串的操作次数
    cnt1, cnt2 = 0, 0

    for i in range(0, n, 2):
        if s[i] == '1':
            cnt1 += 1
        else:
            cnt2 += 1

    for i in range(1, n, 2):
        if s[i] == '0':
            cnt1 += 1
        else:
            cnt2 += 1
    
    return cnt1 if cnt1 < cnt2 else cnt2

print(minOperations(s))