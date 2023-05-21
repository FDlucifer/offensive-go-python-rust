import sys

with open(sys.argv[1], 'r') as f:
    lines = list(map(int, f.readlines()))

part1 = sum([x0 < x1 for x0, x1 in zip(lines, lines[1:])])
print(f"part 1: {part1}")

# part2 = sum([sum(lines[i:i+3]) < sum(lines[i+1:i+4]) for i in range(len(lines) - 2)])
zipped = list(zip(lines, lines[1:], lines[2:]))
part2 = sum([sum(x0) < sum(x1) for x0, x1 in list(zip(zipped, zipped[1:]))])
print(f"part 2: {part2}")

def solve(*lists):
    zipped = list(zip(*lists))
    return sum([sum(x0) < sum(x1) for x0, x1 in zip(zipped, zipped[1:])])

print(f"part 1: {solve(lines)}")
print(f"part 2: {solve(lines, lines[1:], lines[2:])}")
