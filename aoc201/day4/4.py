def read_board(f):
    board = []
    for _ in range(5):
        row = list(map(int, f.readline().split()))
        board.append(list(zip(row, [False for _ in range(5)])))
    return board


def mark_number(board, number):
    for i in range(5):
        for j in range(5):
            (n, _) = board[i][j]
            if n == number:
                board[i][j] = (n, True)


def sum_unmarked(board):
    result = 0
    for i in range(5):
        for j in range(5):
            (n, m) = board[i][j]
            if not m:
                result += n
    return result


def check_bingo(board):
    for col in range(5):
        result = True
        for row in range(5):
            (_, m) = board[row][col]
            result = result and m
        if result:
            return True
    for row in range(5):
        result = True
        for col in range(5):
            (_, m) = board[row][col]
            result = result and m
        if result:
            return True
    return False


f = open("input.txt")
numbers = list(map(int, f.readline().split(",")))
boards = []

first = False
while True:
    line = f.readline()
    if len(line) == 0:
        break
    b = read_board(f)
    boards.append(b)

binged_boards = set()
for n in numbers:
    for (i, b) in enumerate(boards):
        mark_number(b, n)
        if check_bingo(b):
            if not first:
                print(n * sum_unmarked(b))
                first = True
            binged_boards.add(i)
            if len(binged_boards) == len(boards):
                print(n * sum_unmarked(b))
                exit()
