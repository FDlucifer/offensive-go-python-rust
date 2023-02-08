from typing import List

folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]

class Trie:
    def __init__(self):
        self.children = dict()
        self.ref = -1

def removeSubfolders(folder: List[str]) -> List[str]:
    root = Trie()
    for i, path in enumerate(folder):
        path = path.split("/")
        cur = root
        for name in path:
            if name not in cur.children:
                cur.children[name] = Trie()
            cur = cur.children[name]
        cur.ref = i
    
    ans = list()

    def dfs(cur: Trie):
        if cur.ref != -1:
            ans.append(folder[cur.ref])
            return
        for child in cur.children.values():
            dfs(child)

    dfs(root)
    return ans



print(removeSubfolders(folder))