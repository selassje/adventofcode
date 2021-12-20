f = open("input.txt")
image = []
algorithm = f.readline()
f.readline()
for line in f.readlines():
    line = line.strip()
    image.append(list(line))


def get_pixel(image, x, y, outside_pixel):
    if y in range(0, len(image)) and x in range(0, len(image[0])):
        return image[y][x] == "#"
    return outside_pixel


def get_algorithm_index(image, x, y, outside_pixel):
    index = 0
    for ny in range(y - 1, y + 2):
        for nx in range(x - 1, x + 2):
            index <<= 1
            if get_pixel(image, nx, ny, outside_pixel):
                index |= 1
    return index


def count_lit_pixels(image):
    h = len(image)
    w = len(image[0])
    result = 0
    for y in range(h):
        for x in range(w):
            if image[y][x] == "#":
                result += 1
    return result


def enhance_image(image, algorithm, outside_pixel):
    margin = 3
    h = len(image) + 2 * margin
    w = len(image[0]) + 2 * margin
    enhanced = [["." for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            enhanced[y][x] = algorithm[
                get_algorithm_index(image, x - margin, y - margin, outside_pixel)
            ]
    return enhanced


outside_pixel = False
toggle_outside_pixel = algorithm[0] == "#"
for step in range(50):
    image = enhance_image(image, algorithm, outside_pixel)
    if toggle_outside_pixel:
        outside_pixel = not outside_pixel
    if step == 1 or step == 49:
        print(count_lit_pixels(image))
