import sys

f = open("input.txt")
polymer = f.readline().strip()
formulas = {}
f.readline()
for line in f.readlines():
    splitted = line.split(" -> ")
    formulas[splitted[0]] = splitted[1].strip()


def insert():
    new_polymer = polymer[0]
    for i in range(1, len(polymer)):
        f = polymer[i - 1]
        s = polymer[i]
        if f + s in formulas:
            new_polymer += formulas[f + s] + s
        else:
            new_polymer += s
    return new_polymer


def calc_max_min_diff():
    count = {}
    for c in polymer:
        count[c] = count.get(c, 0) + 1
    max_count = 0
    min_count = sys.maxsize
    for cnt in count.values():
        max_count = max(cnt, max_count)
        min_count = min(cnt, min_count)
    return max_count - min_count


for _ in range(10):
    polymer = insert()

print(calc_max_min_diff())
