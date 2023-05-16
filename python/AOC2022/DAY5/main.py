import sys
from collections import defaultdict

with open(sys.argv[1], "r") as f:
    lines = f.read()

create_raw, insts = lines.rstrip().split('\n\n')
crates = defaultdict(list)
crates2 = defaultdict(list)

for ci in create_raw.split('\n')[:-1][::-1]:
    i = 1
    while i < len(ci):
        if ci[i] != ' ':
            crates[(i+3)//4].append(ci[i])
            crates2[(i+3)//4].append(ci[i])
        i += 4

for inst in insts.split('\n'):
    _, num, _, start, _, stop = inst.split(' ')
    num, start, stop = int(num), int(start), int(stop)
    for i in range(num):
        crates[stop].append(crates[start].pop())
    crates2[stop].extend(crates2[start][-num:])
    crates2[start] = crates2[start][:-num]

part1 = ''.join(c[-1] for c in crates.values())
print(f"part 1: {part1}")
part2 = ''.join(c[-1] for c in crates2.values())
print(f"part 2: {part2}")
