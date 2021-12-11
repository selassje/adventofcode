octopus_map = []
f = open("input.txt")
for line in f.readlines():
    line = line.strip()
    octopus_map.append(list(map(int, line)))


def print_map(octopus_map):
    for row in octopus_map:
        line = ""
        for energy in row:
            line += str(energy)
        print(line)
    print()


def flash(octopus_map, flash_map):
    h = len(octopus_map)
    w = len(octopus_map[0])
    for (y, row) in enumerate(octopus_map):
        for (x, energy) in enumerate(row):
            if energy > 9 and not flash_map[y][x]:
                if x > 0 and octopus_map[y][x - 1]:
                    octopus_map[y][x - 1] += 1
                if x < w - 1 and octopus_map[y][x + 1]:
                    octopus_map[y][x + 1] += 1
                if y > 0:
                    octopus_map[y - 1][x] += 1
                if y < h - 1:
                    octopus_map[y + 1][x] += 1
                if x > 0 and y > 0:
                    octopus_map[y - 1][x - 1] += 1
                if x > 0 and y < h - 1:
                    octopus_map[y + 1][x - 1] += 1
                if x < w - 1 and y > 0:
                    octopus_map[y - 1][x + 1] += 1
                if x < w - 1 and y < h - 1:
                    octopus_map[y + 1][x + 1] += 1
                flash_map[y][x] = True


def count_flashes(octopus_map):
    result = 0
    for row in octopus_map:
        for energy in row:
            if energy > 9:
                result += 1
    return result


def increase_energy(octopus_map):
    h = len(octopus_map)
    w = len(octopus_map[0])
    for y in range(h):
        for x in range(w):
            octopus_map[y][x] += 1


def clear_flashes(octopus_map):
    h = len(octopus_map)
    w = len(octopus_map[0])
    for y in range(h):
        for x in range(w):
            if octopus_map[y][x] > 9:
                octopus_map[y][x] = 0


total_flashes = 0
for _ in range(100):
    increase_energy(octopus_map)
    flashes = count_flashes(octopus_map)
    flash_map = [
        [False for _ in range(len(octopus_map[0]))] for _ in range(len(octopus_map))
    ]
    while True:
        flash(octopus_map, flash_map)
        new_flashes = count_flashes(octopus_map)
        if new_flashes == flashes:
            break
        flashes = new_flashes
    total_flashes += flashes
    clear_flashes(octopus_map)
print(total_flashes)
