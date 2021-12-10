import re

initial_state = list(map(int, open("input.txt").readline().split(",")))


def calc_number_after(days):
    count = [0 for _ in range(9)]
    for i in initial_state:
        count[i] += 1
    for _ in range(days):
        old_count_0 = count[0]
        for i in range(8):
            count[i] = count[i + 1]
        count[8] = old_count_0
        count[6] += old_count_0
    return sum(count)


print(calc_number_after(80))
print(calc_number_after(256))
