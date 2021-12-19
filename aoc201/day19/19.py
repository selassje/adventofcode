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

    def get_reoriented_beacons(self, rotation):
        beacons = []
        for r in self.reports:
            beacon = [0 for _ in range(3)]
            for i in range(3):
                beacon[i] = r[i] * rotations[rotation][i]
            beacons.append(beacon)
        return beacons


f = open("example.txt")

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


def find_scanner_location(scanner_0, scanner):
    for rot in range(len(rotations)):
        beacons = scanner.get_reoriented_beacons(rot)
        for beacon_0 in scanner_0.reports:
            for beacon_1 in beacons:
                common_beacons = 0
                scanner_location = [beacon_0[i] - beacon_1[i] for i in range(3)]
                for _beacon_1 in beacons:
                    beacon_relative = sum_position(scanner_location, _beacon_1)
                    if scanner_0.find(beacon_relative):
                        common_beacons += 1
                if common_beacons >= 12:
                    return scanner_location
    assert 1 == 0


scanner_loc = find_scanner_location(scanners[0], scanners[1])
print(scanner_loc)
