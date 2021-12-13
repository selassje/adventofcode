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
    for x2 in range(x):
        for y in range(h):
            pattern[y][x - x2 - 1] = pattern[y][x - x2 - 1] or pattern[y][x + x2 + 1]
    for _ in range(x + 1):
        for y in range(h):
            pattern[y].pop()
    w -= x + 1


def fold_up(y):
    global h
    global w
    for y2 in range(y):
        for x in range(w):
            pattern[y - y2 - 1][x] = pattern[y - y2 - 1][x] or pattern[y + y2 + 1][x]
    for _ in range(y + 1):
        pattern.pop()
    h -= y + 1


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
for i, cmd in enumerate(commands):
    (c, v) = cmd
    if c == Command.FOLD_LEFT:
        fold_left(v)
    else:
        fold_up(v)
    if i == 0:
        print(count_dots())

print_pattern()
