from typing import List

S = "heeellooo"
words = ["hello", "hi", "helo"]


def expressiveWords(s: str, words: List[str]) -> int:
    def trans(s):
        s1, count = [], 0
        for i, c in enumerate(s):
            if i == 0 or c == s[i-1]:
                count += 1
            else:
                count = 1
            if i == len(s)-1 or c != s[i+1]:
                s1.append((c, count))
        return s1

    new_s = trans(s)
    res = 0
    for word in words:
        new_word = trans(word)
        if len(new_word) != len(new_s): continue
        if all([x[0] == y[0] and (x[1] == y[1] or (x[1] > y[1] and x[1] >= 3)) for x, y in zip(new_s, new_word)]):
            res += 1
    return res


print(expressiveWords(S, words))