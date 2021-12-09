import re


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"


class Line:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.start = Point(x1, y1)
        self.end = Point(x2, y2)

    def __str__(self) -> str:
        return str(self.start) + " -> " + str(self.end)


maxX = 0
maxY = 0
f = open("input.txt")
lines = []
for line in f.read().splitlines():
    m = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line)
    if m is not None:
        x1 = int(m.group(1))
        y1 = int(m.group(2))
        x2 = int(m.group(3))
        y2 = int(m.group(4))
        maxX = max(maxX, x1, x2)
        maxY = max(maxY, y1, y2)
        lines.append(Line(x1, y1, x2, y2))
    else:
        exit(2)

diagram = [[0 for _ in range(maxX + 1)] for _ in range(maxY + 1)]
diagram2 = [[0 for _ in range(maxX + 1)] for _ in range(maxY + 1)]

for line in lines:
    if line.start.x == line.end.x:
        startY = min(line.start.y, line.end.y)
        endY = max(line.start.y, line.end.y)
        for y in range(startY, endY + 1):
            diagram[y][line.start.x] += 1
            diagram2[y][line.start.x] += 1
    elif line.start.y == line.end.y:
        startX = min(line.start.x, line.end.x)
        endX = max(line.start.x, line.end.x)
        for x in range(startX, endX + 1):
            diagram[line.start.y][x] += 1
            diagram2[line.start.y][x] += 1
    else:
        startX = min(line.start.x, line.end.x)
        endX = max(line.start.x, line.end.x)
        if startX == line.start.x:
            startPoint = line.start
            endPoint = line.end
        else:
            startPoint = line.end
            endPoint = line.start
        x = startPoint.x
        y = startPoint.y
        if startPoint.y <= endPoint.y:
            inc = 1
        else:
            inc = -1
        while True:
            diagram2[y][x] += 1
            if x == endPoint.x and y == endPoint.y:
                break
            x += 1
            y += inc

twosCount = 0
twosCount_2 = 0
for y in range(maxY + 1):
    for x in range(maxX + 1):
        if diagram[y][x] >= 2:
            twosCount += 1
        if diagram2[y][x] >= 2:
            twosCount_2 += 1
print(twosCount)
print(twosCount_2)
