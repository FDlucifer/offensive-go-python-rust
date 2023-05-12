import sys

with open(sys.argv[1], "r") as f:
    data = f.read().strip()

i = 4
part1 = None
while i < len(data):
    if not part1 and len(set(data[i-4:i])) == 4:
        part1 = i
    if len(set(data[i-14:i])) == 14:
        part2 = i
        break
    i += 1

print(f"part 1: {part1}")
print(f"part 2: {part2}")
