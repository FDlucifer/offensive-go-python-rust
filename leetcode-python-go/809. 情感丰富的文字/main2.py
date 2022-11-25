from typing import List

S = "heeellooo"
words = ["hello", "hi", "helo"]

class Trie:
    def __init__(self):
        self.cnt = 0
        self.child = {}

    def add(self, word):
        t = self
        for i, ch in enumerate(word):
            if i > 0 and ch == word[i - 1]:
                t.cnt += 1
                continue
            if ch not in t.child:
                t.child[ch] = Trie()
            t = t.child[ch]
            t.cnt = 1
        return

def expressiveWords(s: str, words: List[str]) -> int:

    def expressive(s1, trie):
        n = len(s1)
        i = 0
        while i < n:
            if s1[i] not in trie.child:
                return False
            trie = trie.child[s1[i]]
            j = i + 1
            while j < n and s1[i] == s1[j]:
                j += 1
            cnt = j - i
            if trie.cnt < cnt:
                return False
            if trie.cnt > cnt and trie.cnt < 3:
                return False
            i = j
        return not trie.child

    t = Trie()
    t.add(s)
    res = 0
    for word in words:
        if expressive(word, t):
            res += 1
    return res

print(expressiveWords(S, words))