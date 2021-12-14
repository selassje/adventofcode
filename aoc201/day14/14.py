f = open("example.txt")
polymer = f.readline()
formulas = {}
f.readline()
for line in f.readlines():
    splitted = line.split(" -> ")
    formulas[splitted[0]] = splitted[1].strip()

print(polymer)
print(formulas)

def insert():
    new_polymer = ""
    for i in range(1,len(polymer)):
        f = polymer[i - 1]
        s = polymer[i]
        if f + s in formulas:
            new_polymer += f + formulas[f+s] + s
        else:
            new_polymer += f + s
    return new_polymer

for _ in range(10):
    polymer = insert()
    print()
