import sys

with open('input.txt') as boardsFile:
    file = boardsFile.read().split("\n\n")

nums = []
boards = []

for item in file:
    if file.index(item) == 0:
        for number in file[0].split(sep=','):
            nums.append(int(number))
    else:
        boards.append(item)


def lconv(line):
    line = line.split(" ")
    for num in line:
        if num == '':
            line.remove(num)
        else:
            line[line.index(num)] = int(num)

    for num2 in line:
        if isinstance(num2, str):
            line[line.index(num2)] = int(num2)

    return line


def bconv(board):
    board = board.split("\n")
    for line in board:
        board[board.index(line)] = lconv(line)
    return board


for board in boards:
    boards[boards.index(board)] = bconv(board)


def sboard(board, num):
    for li in board:
        for nu in li:
            if nu == num:
                board[board.index(li)][li.index(nu)] = 999


def checkboard(board):
    def all(l):
        return l[0] == l[1] == l[2] == l[3] == l[4]

    for line in board:
        try:
            if all(line):
                return True
        except:
            print(f"error: {board}")

    for i in range(5):
        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[
                4][i]:
            return True

    return False

for x in boards:
    print(x)
    print("\n")

for n in nums:
    for b in boards:
        sboard(b, n)
        if checkboard(b):
            print(b)
            print(f"n is: {n}")
            sys.exit()
