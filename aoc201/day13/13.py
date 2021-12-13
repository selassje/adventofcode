from enum import Enum
import enum
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


def fold_left(x):
    print("fold left")
    pass


def fold_up(y):
    print("fold_up")
    pass


class Command(Enum):
    FOLD_UP = 1
    FOLD_LEFT = 2


coordinates = []
commands = []
h = 0
w = 0

f = open("example.txt")
for line in f.readlines():
    if line != "\n":
        match = re.match("fold along y=(\d+)", line)
        if match != None:
            command = Command.FOLD_UP
            command.FOLD_UP.y = match.group(1)
            commands.append(command)
            continue
        match = re.match("fold along x=(\d+)", line)
        if match != None:
            command = Command.FOLD_LEFT
            command.FOLD_LEFT.x = match.group(1)
            commands.append(command)
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

for c in commands:
    if c == Command.FOLD_LEFT:
        fold_left(c.FOLD_LEFT.x)
    else:
        fold_up(c.FOLD_UP.y)
    print_pattern()
