def hex_to_bin(s):
    return bin(int(s, 16))[2:]


# leading 0's until the length is a multiple of 4
def leading_zeros(a):
    return "0" * ((4 - len(a) % 4) % 4) + a


def parse_header(s, to_decimal=False):
    return (int(s[0:3], 2), int(s[3:6], 2)) if to_decimal else (s[0:3], s[3:6])


def parse_literal(packet, to_decimal=False):
    num_bits = 5
    num_bin = packet[6:]
    binary_numbers = [num_bin[i:i+num_bits] for i in range(0, len(num_bin), num_bits)
                      if len(num_bin[i:i+num_bits]) == 5]

    # binary_numbers = [num for num in binary_numbers if num != "00000"]

    parsed_literal = ""
    parse_counter = 0

    for binary_number in binary_numbers:
        parsed_literal += binary_number[1:]
        parse_counter += 1

        # check if binary_number starts with a 0 and marks the last chunk
        if binary_number[0] == "0":
            # if there are more 5 bit chunks, consider them a new packet
            if len(binary_numbers) != parse_counter:
                parse_packet(num_bin[parse_counter * num_bits:])
            break

    if to_decimal:
        return int(parsed_literal, 2)

    return parsed_literal


def parse_operator(packet):
    length_type_id = packet[6]
    length_of_bits = 0

    if length_type_id == "0":
        length_of_bits = 15
    elif length_type_id == "1":
        length_of_bits = 11

    L_bin = packet[7:7+length_of_bits]
    L = int(L_bin, 2)

    if length_type_id == "0":
        sub_packets_1 = packet[7+length_of_bits:7+length_of_bits+L]
        sub_packets_2 = packet[7+length_of_bits+L:]
        parse_packet(sub_packets_1)
        parse_packet(sub_packets_2)

    elif length_type_id == "1":
        sub_packets = packet[7+length_of_bits:]
        parse_packet(sub_packets)


def parse_packet(packet):
    if packet.count("0") == len(packet):
        return

    packet_version, type_id = parse_header(packet, True)

    global version_counter
    version_counter += packet_version

    if type_id == 4:
        parse_literal(packet, True)
    else:
        parse_operator(packet)


data = open("input.txt").read()

data_bin = hex_to_bin(data)
data_bin = leading_zeros(data_bin)
version_counter = 0

parse_packet(data_bin)
print(version_counter)
