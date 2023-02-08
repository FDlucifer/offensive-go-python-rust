from typing import List

folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]


def removeSubfolders(folder: List[str]) -> List[str]:
    ans = list()
    folder.sort()
    for f in folder:
        if ans:
            if ans[-1].split("/") != f.split("/")[: len(ans[-1].split("/"))]:
                ans.append(f)
        else:
            ans.append(f)
    return ans

print(removeSubfolders(folder))