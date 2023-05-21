import sys
import math

with open(sys.argv[1], 'r') as f:
    cmds = f.readlines()

pos, depth = 0, 0
for cmd in cmds:
    direction, qty = cmd.strip().split(' ')
    qty = int(qty)
    if direction == "forward":
        pos += qty
    elif direction == "down":
        depth += qty
    elif direction == "up":
        depth -= qty


print(f"part 1: {pos * depth}")

pos, depth, aim = 0, 0, 0
for cmd in cmds:
    direction, qty = cmd.strip().split(' ')
    qty = int(qty)
    if direction == "forward":
        pos += qty
        depth += (aim * qty)
    elif direction == "down":
        aim += qty
    elif direction == "up":
        aim -= qty

print(f"part 2: {pos * depth}")

def parse_line(line):
    direction, qty = cmd.strip().split(' ')
    qty = int(qty)
    if direction == "forward":
        return (qty, 0)
    if direction == "down":
        return (0, qty)
    if direction == "up":
        return (0, -qty)

print(f"part 1: {math.prod(map(sum, (zip(*[parse_line(line) for line in cmds]))))}")
