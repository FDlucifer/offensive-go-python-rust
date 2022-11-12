m, length = list(map(int, input().split()))
nums = list(map(int, input().split()))

def judge(l, r):
    _min = 0
    for x in nums:
        if l <= x <= r: continue
        if x < _min: return False
        _min = x
    return True

def getR(left):
    l, r = left, length
    while l <= r:
        mid = (l + r) >> 1
        if judge(left, mid): r = mid - 1
        else: l = mid + 1
    return l

res = 0
for left in range(1, m + 1):
    right = getR(left)
    if right == length + 1: break
    res += length - right + 1

print(res)
