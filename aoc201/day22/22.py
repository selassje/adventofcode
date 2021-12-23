import re

import sys


def get_overlapp_1d(range_1, range_2):
    s1, e1 = range_1
    s2, e2 = range_2

    assert s1 <= e1
    assert s2 <= e2

    if e1 < s2 or e2 < s1:
        return None

    if s1 in range(s2, e2 + 1) and e1 in range(s2, e2 + 1):
        return (s1, e1)

    if s2 in range(s1, e1 + 1) and e2 in range(s1, e1 + 1):
        return (s2, e2)

    if e1 in range(s2, e2 + 1):
        return (s2, e1)
    assert e2 in range(s1, e1 + 1)
    return (s1, e2)


class Cuboid:
    def __init__(self, top_left, bottom_right) -> None:
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.on = False

    def get_size_x(self):
        return self.bottom_right[0] - self.top_left[0] + 1

    def get_size_y(self):
        return self.top_left[1] - self.bottom_right[1] + 1

    def get_size_z(self):
        return self.top_left[2] - self.bottom_right[2] + 1

    def get_volume(self):
        if (
            self.top_left[0] > self.bottom_right[0]
            or self.top_left[1] < self.bottom_right[1]
            or self.top_left[2] < self.bottom_right[2]
        ):
            return 0

        return self.get_size_x() * self.get_size_y() * self.get_size_z()

    def __eq__(self, __o: object) -> bool:
        for i in range(3):
            if self.top_left[i] != __o.top_left[i]:
                return False
        for i in range(3):
            if self.bottom_right[i] != __o.bottom_right[i]:
                return False
        return True

    def __str__(self) -> str:
        _str = "on " if self.on else "off "
        _str += (
            str(self.top_left)
            + " "
            + str(self.bottom_right)
            + " V:"
            + str(self.get_volume())
        )
        return _str


def find_overlapp(c1, c2):
    x_range_1 = (c1.top_left[0], c1.bottom_right[0])
    y_range_1 = (c1.bottom_right[1], c1.top_left[1])
    z_range_1 = (c1.bottom_right[2], c1.top_left[2])
    x_range_2 = (c2.top_left[0], c2.bottom_right[0])
    y_range_2 = (c2.bottom_right[1], c2.top_left[1])
    z_range_2 = (c2.bottom_right[2], c2.top_left[2])

    x_overlapp = get_overlapp_1d(x_range_1, x_range_2)
    y_overlapp = get_overlapp_1d(y_range_1, y_range_2)
    z_overlapp = get_overlapp_1d(z_range_1, z_range_2)

    if x_overlapp is not None and y_overlapp is not None and z_overlapp is not None:
        top_left = (x_overlapp[0], y_overlapp[1], z_overlapp[1])
        bottom_right = (x_overlapp[1], y_overlapp[0], z_overlapp[0])
        return Cuboid(top_left, bottom_right)
    return None


