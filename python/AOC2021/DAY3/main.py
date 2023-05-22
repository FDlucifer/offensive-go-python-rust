import sys
from collections import Counter

with open(sys.argv[1], "r") as f:
    lines = list(map(str.strip, f.readlines()))

gamma = int("".join([Counter(x).most_common(1)[0][0] for x in list(zip(*lines))]), 2)
epsilon = int(len(lines[0]) * "1", 2) - gamma

print(f"part 1: {gamma * epsilon}")


def filter(nums, pos, least=True):
    common = sorted(
        Counter([num[pos] for num in nums]).most_common(),
        key=lambda x: (x[1], x[0]),
        reverse=True,
    )[least][0]
    new_nums = [num for num in nums if num[pos] == common]
    if len(new_nums) == 1:
        return new_nums[0]
    return filter(new_nums, pos + 1, least)


o2 = int(filter(lines, 0, False), 2)
co2 = int(filter(lines, 0, True), 2)
print(f"part 2: {o2 * co2}")
