from enum import Enum
import re


def print_pattern():
    for row in pattern:
        for dot in row:
            if dot:
                print("#", end="")
            else:
                print(".", end="")
        print("")
    print()


def count_dots():
    result = 0
    for row in pattern:
        for dot in row:
            if dot:
                result += 1
    return result


def fold_left(x):
    global h
    global w
    folded_count = x
    new_cols = 0 if (w - x) - x > 0 else abs((w - x) - x)
    for _ in range(new_cols):
        for y in range(h):
            pattern[y].append(False)
    for x2 in range(folded_count):
        for y in range(h):
            pattern[y][x + x2 + 1] = pattern[y][x + x2 + 1] or pattern[y][x - x2 - 1]
    for _ in range(folded_count + 1):
        for y in range(h):
            pattern[y].pop(0)
    w -= folded_count + 1
    w += new_cols
    pass


def fold_up(y):
    global h
    global w
    folded_count = h - y - 1
    new_rows = 0 if y - folded_count > 0 else abs(y - folded_count)
    for _ in range(new_rows):
        pattern.insert(0, [False for _ in range(w)])
    for y2 in range(folded_count):
        for x in range(w):
            pattern[y - y2 - 1][x] = pattern[y - y2 - 1][x] or pattern[y + y2 + 1][x]
    for _ in range(folded_count + 1):
        pattern.pop()
    h -= folded_count + 1
    h += new_rows


class Command(Enum):
    FOLD_UP = 1
    FOLD_LEFT = 2


coordinates = []
commands = []
h = 0
w = 0
f = open("input.txt")
for line in f.readlines():
    if line != "\n":
        match = re.match("fold along y=(\d+)", line)
        if match != None:
            command = Command.FOLD_UP
            y = int(match.group(1))
            commands.append((command, y))
            continue
        match = re.match("fold along x=(\d+)", line)
        if match != None:
            command = Command.FOLD_LEFT
            x = int(match.group(1))
            commands.append((command, x))
            continue
        (x, y) = tuple(map(int, line.split(",")))
        w = max(w, x)
        h = max(h, y)
        coordinates.append((x, y))
h += 1
w += 1

pattern = [[False for _ in range(w)] for _ in range(h)]
for (x, y) in coordinates:
    pattern[y][x] = True
# print_pattern()
for i, cmd in enumerate(commands):
    (c, v) = cmd
    if c == Command.FOLD_LEFT:
        fold_left(v)
    else:
        fold_up(v)
    if i == 0:
        print(count_dots())
