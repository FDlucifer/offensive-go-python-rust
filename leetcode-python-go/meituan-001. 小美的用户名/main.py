nums = int(input())
for _ in range(nums):
    ret, li = True, [False, False]
    strs = input()
    if not (strs[0].islower() or strs[0].isupper()):
        ret = False

    for i in strs:
        if i.islower() or i.isupper():
            li[0] = True
        elif i.isdigit():
            li[1] = True
        else:
            ret = False
            break
    if not all(li):
        ret = False
    print("Accept" if ret else "Wrong")
