import sys
from collections import defaultdict, deque


class Map:
    def __init__(self, lines, part2=False) -> None:
        self.grid = defaultdict(lambda: 30)
        self.queue = deque()
        self.visited = set()

        for r, row in enumerate(lines):
            for c, char in enumerate(row):
                if char == "E":
                    self.target = (r, c)
                    self.grid[(r, c)] = 25
                elif char == "S":
                    self.queue.append((r, c, 0))
                    self.grid[(r, c)] = 0
                else:
                    if part2 and char == "a":
                        self.queue.append((r, c, 0))
                    self.grid[(r, c)] = ord(char) - ord("a")

    def shortest_path(self):
        while self.queue:
            r, c, d = self.queue.popleft()
            if (r, c) == self.target:
                return d
            if (r, c) in self.visited:
                continue
            self.visited.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if self.grid[(r + dr, c + dc)] <= self.grid[(r, c)] + 1:
                    self.queue.append((r + dr, c + dc, d + 1))


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

map = Map(lines)
print(f"part 1: {map.shortest_path()}")

map2 = Map(lines, part2=True)
print(f"part 2: {map2.shortest_path()}")
