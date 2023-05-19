import sys
from collections import deque


def mix(nums):
    for i in range(len_nums):
        while True:
            if nums[0][0] == i:
                break
            nums.append(nums.popleft())

        cur = nums.popleft()
        rotate_by = cur[1] % (len_nums - 1)
        for _ in range(rotate_by):
            nums.append(nums.popleft())
        nums.append(cur)

    return nums


def score_nums(nums):
    while nums[0][1] != 0:
        nums.append(nums.popleft())

    return sum(nums[c % len_nums][1] for c in [1000, 2000, 3000])


with open(sys.argv[1], "r") as f:
    numbers = list(map(int, f.readlines()))

nums = deque(enumerate(numbers))
len_nums = len(nums)
mums = mix(nums)
part1 = score_nums(nums)
print(f"part 1: {part1}")

nums2 = deque((i, n * 811589153) for i, n in enumerate(numbers))
for i in range(10):
    print(f"/r{i}", end='')
    nums2 = mix(nums2)
part2 = score_nums(nums2)
print(f"\rpart 2: {part2}")
