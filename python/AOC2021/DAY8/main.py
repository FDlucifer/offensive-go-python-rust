import sys

with open(sys.argv[1], "r") as f:
    lines = list(map(str.strip, f.readlines()))

cnt = 0
for line in lines:
    digits, disp = line.split(" | ")
    cnt += sum([1 for x in disp.split() if len(x) in [2, 3, 4, 7]])

print(f"part 1: {cnt}")

total = 0
for line in lines:
    digits, disp = line.split(" | ")
    result = ["" for _ in range(10)]
    digits = [set(x) for x in digits.split()]
    result[1] = [x for x in digits if len(x) == 2][0]
    result[4] = [x for x in digits if len(x) == 4][0]
    result[7] = [x for x in digits if len(x) == 3][0]
    result[8] = [x for x in digits if len(x) == 7][0]

    result[6] = [x for x in digits if len(x) == 6 and not result[1].issubset(x)][0]
    result[9] = [x for x in digits if len(x) == 6 and result[4].issubset(x)][0]
    result[0] = [
        x for x in digits if len(x) == 6 and x != result[6] and x != result[9]
    ][0]

    result[3] = [x for x in digits if len(x) == 5 and result[1].issubset(x)][0]
    result[5] = [
        x for x in digits if len(x) == 5 and x.issubset(result[9]) and x != result[3]
    ][0]
    result[2] = [
        x for x in digits if len(x) == 5 and x != result[3] and x != result[5]
    ][0]

    disp = [set(x) for x in disp.split()]
    total += int("".join([str(result.index(x)) for x in disp]))

print(f"part 2: {total}")
