octopus_map = []
f = open("input.txt")
for line in f.readlines():
    line = line.strip()
    octopus_map.append(list(map(int, line)))

h = len(octopus_map)
w = len(octopus_map[0])


def flash(flash_map):
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


def count_flashes():
    result = 0
    for row in octopus_map:
        for energy in row:
            if energy > 9:
                result += 1
    return result


def increase_energy():
    for y in range(h):
        for x in range(w):
            octopus_map[y][x] += 1


def clear_flashes():
    for y in range(h):
        for x in range(w):
            if octopus_map[y][x] > 9:
                octopus_map[y][x] = 0


total_flashes = 0
step = 1
first_all_flashing_step = 0
first_all_flashing_step_reached = False
while step < 100 or not first_all_flashing_step_reached:
    increase_energy()
    flashes = count_flashes()
    flash_map = [[False for _ in range(w)] for _ in range(h)]
    while True:
        flash(flash_map)
        new_flashes = count_flashes()
        if new_flashes == flashes:
            break
        flashes = new_flashes
    if flashes == w * h and not first_all_flashing_step_reached:
        first_all_flashing_step = step
        first_all_flashing_step_reached = True
    if step <= 100:
        total_flashes += flashes
    clear_flashes()
    step += 1

print(total_flashes)
print(first_all_flashing_step)
