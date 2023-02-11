target = "code"

def alphabetBoardPath(target: str) -> str:
    ans = []
    x = y = 0
    for c in target:
        nx, ny = divmod(ord(c) - ord('a'), 5)  # 目标位置
        v = "UD"[nx > x] * abs(nx - x)  # 竖直
        h = "LR"[ny > y] * abs(ny - y)  # 水平
        ans.append((v + h if c != 'z' else h + v) + "!")
        x, y = nx, ny
    return ''.join(ans)

print(alphabetBoardPath(target))