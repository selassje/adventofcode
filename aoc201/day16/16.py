class Packet:
    def evaluate(self):
        if self.type == 0:
            sum = 0
            for s in self.subpackets:
                sum += s.evaluate()
            return sum
        if self.type == 1:
            product = 1
            for s in self.subpackets:
                product *= s.evaluate()
            return product
        if self.type == 2:
            result = self.subpackets[0].evaluate()
            for s in self.subpackets:
                result = min(result, s.evaluate())
            return result
        if self.type == 3:
            result = self.subpackets[0].evaluate()
            for s in self.subpackets:
                result = max(result, s.evaluate())
            return result
        if self.type == 4:
            return self.value
        if self.type == 5:
            if self.subpackets[0].evaluate() > self.subpackets[1].evaluate():
                return 1
            else:
                return 0
        if self.type == 6:
            if self.subpackets[0].evaluate() < self.subpackets[1].evaluate():
                return 1
            else:
                return 0
        if self.type == 7:
            if self.subpackets[0].evaluate() == self.subpackets[1].evaluate():
                return 1
            else:
                return 0


input_raw = open("input.txt").readline()


def hex_to_bit_string(hex):
    bit_string = ""
    for h in hex:
        h_i = int(h, 16)
        bit_string += "{0:04b}".format(h_i)
    return bit_string


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
    packet.subpackets = []
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
                assert remaining_subpackets_bitlength >= 0
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


def solve_1(packet_raw_hex):
    packet_raw_bit = hex_to_bit_string(packet_raw_hex)
    packet = parse_raw_packet(packet_raw_bit)
    return sum_all_packets_versions(packet)


def solve_2(packet_raw_hex):
    packet_raw_bit = hex_to_bit_string(packet_raw_hex)
    packet = parse_raw_packet(packet_raw_bit)
    return packet.evaluate()


assert solve_1("D2FE28") == 6
assert solve_1("8A004A801A8002F478") == 16
assert solve_1("620080001611562C8802118E34") == 12
assert solve_1("C0015000016115A2E0802F182340") == 23
assert solve_1("A0016C880162017C3686B18A3D4780") == 31

assert solve_2("C200B40A82") == 3
assert solve_2("04005AC33890") == 54
assert solve_2("880086C3E88112") == 7
assert solve_2("CE00C43D881120") == 9
assert solve_2("D8005AC2A8F0") == 1
assert solve_2("F600BC2D8F") == 0
assert solve_2("9C005AC2F8F0") == 0
assert solve_2("9C0141080250320F1802104A08") == 1

print(solve_1(input_raw), solve_2(input_raw))
