from typing import List
from collections import defaultdict

keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]

def alertNames(
    keyName: List[str], 
    keyTime: List[str]
) -> List[str]:

    hashmap = defaultdict(list)
    for name, time in zip(keyName, keyTime):
        h, m = map(int, time.split(':'))
        hashmap[name].append(h * 60 + m)

    res = []
    for name, tlist in hashmap.items():
        if len(tlist) < 3:
            continue

        tlist.sort()
        for i in range(len(tlist) - 2):
            if tlist[i + 2] - tlist[i] <= 60:
                res.append(name)
                break

    res.sort()

    return res

print(alertNames(keyName, keyTime))