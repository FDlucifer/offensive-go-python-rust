import sys


with open(sys.argv[1], "r") as f:
    nums = list(map(int, f.readlines()))

s1, s2x = None, None

for x in nums:
    if 2020 - x in nums:
        s1 = x
    for y in nums:
        if 2020 - (x + y) in nums:
            s2x, s2y = x, y
            break
    if s1 and s2x:
        break

print(f"Part 1: {s1 * (2020-s1)}")
print(f"Part 2: {s2x * s2y * (2020 - s2x - s2y )}")
