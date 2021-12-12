import copy

cavern_map = {}
caves = set()
f = open("input.txt")
for line in f.readlines():
    splitted = line.split("-")
    cave_1 = splitted[0]
    cave_2 = splitted[1].strip()
    cave_1_neighbours = cavern_map.get(cave_1, list())
    cave_1_neighbours.append(cave_2)
    cavern_map[cave_1] = cave_1_neighbours
    cave_2_neighbours = cavern_map.get(cave_2, list())
    cave_2_neighbours.append(cave_1)
    cavern_map[cave_2] = cave_2_neighbours

    caves.add(cave_1)
    caves.add(cave_2)

cave_visit_map = {k: 1 for k in caves}
cave_visit_map_2 = {k: 2 for k in caves}
cave_visit_map_2["start"] = 1
cave_visit_map_2["end"] = 1


def find_paths(cave, cave_visit_map, path):
    if cave.islower():
        cave_visit_map[cave] -= 1
    path = path + "," + cave
    if cave == "end":
        print(path)
        return 1
    result = 0
    for n in cavern_map[cave]:
        if cave_visit_map[n] > 0:
            result += find_paths(n, copy.deepcopy(cave_visit_map), path)
    return result


def find_paths_2(cave, cave_visit_map, path, small_single_picked):
    if cave.islower():
        if cave_visit_map[cave] > 0:
            cave_visit_map[cave] -= 1
        elif cave not in ["start", "end"]:
            small_single_picked = True
    path = path + "," + cave
    if cave == "end":
        #  print(path)
        return 1
    result = 0
    for n in cavern_map[cave]:
        if cave_visit_map[n] > 0:
            result += find_paths_2(
                n,
                copy.deepcopy(cave_visit_map),
                path,
                copy.deepcopy(small_single_picked),
            )
        elif not small_single_picked and n.islower() and n not in ["start", "end"]:
            result += find_paths_2(
                n,
                copy.deepcopy(cave_visit_map),
                path,
                copy.deepcopy(small_single_picked),
            )
    return result


def solution_1():
    return find_paths("start", copy.deepcopy(cave_visit_map), "")


def solution_2():
    return find_paths_2("start", cave_visit_map, "", False)


# print(solution_1())
print(solution_2())
