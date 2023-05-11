import sys


def find_item(elf):
    front, back = elf[len(elf) // 2 :], elf[: len(elf) // 2]
    for item in front:
        if item in back:
            return item


def score(item):
    if "a" <= item <= "z":
        return ord(item) - ord("a") + 1
    return ord(item) - ord("A") + 27


with open(sys.argv[1], "r") as f:
    lines = f.readlines()

# part1 = 0
# for elf in lines:
#     item = find_item(elf)
#     part1 += score(item)
part1 = sum(score(find_item(elf)) for elf in lines)

print(f"part 1: {part1}")

# i = 0
# part2 = 0
# while i < len(lines):
#     for c in lines[i]:
#         if c in lines[i+1] and c in lines[i+2]:
#             part2 += score(c)
#             break
#     i += 3

part2 = sum(
    [
        score([badge for badge in team[0] if badge in team[1] and badge in team[2]][0])
        for team in zip(*(iter(lines),) * 3)
    ]
)

print(f"part 2: {part2}")
