packet = open("example.txt").readline()
packet = str(bin(int(packet, 16)))[2:]
print(packet)


def read_bits(packet, start, length):
    return int(packet[start : start + length], 2)


def get_version(packet):
    return read_bits(packet, 0, 3)


def get_type(packet):
    return read_bits(packet, 3, 3)


def get_literal_value(packet):
    next_group_start = 6
    bit_string = ""
    while True:
        bit_string += packet[next_group_start + 1: next_group_start + 5]
        if packet[next_group_start] == "0":
            break
        next_group_start += 5
    return int(bit_string,2)


print(get_version(packet))
print(get_type(packet))
print(get_literal_value(packet))
