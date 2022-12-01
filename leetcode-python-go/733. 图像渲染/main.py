from typing import List
import collections

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    currColor = image[sr][sc]
    if currColor == color:
        return image
    
    n, m = len(image), len(image[0])
    que = collections.deque([(sr, sc)])
    image[sr][sc] = color
    while que:
        x, y = que.popleft()
        for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= mx < n and 0 <= my < m and image[mx][my] == currColor:
                que.append((mx, my))
                image[mx][my] = color
    
    return image

print(floodFill(image, sr, sc, newColor))