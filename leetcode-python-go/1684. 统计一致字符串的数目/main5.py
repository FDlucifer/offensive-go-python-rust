from typing import List

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]


def countConsistentStrings(allowed: str, words: List[str]) -> int:
    res = 0
    for word in words:
        for char in word:
            if char not in allowed:
                break
        else:
            # 这个语句在循环体正常结束（没用被break）时执行
            res += 1
        
    return res

print(countConsistentStrings(allowed, words))