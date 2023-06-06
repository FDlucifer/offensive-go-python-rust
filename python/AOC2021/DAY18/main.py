import sys
import math
import json

with open(sys.argv[1], "r") as f:
    lines = f.readlines()


class Pair:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return f"[{self.left},{self.right}]"


class Value:
    def __init__(self, value):
        self.parent = None
        self.value = value

    def __str__(self):
        return str(self.value)


def parse(pairlist):
    pair = Pair()
    l, r = pairlist
    if type(l) == int:
        pair.left = Value(l)
    else:
        pair.left = parse(l)
    if type(r) == int:
        pair.right = Value(r)
    else:
        pair.right = parse(r)
    pair.left.parent = pair
    pair.right.parent = pair
    return pair


def explode(root):
    queue = [(root, 0)]
    while queue:
        cur, dep = queue.pop()
        if dep >= 4:
            # add cur.left to next left value
            search = cur
            while search.parent:
                if search.parent.left != search:
                    search = search.parent.left
                    break
                search = search.parent
            if search.parent:
                while type(search) != Value:
                    search = search.right
                search.value += cur.left.value

            # add cur.right to next right value
            search = cur
            while search.parent:
                if search.parent.right != search:
                    search = search.parent.right
                    break
                search = search.parent
            if search.parent:
                while type(search) != Value:
                    search = search.left
                search.value += cur.right.value

            x = Value(0)
            x.parent = cur.parent
            if cur.parent.left == cur:
                cur.parent.left = x
            else:
                cur.parent.right = x
            # print(f"exploded: {root}")
            queue = [(root, 0)]

        if cur.right and not type(cur.right) == Value:
            queue.append((cur.right, dep + 1))
        if cur.left and not type(cur.left) == Value:
            queue.append((cur.left, dep + 1))

    return root


def split(root):
    queue = [root]
    while queue:
        cur = queue.pop()
        if type(cur) == Value and cur.value > 9:
            pair = Pair()
            pair.left = Value(cur.value // 2)
            pair.right = Value(math.ceil(cur.value / 2))
            pair.left.parent = pair
            pair.right.parent = pair
            pair.parent = cur.parent
            if cur.parent.left == cur:
                cur.parent.left = pair
            else:
                cur.parent.right = pair
            # print(f"split: {root}")
            root = explode(root)
            queue = [root]
            continue
        if type(cur) == Pair:
            queue.append(cur.right)
            queue.append(cur.left)
    return root


def add(p1, p2):
    pair = Pair()
    pair.left = p1
    pair.right = p2
    p1.parent = pair
    p2.parent = pair
    # print(f"added: {pair}")
    return pair


def score(pair):
    if type(pair) == Value:
        return pair.value
    return 3 * score(pair.left) + 2 * score(pair.right)


root = split(explode(parse(json.loads(lines[0]))))
for line in lines[1:]:
    root = add(root, parse(json.loads(line)))
    root = split(explode(root))

print(f"part 1: {score(root)}")

maxscore = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i == j:
            continue
        s = score(
            split(
                explode(add(parse(json.loads(lines[i])), parse(json.loads(lines[j]))))
            )
        )
        maxscore = max(s, maxscore)

print(f"part 2: {maxscore}")
