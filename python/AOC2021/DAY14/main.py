import sys
from collections import Counter

with open(sys.argv[1], "r") as f:
    s, patterns = f.read().split("\n\n")

s = s.strip()
c = {}
for line in patterns.strip().split("\n"):
    pair, new = line.strip().split(" -> ")
    c[pair] = new

pairs = Counter()
for i in range(len(s) - 1):
    pairs[s[i] + s[i + 1]] += 1

for t in range(40):
    if t == 10:
        counts = Counter()
        for p in pairs:
            counts[p[0]] += pairs[p]
        counts[s[-1]] += 1

        part1 = max(counts.values()) - min(counts.values())
        print(f"part 1: {part1}")
    pairs2 = Counter()
    for pair in pairs:
        pairs2[pair[0] + c[pair]] += pairs[pair]
        pairs2[c[pair] + pair[1]] += pairs[pair]
    pairs = pairs2

counts = Counter()
for p in pairs:
    counts[p[0]] += pairs[p]
counts[s[-1]] += 1

part2 = max(counts.values()) - min(counts.values())
print(f"part 2: {part2}")
