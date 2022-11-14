from typing import List

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x:-x[1])
    ans=0
    for b in boxTypes:
        if not truckSize:
            break
        if b[0]<truckSize:
            truckSize-=b[0]
            ans+=b[0]*b[1]
        else:
            ans+=truckSize*b[1]
            truckSize=0
    return ans


print(maximumUnits(boxTypes, truckSize))