poured = 2
query_glass = 1
query_row = 1

def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
    count=[poured]
    for i in range(1,query_row+1):
        arr=[max(0,count[0]-1)/2]
        for j in range(1,i):
            arr.append((max(0,count[j-1]-1)+max(0,count[j]-1))/2)
        count=arr+[max(0,count[i-1]-1)/2]
    return min(1,count[query_glass])


print(champagneTower(poured, query_glass, query_row))