from typing import List

folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]

def removeSubfolders(folder: List[str]) -> List[str]:
    folder.sort()
    ans = [folder[0]]
    for i in range(1, len(folder)):
        if not ((pre := len(ans[-1])) < len(folder[i]) and ans[-1] == folder[i][:pre] and folder[i][pre] == "/"):
            ans.append(folder[i])
    return ans

print(removeSubfolders(folder))