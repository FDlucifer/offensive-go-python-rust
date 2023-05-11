import sys

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

part1 = 0
part2 = 0
for line in lines:
    e1, e2 = line.split(',')
    x1 = list(map(int, e1.split('-')))
    x2 = list(map(int, e2.split('-')))
    if (x1[0] <= x2[0] and x2[1] <= x1[1]) or (x2[0] <= x1[0] and x1[1] <= x2[1]):
        part1 += 1
    if (x1[0] <= x2[0] and x2[0] <= x1[1]) or (x2[0] <= x1[0] and x1[0] <= x2[1]):
        part2 += 1

pairs = [[list(map(int, elf.split('-'))) for elf in line.split(',')] for line in lines]
listcomp_part1 = len([p for p in pairs if (p[0][0] <= p[1][0] and p[1][1] <= p[0][1]) or (p[1][0] <= p[0][0] and p[0][1] <= p[1][1])])
assert part1 == listcomp_part1

print(f"part 1: {part1}")
print(f"part 2: {part2}")
