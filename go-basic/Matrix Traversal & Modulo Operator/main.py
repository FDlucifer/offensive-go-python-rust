r = open('input.txt').read().strip('\n')
input = r.splitlines()

#Part 1
def collisions(terrain, rise, run):
    hit = 0
    x = 0
    y = 0
    while True:
        y = y + rise
        if y >= len(terrain):
            break
        x = (x + run) % len(terrain[y])
        if terrain[y][x] == '#':
            hit = hit + 1
    return hit

print(collisions(input, 1, 3))

#Part 2
acc = 1
for slopes in [[1,1],[1,3],[1,5],[1,7],[2,1]]:
    acc = acc * collisions(input,slopes[0],slopes[1])

print(acc)