s = "ab##"
t = "c#d#"

def backspaceCompare(S: str, T: str) -> bool:
    def build(s: str) -> str:
        ret = list()
        for ch in s:
            if ch != "#":
                ret.append(ch)
            elif ret:
                ret.pop()
        return "".join(ret)
    
    return build(S) == build(T)

print(backspaceCompare(s, t))