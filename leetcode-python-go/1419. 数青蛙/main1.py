from itertools import tee
from collections import Counter

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

croakOfFrogs = "crcoakroak"

# 预处理每个字母在 "croak" 中的上一个字母
PREVIOUS = dict(pairwise("croakc"[::-1]))

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    cnt = Counter()
    for ch in croakOfFrogs:
        pre = PREVIOUS[ch]  # pre 为 ch 在 "croak" 中的上一个字母
        if cnt[pre]:  # 如果有青蛙发出了 pre 的声音
            cnt[pre] -= 1  # 复用一只
        elif ch != 'c':  # 否则青蛙必须从 'c' 开始蛙鸣
            return -1  # 不符合要求
        cnt[ch] += 1  # 发出了 ch 的声音
    if any(cnt[ch] for ch in "croa"):
        return -1  # 有发出其它声音的青蛙，不符合要求
    return cnt['k']  # 最后青蛙们都发出了 'k' 的声音


print(minNumberOfFrogs(croakOfFrogs))
