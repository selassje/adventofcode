f = open("input.txt")
depths = list(map(int, f.read().splitlines()))

increaseCount = 0
increaseCountThree = 0

for i in range(1, len(depths)):
    if depths[i] > depths[i - 1]:
        increaseCount += 1

for i in range(3, len(depths)):
    if depths[i] > depths[i - 3]:
        increaseCountThree += 1


print(increaseCount)
print(increaseCountThree)
