import re


hor = 0
depth = 0

f = open("input.txt")
commands = f.read().splitlines()

for command in commands:
    match = re.match(r"forward (\d+)", command)
    if match is not None:
        hor += int(match.group(1))
    match = re.match(r"down (\d+)", command)
    if match is not None:
        depth += int(match.group(1))
    match = re.match(r"up (\d+)", command)
    if match is not None:
        depth -= int(match.group(1))

print(hor * depth)

hor = 0
depth = 0
aim = 0

for command in commands:
    match = re.match(r"forward (\d+)", command)
    if match is not None:
        depth += aim * int(match.group(1))
        hor += int(match.group(1))
    match = re.match(r"down (\d+)", command)
    if match is not None:
        aim += int(match.group(1))
    match = re.match(r"up (\d+)", command)
    if match is not None:
        aim -= int(match.group(1))

print(hor * depth)
