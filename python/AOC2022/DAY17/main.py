import sys


class Game:
    def __init__(self, stream) -> None:
        self.stream = stream
        self.rock_num = 0
        self.stream_id = 0
        self.left_wall = 0
        self.right_wall = 0
        self.height = 0
        self.grid = set()
        for i in range(0, 9):
            self.grid.add((i, 0))
        self.new_rock()
        self.signatures = {}

    def drop_one_rock(self):
        while True:
            # push by stream
            self.push(self.stream[self.stream_id] == "<")
            if self.fall():
                break
        sig = self.signature()
        hit = None, None
        if sig in self.signatures:
            # print(f"repeat at h={self.height} r={self.rock_num} prev at {self.signatures[sig]} Delta h: {self.height - self.signatures[sig][0]} r: {self.rock_num - self.signatures[sig][1]}")
            hit = (
                self.height - self.signatures[sig][0],
                self.rock_num - self.signatures[sig][1],
            )
        self.signatures[sig] = (self.height, self.rock_num)
        return hit

    def push(self, left=True):
        dx = -1 if left else 1
        if all(0 < x + dx < 8 for x, y in self.rock) and all(
            (x + dx, y) not in self.grid for x, y in self.rock
        ):
            self.rock = set((x + dx, y) for x, y in self.rock)
        self.stream_id = (self.stream_id + 1) % len(self.stream)

    def fall(self):
        # if can fall, all points move down, return false
        if all((x, y - 1) not in self.grid for x, y in self.rock):
            self.rock = set((x, y - 1) for x, y in self.rock)
            return False
        # if can't fall, lock in, update height, get new rock, return true
        self.height = max([y for x, y in self.rock] + [self.height])
        for x, y in self.rock:
            self.grid.add((x, y))
        self.new_rock()
        return True

    def new_rock(self):
        self.rock = set()
        num = self.rock_num % 5
        if num == 0:
            for x in range(3, 7):
                self.rock.add((x, self.height + 4))
        elif num == 1:
            self.rock.add((3, self.height + 5))
            self.rock.add((4, self.height + 4))
            self.rock.add((4, self.height + 5))
            self.rock.add((4, self.height + 6))
            self.rock.add((5, self.height + 5))
        elif num == 2:
            for x in range(3, 6):
                self.rock.add((x, self.height + 4))
            for y in range(5, 7):
                self.rock.add((5, self.height + y))
        elif num == 3:
            for y in range(4, 8):
                self.rock.add((3, self.height + y))
        elif num == 4:
            for x in range(3, 5):
                for y in range(4, 6):
                    self.rock.add((x, y + self.height))
        else:
            assert False
        self.rock_num += 1

    def print(self):
        top = max([self.height] + [y for x, y in self.rock]) + 2
        for r in range(top, -1, -1):
            print("|", end="")
            for c in range(1, 8):
                if (c, r) in self.grid:
                    print("#", end="")
                elif (c, r) in self.rock:
                    print("@", end="")
                else:
                    print(" ", end="")
            print("|")

    def signature(self):
        rows = 40
        points = set((self.rock_num % 5,))
        for y in range(rows):
            for x in range(1, 8):
                if (x, y + self.height - rows) in self.grid:
                    points.add((x, y))
        return frozenset(points)


with open(sys.argv[1], "r") as f:
    line = f.read().strip()

game = Game(line)
num_to_drop = int(sys.argv[2]) if len(sys.argv) > 2 else 2022
for _ in range(num_to_drop):
    game.drop_one_rock()
    # game.print()

part1 = game.height
print(f"part 1: {part1}")

game2 = Game(line)
num_to_drop = int(sys.argv[2]) if len(sys.argv) > 2 else 1_000_000_000_000
while True:
    dh, dr = game2.drop_one_rock()
    if dh:
        break

rocks_left = num_to_drop - game2.rock_num + 1
fake_sections = rocks_left // dr
more_drops = rocks_left - (fake_sections * dr)
for _ in range(more_drops):
    game2.drop_one_rock()

part2 = game2.height + (fake_sections * dh)
print(f"part 2: {part2}")
