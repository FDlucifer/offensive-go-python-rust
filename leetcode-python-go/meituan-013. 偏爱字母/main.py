input()
s = input()
res, cnt = 0, 0
for c in s:
    if c == 'E':
        cnt += 1
        res = max(res, cnt)
    else:
        cnt -= 1
        cnt = max(cnt, 0)
print(res)
