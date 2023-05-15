import sys


class Computer:
    def __init__(self, lines):
        self.program = lines
        self.clock = 0
        self.x = 1
        self.total_sig_strength = 0
        self.pixels = {}

    def run(self):
        for line in self.program:
            if line.startswith("noop"):
                self.noop()
            elif line.startswith("addx"):
                v = int(line.split(" ")[1])
                self.add(v)

    def noop(self):
        self.step()

    def add(self, v):
        self.step()
        self.step()
        self.x += v

    def step(self):
        row = self.clock // 40
        col = self.clock % 40
        self.clock += 1
        if self.x - 1 <= col <= self.x + 1:
            pix = '#'
        else:
            pix = ' '
        self.pixels[(row, col)] = pix
        if (self.clock - 20) % 40 == 0:
            self.total_sig_strength += self.clock * self.x

    def print(self):
        for r in range(6):
            for c in range(40):
                print(self.pixels[(r,c)], end='')
            print()


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

comp = Computer(lines)
comp.run()

print(f"part 1: {comp.total_sig_strength}")
print(f"part 2: ")
comp.print()
