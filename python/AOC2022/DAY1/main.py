# (base) D:\1.program\python\python2\offensive-go-python-rust\golang\AOC2022\DAY1>python -i main.py input.txt
# part 1: 69883
# part 2:
# >>> len(largest)
# 243
# >>> largest[0]
# 69883
# >>> largest[1]
# 69727
# >>> largest[2]
# 67966

import sys

with open(sys.argv[1], 'r') as f:
    data = f.read().strip()

elves = data.split('\n\n')

largest = [0,0,0]

for elf in elves:
    total = sum(int(x) for x in elf.split('\n') if x)
    # if total > largest:
    #     largest = total
    largest = sorted(largest + [total], reverse=True)[:3]

print(f'part 1: {largest[0]}')
print(f'part 2: {sum(largest)}')

# one liner
totals = sorted([sum(map(int, elf.split('\n'))) for elf in elves], reverse=True)
print(f'part 1: {totals[0]}')
print(f'part 2: {sum(totals[:3])}')
