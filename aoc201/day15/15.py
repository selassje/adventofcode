import sys

cavern = []
f = open("input.txt")
for line in f.readlines():
    line = line.strip()
    cavern.append(list(map(int, line)))

h = len(cavern)
w = len(cavern[0])


def get_risk_level(x, y):
    tile_x = int(x / w)
    tile_y = int(y / h)
    in_tile_x = x % w
    in_tile_y = y % h
    orig_risk = cavern[in_tile_y][in_tile_x]
    risk = orig_risk + tile_x + tile_y
    if risk > 9:
        risk -= 9
    return risk


def find(q, x, y):
    for (i, j, _) in q:
        if i == x and y == j:
            return True
    return False


def update(q, x, y, newd):
    for (i, j, d) in q:
        if i == x and y == j:
            q.remove((i, j, d))
            break
    q.append((x, y, newd))


def dijsktra(w, h):
    d = [[sys.maxsize for _ in range(w)] for _ in range(h)]
    d[0][0] = 0
    q = []
    for x in range(w):
        for y in range(h):
            q.append((x, y, d[y][x]))
    q.sort(key=lambda x: x[2], reverse=True)

    while len(q) > 0:
        (x, y, _) = q.pop()
        for i, j in [(-1, 0), (1, 0), (-1, -1), (0, 1)]:
            ix = x + i
            jy = y + j
            if find(
                q,
                ix,
                jy,
            ):
                alt = d[y][x] + get_risk_level(jy, ix)
                if alt < d[jy][ix]:
                    update(q, ix, jy, alt)
                    d[jy][ix] = alt

        q.sort(key=lambda x: x[2], reverse=True)
    return d[-1][-1]


print(dijsktra(w, h))
print(dijsktra(w * 5, h * 5))
