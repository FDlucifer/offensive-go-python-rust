import sys


def getval(m):
    ex = monkeys[m]
    try:
        return int(ex)
    except ValueError:
        pass

    toks = ex.split(" ")
    assert len(toks) == 3

    if toks[1] == "+":
        return getval(toks[0]) + getval(toks[2])
    if toks[1] == "-":
        return getval(toks[0]) - getval(toks[2])
    if toks[1] == "*":
        return getval(toks[0]) * getval(toks[2])
    if toks[1] == "/":
        return getval(toks[0]) / getval(toks[2])
    assert False


def getval2(m, humn):
    if m == "humn":
        return humn
    ex = monkeys[m]
    try:
        return int(ex)
    except ValueError:
        pass

    toks = ex.split(" ")
    assert len(toks) == 3

    if m == "root":
        v1 = getval2(toks[0], humn)
        v2 = getval2(toks[2], humn)
        return (v1 == v2, v1, v2)

    if toks[1] == "+":
        return getval2(toks[0], humn) + getval2(toks[2], humn)
    if toks[1] == "-":
        return getval2(toks[0], humn) - getval2(toks[2], humn)
    if toks[1] == "*":
        return getval2(toks[0], humn) * getval2(toks[2], humn)
    if toks[1] == "/":
        return getval2(toks[0], humn) / getval2(toks[2], humn)
    assert False


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

monkeys = {}
for line in lines:
    m, ex = line.strip().split(": ")
    monkeys[m] = ex

part1 = getval("root")
print(f"part 1: {part1}")


lo = -1e20
hi = 1e20
mid = 0
while True:
    eq, v1, v2 = getval2("root", mid)
    if eq:
        break
    if v1 - v2 > 0:
        lo = mid
    else:
        hi = mid
    mid = (hi + lo) // 2

part2 = mid
print(f"\rpart 2: {part2}")
