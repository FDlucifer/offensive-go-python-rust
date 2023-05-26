import sys
from collections import deque

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

points = {")": 3, "]": 57, "}": 1197, ">": 25137}
points2 = {")": 1, "]": 2, "}": 3, ">": 4}
matching = {
    "{": "}",
    "(": ")",
    "[": "]",
    "<": ">",
    "}": "{",
    ")": "(",
    "]": "[",
    ">": "<",
}

score = 0
incomp_scores = []

for line in lines:
    q = deque()
    corrupt = False
    for c in line.strip():
        if c in "([{<":
            q.append(c)
        else:
            if q[-1] == matching[c]:
                q.pop()
            else:
                score += points[c]
                corrupt = True
                break

    if not corrupt:
        score2 = 0
        while q:
            c = q.pop()
            score2 *= 5
            score2 += points2[matching[c]]
        incomp_scores.append(score2)

print(f"part 1: {score}")
print(f"part 2: {sorted(incomp_scores)[len(incomp_scores)//2]}")
