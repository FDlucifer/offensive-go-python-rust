from typing import List

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4

def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    res = 0
    for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
        if numberOfBoxes >= truckSize:
            res += truckSize * numberOfUnitsPerBox
            break
        res += numberOfBoxes * numberOfUnitsPerBox
        truckSize -= numberOfBoxes
    return res


print(maximumUnits(boxTypes, truckSize))