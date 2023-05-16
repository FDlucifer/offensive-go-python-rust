import sys
import math


class Monkey:
    def __init__(self, text: str) -> None:
        lines = text.split("\n")
        self.items = list(map(int, lines[1].split(":")[-1].split(",")))
        self.op = eval(f"lambda old: {lines[2].split('=')[-1]}")
        self.test = int(lines[3].split(" ")[-1])
        self.true_target = int(lines[4].split(" ")[-1])
        self.false_target = int(lines[5].split(" ")[-1])
        self.num_items = 0


class World:
    def __init__(self, monkey_texts, part2=False) -> None:
        self.monkeys = []
        for mt in monkey_texts:
            self.monkeys.append(Monkey(mt))
        self.part2 = part2
        self.mod_factor = math.prod(m.test for m in self.monkeys)

    def round(self):
        for m in self.monkeys:
            for item in m.items:
                m.num_items += 1
                val = m.op(item)
                if not self.part2:
                    val = val // 3
                else:
                    val = val % self.mod_factor
                if val % m.test == 0:
                    self.monkeys[m.true_target].items.append(val)
                else:
                    self.monkeys[m.false_target].items.append(val)
            m.items = []

    def get_score(self):
        sorted_monkeys = sorted(self.monkeys, key=lambda m: -m.num_items)
        return sorted_monkeys[0].num_items * sorted_monkeys[1].num_items


with open(sys.argv[1], "r") as f:
    monkey_texts = f.read().split("\n\n")

world = World(monkey_texts)
for _ in range(20):
    world.round()

print(f"part 1: {world.get_score()}")

world2 = World(monkey_texts, part2=True)
for _ in range(10000):
    world2.round()

print(f"part 2: {world2.get_score()}")
