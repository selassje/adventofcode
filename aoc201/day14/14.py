import copy

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
    max_count = list(count_single.values())[0]
    min_count = list(count_single.values())[0]
    for cnt in count_single.values():
        max_count = max(cnt, max_count)
        if cnt > 0:
            min_count = min(cnt, min_count)
    return max_count - min_count


count_single = {}
count_pairs = {}
for c in polymer:
    count_single[c] = count_single.get(c, 0) + 1
for i in range(1, len(polymer)):
    f = polymer[i - 1]
    s = polymer[i]
    count_pairs[f + s] = count_pairs.get(f + s, 0) + 1

for i in range(40):
    new_count_single = copy.deepcopy(count_single)
    new_count_pairs = copy.deepcopy(count_pairs)
    for pair, pair_cnt in count_pairs.items():
        if pair_cnt > 0 and pair in formulas:
            inserted = formulas[pair]
            new_count_single[inserted] = new_count_single.get(inserted, 0) + pair_cnt
            new_count_pairs[pair[0] + inserted] = (
                new_count_pairs.get(pair[0] + inserted, 0) + pair_cnt
            )
            new_count_pairs[inserted + pair[1]] = (
                new_count_pairs.get(inserted + pair[1], 0) + pair_cnt
            )
            new_count_pairs[pair] -= pair_cnt

    for k in list(new_count_pairs):
        if new_count_pairs[k] == 0:
            del new_count_pairs[k]
    count_single = new_count_single
    count_pairs = new_count_pairs

    if i == 9:
        print(calc_max_min_diff())

print(calc_max_min_diff())
