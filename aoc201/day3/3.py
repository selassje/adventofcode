import re


def get_ones_count(reports):
    ones_count = [0 for _ in range(bit_len)]
    for r in reports:
        for i in range(bit_len):
            if r[i] == "1":
                ones_count[i] += 1
    return ones_count


def filter_by_prefix(prefix, reports):
    result = []
    rep = str(bit_len - len(prefix))
    pattern = prefix + r"[1|0]{" + rep + r"}"
    for r in reports:
        if re.match(pattern, r) is not None:
            result.append(r)
    return result


f = open("input.txt")

reports = f.read().splitlines()
bit_len = len(reports[0])
reports_count = len(reports)
reports_count_half = reports_count / 2
ones_count = get_ones_count(reports)

gamma = 0
epsilon = 0

for i in range(bit_len):
    if ones_count[i] > reports_count_half:
        gamma += pow(2, bit_len - 1 - i)
    else:
        epsilon += pow(2, bit_len - 1 - i)

print(gamma * epsilon)


def calc_oxygen_or_co2(is_oxygen):
    prefix = ""
    filtered_reports = reports
    ones_count_filtered = ones_count
    reports_count_half_filtered = reports_count_half
    for i in range(bit_len):
        if (ones_count_filtered[i] >= reports_count_half_filtered and is_oxygen) or (
            ones_count_filtered[i] < reports_count_half_filtered and not is_oxygen
        ):
            prefix += "1"
        else:
            prefix += "0"
        filtered_reports = filter_by_prefix(prefix, filtered_reports)
        ones_count_filtered = get_ones_count(filtered_reports)
        reports_count_half_filtered = len(filtered_reports) / 2
        if len(filtered_reports) == 1:
            return int(filtered_reports[0], 2)


print(calc_oxygen_or_co2(True) * calc_oxygen_or_co2(False))
