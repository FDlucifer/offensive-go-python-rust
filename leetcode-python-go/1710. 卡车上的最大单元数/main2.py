from typing import List

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    count=[0]*1005
    for b in boxTypes:
        count[b[1]]+=b[0]
    ans=0
    for i in range(1000,0,-1):
        if not truckSize:
            break
        if count[i]<truckSize:
            truckSize-=count[i]
            ans+=count[i]*i
        else:
            ans+=truckSize*i
            truckSize=0
    return ans


print(maximumUnits(boxTypes, truckSize))