import sys
from collections import defaultdict

STEPCOORD = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}
LEFTTURN = {"R": "U", "U": "L", "L": "D", "D": "R"}
RIGHTTURN = {"R": "D", "D": "L", "L": "U", "U": "R"}
FACESCORE = {"R": 0, "D": 1, "L": 2, "U": 3}


class World:
    def __init__(self, map, instructions, part2=False) -> None:
        self.grid = defaultdict(lambda: " ")
        self.position = None
        self.dir = "R"
        self.part2 = part2
        self.parse_grid(map)
        if part2:
            self.parse_edges()
        self.parse_instructions(instructions)

    def parse_grid(self, map):
        self.max_col = 0
        for r, row in enumerate(map.split("\n")):
            for c, char in enumerate(row):
                self.grid[(r, c)] = char
                if not self.position and char != " ":
                    self.position = (r, c)
            self.max_col = max(self.max_col, c)
        self.max_row = r

    def parse_edges(self):
        self.edges = {}
        if sys.argv[1].endswith("ex.txt"):
            SCALE = 4
            for i in range(SCALE):
                self.edges[(0, 8 + i, "U")] = (4, 3 - i, "D")  # 1
                self.edges[(4, 3 - i, "U")] = (0, 8 + i, "D")  # 1
                self.edges[(i, 8, "L")] = (4, 4 + i, "D")  # 2
                self.edges[(4, 4 + i, "U")] = (i, 8, "R")  # 2
                self.edges[(i, 11, "R")] = (11 - i, 15, "L")  # 3
                self.edges[(11 - i, 15, "R")] = (i, 11, "L")  # 3
                self.edges[(4 + i, 0, "L")] = (11, 15 - i, "U")  # 4
                self.edges[(11, 15 - i, "D")] = (4 + 1, 0, "R")  # 4
                self.edges[(7, i, "D")] = (11, 11 - i, "U")  # 5
                self.edges[(11, 11 - i, "D")] = (7, i, "U")  # 5
                self.edges[(7, 4 + i, "D")] = (11 - i, 8, "R")  # 6
                self.edges[(11 - i, 8, "L")] = (7, 4 + i, "U")  # 6
                self.edges[(4 + i, 11, "R")] = (8, 15 - i, "D")  # 7
                self.edges[(8, 15 - i, "U")] = (4 + i, 11, "L")  # 7
            return
        SCALE = 50
        for i in range(SCALE):
            self.edges[(0, 50 + i, "U")] = (150 + i, 0, "R")  # 1
            self.edges[(150 + i, 0, "L")] = (0, 50 + i, "D")  # 1
            self.edges[(i, 50, "L")] = (149 - i, 0, "R")  # 2
            self.edges[(149 - i, 0, "L")] = (i, 50, "R")  # 2
            self.edges[(50 + i, 50, "L")] = (100, i, "D")  # 3
            self.edges[(100, i, "U")] = (50 + i, 50, "R")  # 3
            self.edges[(i, 149, "R")] = (149 - i, 99, "L")  # 4
            self.edges[(149 - i, 99, "R")] = (i, 149, "L")  # 4
            self.edges[(49, 100 + i, "D")] = (50 + i, 99, "L")  # 5
            self.edges[(50 + i, 99, "R")] = (49, 100 + i, "U")  # 5
            self.edges[(0, 100 + i, "U")] = (199, i, "U")  # 6
            self.edges[(199, i, "D")] = (0, 100 + i, "D")  # 6
            self.edges[(149, 50 + i, "D")] = (150 + i, 49, "L")  # 7
            self.edges[(150 + i, 49, "R")] = (149, 50 + i, "U")  # 7


    def parse_instructions(self, instructions):
        res = []
        temp = ""
        for c in instructions:
            if c in "RL":
                if temp:
                    res.append(int(temp))
                    temp = ""
                res.append(c)
            elif c in "1234567890":
                temp += c
        if temp:
            res.append(int(temp))
        self.instructions = res

    def step(self, num):
        for _ in range(num):
            r, c = self.position
            dr, dc = STEPCOORD[self.dir]
            nr, nc = r + dr, c + dc
            nd = self.dir

            if self.part2 and (r, c, self.dir) in self.edges:
                nr, nc, nd = self.edges[(r, c, self.dir)]
            if self.grid[(nr, nc)] == ".":
                self.position = (nr, nc)
                self.dir = nd
            elif self.grid[(nr, nc)] == "#":
                return
            elif self.grid[(nr, nc)] == " ":
                assert not self.part2
                if self.dir == "R":
                    c = 0
                elif self.dir == "L":
                    c = self.max_col
                elif self.dir == "U":
                    r = self.max_row
                elif self.dir == "D":
                    r = 0
                else:
                    assert False
                while self.grid[(r, c)] == " ":
                    r, c = r + dr, c + dc
                if self.grid[(r, c)] == ".":
                    self.position = (r, c)
                elif self.grid[(r, c)] == "#":
                    return
                else:
                    assert False

    def turn(self, dir):
        if dir == "R":
            self.dir = RIGHTTURN[self.dir]
        elif dir == "L":
            self.dir = LEFTTURN[self.dir]
        else:
            assert False

    def run(self):
        for inst in self.instructions:
            if inst == "R" or inst == "L":
                self.turn(inst)
            else:
                self.step(inst)

        r, c = self.position
        return (r + 1) * 1000 + (c + 1) * 4 + FACESCORE[self.dir]


with open(sys.argv[1], "r") as f:
    map, instructions = f.read().strip("\n").split("\n\n")


world = World(map, instructions)
part1 = world.run()
print(f"part 1: {part1}")


world2 = World(map, instructions, part2=True)
part2 = world2.run()
print(f"\rpart 2: {part2}")
