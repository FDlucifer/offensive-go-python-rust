import sys

with open(sys.argv[1]) as f:
    lines = f.readlines()

numbers = list(map(int, lines[0].split(",")))

boards = []
board = []
cols = [[], [], [], [], []]

for line in lines[2:]:
    if line.strip():
        line_nums = list(map(int, line.split()))
        board.append(line_nums)
        cols = [[*x[0], x[1]] for x in list(zip(cols, line_nums))]
    else:
        board += cols
        boards.append(board)
        board = []
        cols = [[], [], [], [], []]
if line.strip():
    board += cols
    boards.append(board)

has_win = [False for _ in boards]


def check_board(nums, board):
    for row in board:
        if all([n in nums for n in row]):
            return sum([j for i in board[:5] for j in i if j not in nums]) * nums[-1]
    return False


win = False
for i in range(5, len(numbers)):
    for j, board in enumerate(boards):
        if has_win[j]:
            continue
        score = check_board(numbers[:i], board)
        if score:
            has_win[j] = True
            if all(has_win):
                score = check_board(numbers[:i], board)
                print(f"part 2: {score}")
            if not win:
                print(f"part 1: {score}")
                win = True
