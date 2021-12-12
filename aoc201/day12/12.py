cavern_map = {}
caves = set()
f = open("example.txt")
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

print(cavern_map)
print(caves)

cave_visit_map = {k: False for k in caves}


def find_paths(cave, cave_visit_map):
    if cave.islower():
        cave_visit_map[cave] = True
    if cave == "end":
        return 1
    result = 0
    for n in cavern_map[cave]:
        if not cave_visit_map[n]:
            result += find_paths(n, cave_visit_map)
    return result


print(find_paths("start", cave_visit_map))
