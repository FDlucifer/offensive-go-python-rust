import math


def hex_to_bin(s):
    return format(int(s.strip(), 16), f"0{len(s.strip()) * 4}b")


def parse_header(s):
    return int(s[:3], 2), int(s[3:6], 2)


def parse_literal(packet):
    bit_index = 6
    parsed_literal = ""

    while True:
        parsed_literal += packet[bit_index + 1 : bit_index + 5]

        if packet[bit_index] == "0":
            break

        bit_index += 5

    return int(parsed_literal, 2), bit_index + 5


def parse_operator(packet):
    if packet[6] == "0":
        L = int(packet[7 : 22], 2)
        bit_index = 22
        numbers = []

        while bit_index < L + 22:
            result, length = parse_packet(packet[bit_index : ])
            bit_index += length
            numbers.append(result)

    else:
        num_sub_packets = int(packet[7 : 18], 2)
        bit_index = 18
        numbers = []

        for _ in range(num_sub_packets):
            result, length = parse_packet(packet[bit_index : ])
            bit_index += length
            numbers.append(result)

    return numbers, bit_index


def parse_packet(packet):
    packet_version, type_id = parse_header(packet)

    if type_id == 4:
        return parse_literal(packet)

    else:
        numbers, bit_index = parse_operator(packet)


    if type_id in OPERATORS:
        result = OPERATORS[type_id](numbers)

    return result, bit_index


OPERATORS = {
        0: sum,
        1: math.prod,
        2: min,
        3: max,
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1])
    }

data = open("input.txt").read()

data_bin = hex_to_bin(data)

print("evaluated expression:", parse_packet(data_bin)[0])
