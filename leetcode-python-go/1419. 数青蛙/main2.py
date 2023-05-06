from itertools import tee

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

croakOfFrogs = "crcoakroak"

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    mydict = dict(pairwise("croakc")) #字典中mydict['a']理解为当前等待叫a的青蛙
    cnt = dict(zip("croak",[0]*5))
    # print(mydict,cnt)
    for c in croakOfFrogs:
        if c != "c" and cnt[c] == 0:
            #没有能叫的，且不是第一个字母
            return -1
        if cnt[c] >0 :
            # 拦截下叫c的有才复用，否则可能把c的减到负数了
            cnt[c] -= 1
        cnt[mydict[c]] += 1
    if any([cnt[x] for x in "roak"]):
        return -1
    return cnt["c"]

print(minNumberOfFrogs(croakOfFrogs))
