import sys

with open(sys.argv[1], "r") as f:
    input_ = f.read()

coords, folds = input_.split("\n\n")
folds = [x.split()[-1].split("=") for x in folds.strip().split("\n")]

G = set([tuple(map(int, coord.split(","))) for coord in coords.split("\n")])

for i, fold in enumerate(folds):
    if fold[0] == "y":
        for p in G.copy():
            if p[1] > int(fold[1]):
                G.remove(p)
                G.add((p[0], 2 * int(fold[1]) - p[1]))

    if fold[0] == "x":
        for p in G.copy():
            if p[0] > int(fold[1]):
                G.remove(p)
                G.add((2 * int(fold[1]) - p[0], p[1]))

    if i == 0:
        print(f"part 1: {len(G)}")

maxx = max([p[1] for p in G])
maxy = max([p[0] for p in G])

print("part 2: ")
for x in range(maxx + 1):
    for y in range(maxy + 1):
        if (y, x) in G:
            print(".", end="")
        else:
            print(" ", end="")
    print()
