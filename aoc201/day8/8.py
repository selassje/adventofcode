import itertools


def string_to_char_set(str):
    return set(list(str))


def segments_to_digit(seg):
    set_seg = string_to_char_set(seg)
    if set_seg == set(["a", "b", "c", "e", "f", "g"]):
        return 0
    if set_seg == set(["c", "f"]):
        return 1
    if set_seg == set(["a", "c", "d", "e", "g"]):
        return 2
    if set_seg == set(["a", "c", "d", "f", "g"]):
        return 3
    if set_seg == set(["b", "c", "d", "f"]):
        return 4
    if set_seg == set(["a", "b", "d", "f", "g"]):
        return 5
    if set_seg == set(["a", "b", "d", "e", "f", "g"]):
        return 6
    if set_seg == set(["a", "c", "f"]):
        return 7
    if set_seg == set(["a", "b", "c", "d", "e", "f", "g"]):
        return 8
    if set_seg == set(["a", "b", "c", "d", "f", "g"]):
        return 9
    return None


class Entry:
    def __init__(self) -> None:
        self.patterns = [set() for _ in range(10)]
        self.digits = [set() for _ in range(4)]


segment_count_to_digits = [[] for _ in range(8)]
segment_count_to_digits[0] = []
segment_count_to_digits[1] = []
segment_count_to_digits[2] = [1]
segment_count_to_digits[3] = [7]
segment_count_to_digits[4] = [4]
segment_count_to_digits[5] = [2, 3, 5]
segment_count_to_digits[6] = [0, 6, 9]
segment_count_to_digits[7] = [8]


entries = []
f = open("input.txt")
for line in f.readlines():
    entry = Entry()
    splitted = line.split(" | ")
    for (i, word) in enumerate(splitted[0].split(" ")):
        entry.patterns[i] = string_to_char_set(word)
    for (i, word) in enumerate(splitted[1].split(" ")):
        word = word.strip()
        entry.digits[i] = string_to_char_set(word)
    entries.append(entry)

unique_digits_count = 0
for e in entries:
    for d in e.digits:
        if len(segment_count_to_digits[len(d)]) == 1:
            unique_digits_count += 1

print(unique_digits_count)

permutations = list(itertools.permutations(["a", "b", "c", "d", "e", "f", "g"]))


def apply_permutation(signal, perm):
    permuted = ""
    for c in signal:
        permuted += perm[ord(c) - ord("a")]
    return permuted


def check_permutation(entry, perm):
    for pattern in entry.patterns:
        permuted = apply_permutation(pattern, perm)
        if segments_to_digit(permuted) == None:
            return False
    return True


def decode_entry(entry):
    for perm in permutations:
        if check_permutation(entry, perm):
            value = 0
            for i in range(4):
                permuted = apply_permutation(e.digits[i], perm)
                d = segments_to_digit(permuted)
                value += d * pow(10, 3 - i)
            return value


decoded_sum = 0
for e in entries:
    decoded_sum += decode_entry(e)
print(decoded_sum)
