class Packet:
    version = 0
    type = 0
    subpackets = []


packet_raw = open("example.txt").readline()
packet_raw = str(bin(int(packet_raw, 16)))[2:]
print(packet_raw)


def read_bits(packet, start, length):
    return int(packet[start : start + length], 2)


def parse_literal_value(packet, start):
    next_group_start = start
    bit_string = ""
    while True:
        bit_string += packet[next_group_start + 1 : next_group_start + 5]
        if packet[next_group_start] == "0":
            break
        next_group_start += 5
    return (next_group_start - start + 5, int(bit_string, 2))


def parse_raw_packet_internal(packet_raw, start):
    packet = Packet()
    packet.version = read_bits(packet_raw, start, 3)
    packet.type = read_bits(packet_raw, start + 3, 3)
    bit_length = 6

    if packet.type == 4:
        literal_bit_count, packet.value = parse_literal_value(packet_raw, start + 6)
        bit_length += literal_bit_count
    else:
        packet.length_type = read_bits(packet_raw, start + 6, 1)
        bit_length += 1
        if packet.length_type == 0:
            packet.subpackets_bitlength = read_bits(packet_raw, start + 7, 15)
            bit_length += 15
            remaining_subpackets_bitlength = packet.subpackets_bitlength
            while remaining_subpackets_bitlength > 0:
                (subpacket_bitlength, subpacket) = parse_raw_packet_internal(
                    packet_raw, start + bit_length
                )
                bit_length += subpacket_bitlength
                packet.subpackets.append(subpacket)
                remaining_subpackets_bitlength -= subpacket_bitlength
        else:
            packet.subpackets_count = read_bits(packet_raw, start + 7, 11)
            bit_length += 11
            remaining_subpackets = packet.subpackets_count
            while remaining_subpackets > 0:
                (subpacket_bitlength, subpacket) = parse_raw_packet_internal(
                    packet_raw, start + bit_length
                )
                bit_length += subpacket_bitlength
                packet.subpackets.append(subpacket)
                remaining_subpackets -= 1
    return (bit_length, packet)


def parse_raw_packet(packet_raw):
    _, packet = parse_raw_packet_internal(packet_raw, 0)
    return packet


def sum_all_packets_versions(packet):
    result = packet.version
    for subpacket in packet.subpackets:
        result += sum_all_packets_versions(subpacket)
    return result


def solve_1(packet_raw):
    packet_raw_bit = str(bin(int(packet_raw, 16)))[2:]
    packet = parse_raw_packet(packet_raw_bit)
    return sum_all_packets_versions(packet)


assert solve_1("D2FE28") == 6
assert solve_1("8A004A801A8002F478") == 16
