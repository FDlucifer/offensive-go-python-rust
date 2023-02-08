from typing import List

folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]


def removeSubfolders(folder: List[str]) -> List[str]:
    n = len(folder)

    folder.sort()

    res = []
    res.append(folder[0])

    cond = lambda i, j: folder[j] == folder[i] or \
                        folder[j].startswith(folder[i] + '/')

    i = 0
    while i < n:
        j = i + 1
        while j < n and cond(i, j):
            j += 1
        
        if j < n:
            res.append(folder[j])

        i = j
    
    return res
        

print(removeSubfolders(folder))