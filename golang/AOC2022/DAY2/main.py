import sys

scores = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

scores2 = {
    "A X": 3 + 0, # Scissors, lose
    "A Y": 1 + 3, # rock, draw
    "A Z": 2 + 6, # paper, win
    "B X": 1 + 0, # rock, lose
    "B Y": 2 + 3, # paper, draw
    "B Z": 3 + 6, # Scissors, win
    "C X": 2 + 0, # paper, lose
    "C Y": 3 + 3, # Scissors, draw
    "C Z": 1 + 6, # rock, win
}

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

part1 = sum([scores[l.strip()] for l in lines])
print(f'part 1: {part1}')

part2 = sum([scores2[l.strip()] for l in lines])
print(f'part 2: {part2}')
