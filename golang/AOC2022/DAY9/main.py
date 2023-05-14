import sys
import math

move = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

def process_moves(lines, num_knots):
    # hx, hy, tx, ty = 0, 0, 0, 0
    knots = [(0,0)] * num_knots
    visited = {(0,0)}
    for line in lines:
        direction, num = line.split(' ')
        m = move[direction]
        for _ in range(int(num)):
            # move head
            # hx, hy = hx + m[0], hy + m[1]
            knots[0] = (knots[0][0] + m[0], knots[0][1] + m[1])

            # update tails
            for i in range(1, len(knots)):
                # dx, dy = hx - tx, hy - ty
                dx = knots[i-1][0] - knots[i][0]
                dy = knots[i-1][1] - knots[i][1]

                if abs(dx) > 1 or abs(dy) > 1:
                    newx, newy = knots[i][0], knots[i][1]
                    if dx:
                        # tx += math.copysign(1, dx)
                        newx = knots[i][0] + math.copysign(1, dx)
                    if dy:
                        # ty += math.copysign(1, dy)
                        newy = knots[i][1] + math.copysign(1, dy)
                    knots[i] = (newx, newy)
                    # visited.add((tx,ty))
            visited.add(knots[-1])
    return len(visited)

part1 = process_moves(lines, 2)
print(f"part 1: {part1}")
part2 = process_moves(lines, 10)
print(f"part 2: {part2}")
