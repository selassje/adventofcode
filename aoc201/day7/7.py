import sys

initial_positions = list(map(int, open("input.txt").readline().split(",")))
crabs_count = len(initial_positions)

minFuel2 = sys.maxsize
minFuel = sys.maxsize

for i in range(crabs_count):
    fuel = 0
    fuel2 = 0
    for crab in initial_positions:
        n = abs(crab - i)
        fuel += n
        fuel2 += int((n * (n + 1)) / 2)
    minFuel = min(minFuel, fuel)
    minFuel2 = min(minFuel2, fuel2)

print(minFuel)
print(minFuel2)
