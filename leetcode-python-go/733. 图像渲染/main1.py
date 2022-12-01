from typing import List

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    n, m = len(image), len(image[0])
    currColor = image[sr][sc]

    def dfs(x: int, y: int):
        if image[x][y] == currColor:
            image[x][y] = color
            for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                    dfs(mx, my)

    if currColor != color:
        dfs(sr, sc)
    return image


print(floodFill(image, sr, sc, newColor))