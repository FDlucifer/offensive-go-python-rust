import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

path = []
dirsizes = defaultdict(int)
for line in lines:
    tokens = line.strip().split(' ')
    if tokens[0] == "$" and tokens[1] == "cd":
        if tokens[2] == '/':
            path = ['/']
        elif tokens[2] == '..':
            path.pop()
        else:
            path.append(tokens[2])
    elif tokens[0] == "$" and tokens[1] == "ls":
        pass
    else:
        try:
            size = int(tokens[0])
            for i in range(0, len(path)):
                dirsizes['/'.join(path[:i+1])] += size
        except ValueError:
            pass

part1 = sum(s for s in dirsizes.values() if s <= 100000)
print(f"part 1: {part1}")

disk_size = 70000000
need = 30000000
need_to_free = need - (disk_size - dirsizes['/'])

# part2 = sorted(s for s in dirsizes.values() if s >= need_to_free)[0]
part2 = min(s for s in dirsizes.values() if s >= need_to_free)
print(f"part 2: {part2}")
