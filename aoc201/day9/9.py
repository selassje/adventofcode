from enum import Enum

heightmap = []
f = open("input.txt")
for line in f.readlines():
    line = line.strip()
    heightmap.append(list(map(int, line)))


def is_lowpoint(heightmap, x, y):
    value = heightmap[y][x]
    if x > 0 and heightmap[y][x - 1] <= value:
        return False
    if x < len(heightmap[0]) - 1 and heightmap[y][x + 1] <= value:
        return False
    if y > 0 and heightmap[y - 1][x] <= value:
        return False
    if y < len(heightmap) - 1 and heightmap[y + 1][x] <= value:
        return False
    return True


class State(Enum):
    IN_BASIN = 0
    NOT_IN_BASIN = 1
    UNCHECKED = 2


def scan_basin(heightmap, state_map, x, y):
    if state_map[y][x] != State.UNCHECKED:
        return 0
    count = 0
    height = heightmap[y][x]
    if height != 9:
        state_map[y][x] = State.IN_BASIN
        count += 1
        if x > 0:
            count += scan_basin(heightmap, state_map, x - 1, y)
        if x < len(heightmap[0]) - 1:
            count += scan_basin(heightmap, state_map, x + 1, y)
        if y > 0:
            count += scan_basin(heightmap, state_map, x, y - 1)
        if y < len(heightmap) - 1:
            count += scan_basin(heightmap, state_map, x, y + 1)
    else:
        state_map[y][x] = State.NOT_IN_BASIN
    return count


basins = []
risk_level_sum = 0
for (y, row) in enumerate(heightmap):
    for (x, v) in enumerate(row):
        if is_lowpoint(heightmap, x, y):
            state_map = [
                [State.UNCHECKED for _ in range(len(heightmap[0]))]
                for _ in range(len(heightmap))
            ]
            risk_level_sum += heightmap[y][x] + 1
            basins.append(scan_basin(heightmap, state_map, x, y))

print(risk_level_sum)

basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
