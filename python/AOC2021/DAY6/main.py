import sys

# with open(sys.argv[1], 'r') as f:
#     fish = list(map(int, f.read().split(',')))

# for _ in range(80):
#     new_fish = []
#     for f in fish:
#         if f == 0:
#             new_fish.append(6)
#             new_fish.append(8)
#         else:
#             new_fish.append(f-1)
#     fish = new_fish

# part1 = len(fish)
# print(f"part 1: {part1}")

from collections import Counter, defaultdict

with open(sys.argv[1], 'r') as f:
    fish = Counter(map(int, f.read().split(',')))

for _ in range(256):
    new_fish = defaultdict(int)
    for stage, num in fish.items():
        if stage == 0:
            new_fish[6] += num
            new_fish[8] += num
        else:
            new_fish[stage-1] += num
    fish = new_fish
    if _ == 79:
        print(f"part 1: {sum(fish.values())}")

part2 = sum(fish.values())
print(f"part 2: {part2}")
