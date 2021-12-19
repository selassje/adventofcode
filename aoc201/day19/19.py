def roll(v):
    return (v[0], v[2], -v[1])


def turn(v):
    return (-v[1], v[0], v[2])


def sequence(v):
    for _ in range(2):
        for _ in range(3):
            v = roll(v)
            yield (v)
            for i in range(3):
                v = turn(v)
                yield (v)
        v = roll(turn(roll(v)))


rotations = list(sequence((1, 1, 1)))


def sum_position(position_1, position_2):
    return [position_1[i] + position_2[i] for i in range(3)]


def deduct_position(position_1, position_2):
    return [position_1[i] - position_2[i] for i in range(3)]


class Scanner:
    def __init__(self, reports) -> None:
        self.reports = reports

    def __str__(self) -> str:
        result = "\n"
        for r in self.reports:
            result += "{0},{1},{2} \n".format(r[0], r[1], r[2])
        return result + "\n"

    def find(self, beacon):
        for r in self.reports:
            if r[0] == beacon[0] and r[1] == beacon[1] and r[2] == beacon[2]:
                return True
        return False

    def rotate_and_shift(self, rotation, center):
        beacons = self.get_reoriented_beacons(rotation)
        for i in range(len(beacons)):
            beacons[i] = sum_position(center, beacons[i])
        self.reports = beacons

    def rotate(self, rotation):
        beacons = self.get_reoriented_beacons(rotation)
        self.reports = beacons

    def get_reoriented_beacons(self, rotation):
        beacons = []
        for r in self.reports:
            beacon = [0 for _ in range(3)]
            x = list(sequence((r[0], r[1], r[2])))[rotation]
            # for i in range(3):
            #     #beacon[i] = r[i] * rotations[rotation][i]
            #     beacon[i] = sequence(())[rotation][i]
            beacons.append(x)
        return beacons


f = open("input.txt")

scanners = []
reports = []
for line in f.readlines():
    line = line.strip()
    if line != "":
        if line.find("scanner") != -1:
            scanners.append(Scanner(reports))
            reports = []
        else:
            reports.append(list(map(int, line.split(","))))
scanners.pop(0)
scanners.append(Scanner(reports))

# for s in scanners:
#     print(s)


def find_scanner_location(scanner_1, scanner_2, log):
    for rot in range(len(rotations)):
        beacons = scanner_2.get_reoriented_beacons(rot)
        for beacon_0 in scanner_1.reports:
            for beacon_1 in beacons:
                common_beacons = 0
                scanner_location = [beacon_0[i] - beacon_1[i] for i in range(3)]
                if scanner_location[0] == -88:
                    # print(scanner_location)
                    pass
                for _beacon_1 in beacons:
                    beacon_relative = sum_position(scanner_location, _beacon_1)
                    if scanner_1.find(beacon_relative):
                        common_beacons += 1
                if common_beacons >= 12:
                    print("rotation", rot)
                    scanner_2.rotate(rot)
                    return scanner_location
    return None


scanners_locations = {0: (0, 0, 0)}

while len(scanners_locations) != len(scanners):
    for i, s in enumerate(scanners):
        if i not in scanners_locations:
            for k, v in scanners_locations.items():
                scanner_location = find_scanner_location(
                    scanners[k], scanners[i], False
                )
                if scanner_location is not None:
                    print("lol")
                    scanners_locations[i] = sum_position(v, scanner_location)
                    break

unique_beacons = set()
for i, s in enumerate(scanners):
    for r in s.reports:
        unique_beacons.add(tuple(sum_position(scanners_locations[i], r)))

print(unique_beacons)
print(len(unique_beacons))
