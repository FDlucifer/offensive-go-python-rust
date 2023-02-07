from typing import List
from collections import defaultdict

keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"]
keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]

def alertNames(keyName: List[str], keyTime: List[str]) -> List[str]:
    timeMap = defaultdict(list)
    for name, time in zip(keyName, keyTime):
        hour, minute = int(time[:2]), int(time[3:])
        timeMap[name].append(hour * 60 + minute)

    ans = []
    for name, times in timeMap.items():
        times.sort()
        if any(t2 - t1 <= 60 for t1, t2 in zip(times, times[2:])):
            ans.append(name)
    ans.sort()
    return ans

print(alertNames(keyName, keyTime))