import sys



target_x = (137, 171)
target_y = (-98, -73)

def get_position(init_vx, init_vy, step):
    pos = lambda init_v, s: (init_v * s) - int((s * (s - 1)) / 2)
    final_y = pos(init_vy, step)
    if step < init_vx:
        final_x = pos(init_vx, step)
    else:
        final_x = pos(init_vx, init_vx)
    return final_x, final_y


def get_max_y(init_vy):
    _, max_y = get_position(0, init_vy, init_vy)
    if init_vy <= 0:
        max_y = 0
    return max_y


def is_valid(init_vx, init_vy, x_range, y_range):
    (min_x, max_x) = x_range
    (min_y, max_y) = y_range
    x = 0
    y = 0
    while True:
        if x in range(min_x, max_x + 1) and y in range(min_y, max_y + 1):
            return True
        if x > max_x:
            return False
        if y < min_y and init_vy <= 0:
            return False
        x += init_vx
        y += init_vy
        if init_vx > 0:
            init_vx -= 1
        init_vy -= 1


max_y = -sys.maxsize
valid_count = 0

for x in range(0, target_x[1] + 1):
    for y in range(-1000, 1000):
        if is_valid(x, y, target_x, target_y):
            valid_count += 1
            max_y = max(max_y, get_max_y(y))

print(max_y, valid_count)