def cut_out_sub_cuboid(target, sub_cuboid):
    remaining = []

    def add_if_not_empty(x):
        if x.get_volume() != 0:
            remaining.append(x)
            return True

    above = Cuboid(
        target.top_left,
        (target.bottom_right[0], target.bottom_right[1], sub_cuboid.top_left[2] + 1),
    )

    below = Cuboid(
        (target.top_left[0], target.top_left[1], sub_cuboid.bottom_right[2] - 1),
        target.bottom_right,
    )

    add_if_not_empty(above)
    add_if_not_empty(below)
    top = sub_cuboid.top_left[2]
    bottom = sub_cuboid.bottom_right[2]

    if (
        target.top_left[0] <= sub_cuboid.top_left[0]
        and target.top_left[1] >= sub_cuboid.top_left[1]
        and target.top_left[2] >= sub_cuboid.top_left[2]
        and target.bottom_right[0] >= sub_cuboid.bottom_right[0]
        and target.bottom_right[1] <= sub_cuboid.bottom_right[1]
        and target.bottom_right[2] <= sub_cuboid.bottom_right[2]
    ):
        beside_left = Cuboid(
            (
                target.top_left[0],
                target.top_left[1],
                top,
            ),
            (sub_cuboid.top_left[0] - 1, target.bottom_right[1], bottom),
        )
        add_if_not_empty(beside_left)
        beside_right = Cuboid(
            (
                sub_cuboid.bottom_right[0] + 1,
                target.top_left[1],
                top,
            ),
            (target.bottom_right[0], target.bottom_right[1], bottom),
        )
        add_if_not_empty(beside_right)

        beside_down = Cuboid(
            (
                sub_cuboid.top_left[0],
                sub_cuboid.bottom_right[1] - 1,
                top,
            ),
            (
                sub_cuboid.bottom_right[0],
                target.bottom_right[1],
                bottom,
            ),
        )
        add_if_not_empty(beside_down)

        beside_up = Cuboid(
            (
                sub_cuboid.top_left[0],
                target.top_left[1],
                top,
            ),
            (sub_cuboid.bottom_right[0], sub_cuboid.top_left[1] + 1, bottom),
        )
        add_if_not_empty(beside_up)
        for r in remaining:
            r.on = target.on
        return remaining
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
            top,
        ),
        (target.bottom_right[0], target.bottom_right[1], bottom),
    )
    if add_if_not_empty(beside):
        remaining_beside_bottom_right[1] = sub_cuboid.top_left[1]
    beside = Cuboid(
        (
            target.top_left[0],
            sub_cuboid.top_left[1],
            top,
        ),
        (
            sub_cuboid.top_left[0],
            sub_cuboid.top_left[1],
            bottom,
        ),
    )
    if add_if_not_empty(beside):
        remaining_beside_bottom_right[1] = sub_cuboid.top_left[1]

    beside = Cuboid(
        (
            target.top_left[0],
            target.top_left[1],
            top,
        ),
        (sub_cuboid.top_left[0], sub_cuboid.bottom_right[1], bottom),
    )
    if add_if_not_empty(beside):
        remaining_beside_top_left[1] = sub_cuboid.bottom_right[1]
    beside = Cuboid(
        (
            sub_cuboid.bottom_right[0],
            target.top_left[1],
            top,
        ),
        (
            target.bottom_right[0],
            sub_cuboid.bottom_right[1],
            bottom,
        ),
    )
    if add_if_not_empty(beside):
        remaining_beside_top_left[1] = sub_cuboid.bottom_right[1]
    beside = Cuboid(
        (
            target.top_left[0],
            target.top_left[1],
            top,
        ),
        (sub_cuboid.bottom_right[0], sub_cuboid.top_left[1], bottom),
    )
    if add_if_not_empty(beside):
        remaining_beside_top_left[0] = sub_cuboid.bottom_right[0]
    beside = Cuboid(
        (
            target.top_left[0],
            sub_cuboid.bottom_right[1],
            top,
        ),
        (
            sub_cuboid.bottom_right[0],
            target.bottom_right[1],
            bottom,
        ),
    )
    if add_if_not_empty(beside):
        remaining_beside_top_left[0] = sub_cuboid.bottom_right[0]

    beside = Cuboid(
        (
            sub_cuboid.top_left[0],
            target.top_left[1],
            top,
        ),
        (target.bottom_right[0], sub_cuboid.top_left[1], bottom),
    )
    if add_if_not_empty(beside):
        remaining_beside_bottom_right[0] = sub_cuboid.top_left[0]
    beside = Cuboid(
        (
            sub_cuboid.top_left[0],
            sub_cuboid.bottom_right[1],
            top,
        ),
        (
            target.bottom_right[0],
            target.bottom_right[1],
            bottom,
        ),
    )
    if add_if_not_empty(beside):
        remaining_beside_bottom_right[0] = sub_cuboid.top_left[0]
    add_if_not_empty(Cuboid(remaining_beside_top_left, remaining_beside_bottom_right))

    for r in remaining:
        r.on = target.on
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


min_x = sys.maxsize
min_y = sys.maxsize
min_z = sys.maxsize
max_x = -sys.maxsize
max_y = -sys.maxsize
max_z = -sys.maxsize

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
    min_x = min(min_x, x[0])
    min_y = min(min_y, y[0])
    min_z = min(min_z, z[0])
    max_x = max(max_x, x[1])
    max_y = max(max_y, y[1])
    max_z = max(max_z, z[1])
    commands.append(Command(enabled, x, y, z))


def solve(x_range, y_range, z_range):
    top_left = (x_range[0], y_range[1], z_range[1])
    bottom_right = (x_range[1], y_range[0], z_range[0])

    cuboids = [Cuboid(top_left, bottom_right)]
    total_volume = cuboids[0].get_volume()
    for com in commands:
        incoming_cuboid = Cuboid(
            (com.x[0], com.y[1], com.z[1]), (com.x[1], com.y[0], com.z[0])
        )
        #   print("incoming " + str(incoming_cuboid))
        cuboids_to_add = []
        cuboids_to_remove = []
        for cub in cuboids:
            overlapp = find_overlapp(cub, incoming_cuboid)
            # print("overlapp " + str(overlapp))
            if overlapp is not None:
                if overlapp == cub:
                    cub.on = com.on
                elif com.on != cub.on:
                    overlapp.on = com.on
                    cuboids_to_add.append(overlapp)
                    remaining = cut_out_sub_cuboid(cub, overlapp)
                    cuboids_to_add += remaining
                    cuboids_to_remove.append(cub)
        for r in cuboids_to_remove:
            cuboids.remove(r)
        cuboids += cuboids_to_add

        volume = 0
        # for c in cuboids:
        #     volume += c.get_volume()
        #     print(c)
        # print()
        #  print(total_volume, volume)
        # assert total_volume == volume
        # return 0

    result = 0
    for cub in cuboids:
        if cub.on:
            result += cub.get_volume()
    return result


print(solve((-50, 50), (-50, 50), (-50, 50)))
# print(solve((min_x, max_x), (min_y, max_y), (min_z, max_z)))
