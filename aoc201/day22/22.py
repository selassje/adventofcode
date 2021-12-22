import re

from click import group


class Command:
    def __init__(self, on, x, y, z) -> None:
        self.on = on
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        _str = "on " if self.on else "off "
        _str += str(self.x) + " " + str(self.y) + " " + str(self.z)
        return _str


def count_enabled(grid):
    result = 0
    for base in grid:
        for row in base:
            for core in row:
                if core:
                    result += 1
    return result


def apply_command(grid, command):
    result = 0
    for z, base in enumerate(grid):
        for y, row in enumerate(base):
            for x, _ in enumerate(row):
                _x = x - 50
                _y = y - 50
                _z = z - 50
                if (
                    _z in range(command.z[0], command.z[1] + 1)
                    and _y in range(command.y[0], command.y[1] + 1)
                    and _x in range(command.x[0], command.x[1] + 1)
                ):
                    grid[z][y][x] = command.on
    return result


commands = []
f = open("input.txt")
for line in f.readlines():
    splitted = line.split(" ")
    enabled = True if splitted[0] == "on" else False
    match = re.match(
        "x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", splitted[1]
    )
    x = (int(match.group(1)), int(match.group(2)))
    y = (int(match.group(3)), int(match.group(4)))
    z = (int(match.group(5)), int(match.group(6)))
    commands.append(Command(enabled, x, y, z))


grid = [[[False for _ in range(101)] for _ in range(101)] for _ in range(101)]

for c in commands:
    apply_command(grid, c)


print(count_enabled(grid))
