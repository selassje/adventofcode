import re

from copy import deepcopy


def get_overlapp_1d(range_1, range_2):
    s1, e1 = range_1
    s2, e2 = range_2

    assert s1 <= e1
    assert s2 <= e2

    if e1 < s2 or e1 < s1:
        return None

    if e1 in range(s2, e2 + 1):
        return (s2, e1)
    assert e2 in range(s1, e1 + 1)
    return (s1, e2)


class Cuboid:
    def __init__(self, top_left, bottom_right) -> None:
        self.top_left = top_left
        self.bottom_right = bottom_right

    def get_size_x(self):
        return self.bottom_right[0] - self.top_left[0]

    def get_size_y(self):
        return self.top_left[1] - self.bottom_right[1]

    def get_size_z(self):
        return self.top_left[2] - self.bottom_right[2]

    def get_volume(self):
        if (
            self.top_left[0] > self.bottom_right[0]
            or self.top_left[1] > self.bottom_right[1]
            or self.top_left[2] < self.bottom_right[2]
        ):
            return 0

        return self.get_size_x() * self.get_size_y() * self.get_size_z()


def cut_out_sub_cuboid(target, sub_cuboid):
    remaining = []

    def add_if_not_empty(x):
        if x.get_volume() != 0:
            remaining.append(x)
            return True

    above = Cuboid(
        target.top_left,
        (target.bottom_right[0], target.bottom_right[1], sub_cuboid.top_left[2]),
    )

    below = Cuboid(
        (target.top_left[0], target.top_left[1], sub_cuboid.bottom_right[2]),
        target.bottom_right,
    )

    top = sub_cuboid.top_left[2]
    bottom = sub_cuboid.bottom_right[2]

    remaining_beside_top_left = [target.top_left[0], target.top_left[1], top]
    remaining_beside_bottom_right = [
        target.bottom_right[0],
        target.bottom_right[1],
        bottom,
    ]
    beside = Cuboid(
        (
            sub_cuboid.bottom_right[0],
            sub_cuboid.bottom_right[1],
            sub_cuboid.top_left[2],
        ),
        (target.bottom_right[0], target.bottom_right[1], sub_cuboid.bottom_right[2]),
    )
    if add_if_not_empty(beside):
        remaining_beside_bottom_right[1] = sub_cuboid.top_left[1]
    beside = Cuboid(
        (
            target.top_left[0],
            sub_cuboid.top_lef[1],
            sub_cuboid.top_left[2],
        ),
        (
            sub_cuboid.top_left[0],
            sub_cuboid.top_left[1],
            sub_cuboid.bottom_right[2],
        ),
    )
    if add_if_not_empty(beside):
        remaining_beside_bottom_right[1] = sub_cuboid.top_left[1]
    
    add_if_not_empty(above)
    add_if_not_empty(below)
    add_if_not_empty(Cuboid(remaining_beside_top_left,remaining_beside_bottom_right))
    return remaining


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
