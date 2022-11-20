from functools import cache

n = 50

def soupServings(n: int) -> float:
    if n>4800:
        return 1
    if not n:
        return 0.5
    n=(n-1)//25+1
    ans=[[0]*(n+1) for i in range(1+n)]
    ans[0][0]=0.5
    for i in range(1,n+1):
        ans[0][i]=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            ans[i][j]=(ans[max(i-4,0)][j]+ans[max(i-3,0)][j-1]+ans[max(i-2,0)][max(j-2,0)]+ans[i-1][max(j-3,0)])/4
    return ans[n][n]

print(soupServings(n))