f = open("input.txt")
image = []
algorithm = f.readline()
f.readline()
for line in f.readlines():
    line = line.strip()
    image.append(list(line))


def print_image(image):
    h = len(image)
    w = len(image[0])
    for y in range(h):
        for x in range(w):
            print(image[y][x], end="")
        print()
    print()


def get_pixel(image, x, y):
    if y in range(0, len(image)) and x in range(0, len(image[0])):
        return image[y][x] == "#"
    return False


def get_algorithm_index(image, x, y):
    index = 0
    for ny in range(y - 1, y + 2):
        for nx in range(x - 1, x + 2):
            index <<= 1
            if get_pixel(image, nx, ny):
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


def enhance_image(image, algorithm):
    margin = 3
    h = len(image) + 2 * margin
    w = len(image[0]) + 2 * margin
    enhanced = [["." for _ in range(w)] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            enhanced[y][x] = algorithm[
                get_algorithm_index(image, x - margin, y - margin)
            ]
    return enhanced


print(algorithm)

for _ in range(2):
    image = enhance_image(image, algorithm)
    print_image(image)

print(count_lit_pixels(image))
