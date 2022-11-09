from typing import List

n = 5
mines = [[4, 2]]

def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:
    grid,left,right,up,down=[[0]*n for i in range(n)],[[0]*n for i in range(n)],[[0]*n for i in range(n)],[[0]*n for i in range(n)],[[0]*n for i in range(n)]
    for m in mines:
        grid[m[0]][m[1]]=1
    for i in range(n):
        if not grid[i][0]:
            left[i][0]=1
        if not grid[i][n-1]:
            right[i][n-1]=1
        if not grid[0][i]:
            up[0][i]=1
        if not grid[n-1][i]:
            down[n-1][i]=1
        for j in range(1,n):
            if not grid[i][j]:
                left[i][j]=1+left[i][j-1]
            if not grid[i][n-1-j]:
                right[i][n-1-j]=1+right[i][n-j]
            if not grid[j][i]:
                up[j][i]=1+up[j-1][i]
            if not grid[n-1-j][i]:
                down[n-1-j][i]=1+down[n-j][i]
    return max(min(min(left[i][j],right[i][j]),min(up[i][j],down[i][j])) for i in range(n) for j in range(n))


print(orderOfLargestPlusSign(n, mines))