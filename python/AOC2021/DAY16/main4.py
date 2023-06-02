import functools
import operator
from typing import List, Union


def get_filename(test=False):
    return 'input.txt'


def get_input(parse, test=False):
    data = []
    filename = get_filename(test)
    with open(filename, "r") as file:
        for line in file:
            data.append(parse(line.strip()))
    return data


################################################################################
############################### Start of Part 1 ################################
################################################################################


def parse1(line: str):
    return line


################################################################################
########################## Helper Functions of Part 1 ##########################
################################################################################


class Packet:
    def __init__(self, version, typeId) -> None:
        self.version = version
        self.typeId = typeId
        self.lenTypeId = None
        self.value = None
        self.subPackets = []
        self.bitLen = None

    def __str__(self) -> str:
        if self.value:
            content = f"<value:{self.value}>"
        else:
            content = f"<{len(self.subPackets)} SubPackets>"
        return (
            "<Packet"
            f" version:{self.version} typeId:{self.typeId} lenTypeId:{self.lenTypeId} contents:{content} bitLen:{self.bitLen}>"
        )


HEX_TO_BIT = {
    "0": [0, 0, 0, 0],
    "1": [0, 0, 0, 1],
    "2": [0, 0, 1, 0],
    "3": [0, 0, 1, 1],
    "4": [0, 1, 0, 0],
    "5": [0, 1, 0, 1],
    "6": [0, 1, 1, 0],
    "7": [0, 1, 1, 1],
    "8": [1, 0, 0, 0],
    "9": [1, 0, 0, 1],
    "A": [1, 0, 1, 0],
    "B": [1, 0, 1, 1],
    "C": [1, 1, 0, 0],
    "D": [1, 1, 0, 1],
    "E": [1, 1, 1, 0],
    "F": [1, 1, 1, 1],
}


def hex_to_bit_arr(hexstr: str):
    bitarr = []
    for hex_ in hexstr:
        bitarr.extend(HEX_TO_BIT[hex_])
    return bitarr


def bit_arr_to_dec(bitArr: List[bool]) -> int:
    """Convert bit array to decimal representation

    Args:
        bitArr (List[bool]): bit array

    Returns:
        int: int representation of bit array
    """
    value: int = 0
    for bit in bitArr:
        value = value << 1
        value += bit
    return value


def parse_packet(packet: List[bool]) -> Packet:
    # Uncomment to see process

    version = bit_arr_to_dec(packet[0:3])
    typeId = bit_arr_to_dec(packet[3:6])

    packetObj: Packet = Packet(version, typeId)

    # print('V:', version, '| T:', typeId)

    if typeId == 4:
        # Data packet
        values = []
        curr = 6
        while packet[curr] != 0:
            values.extend(packet[curr + 1 : curr + 5])
            curr += 5
        values.extend(packet[curr + 1 : curr + 5])
        packetObj.value = values
        packetObj.bitLen = curr + 5
        return packetObj

    HEADER_OFFSET = 7

    packetObj.lenTypeId = packet[6]

    curr = None

    # print('I:', len_type_id)

    if packetObj.lenTypeId == 0:
        bitsToLook = 15
        lenInBits = bit_arr_to_dec(packet[HEADER_OFFSET : HEADER_OFFSET + bitsToLook])
        curr = HEADER_OFFSET + bitsToLook
        while curr < lenInBits + (HEADER_OFFSET + bitsToLook):
            subPacket: Packet = parse_packet(packet[curr : curr + lenInBits])
            packetObj.subPackets.append(subPacket)
            curr += subPacket.bitLen
    else:
        bitsToLook = 11
        totalSubPackets = bit_arr_to_dec(
            packet[HEADER_OFFSET : HEADER_OFFSET + bitsToLook]
        )
        curr = HEADER_OFFSET + bitsToLook
        while totalSubPackets > 0:
            subPacket: Packet = parse_packet(packet[curr:])
            packetObj.subPackets.append(subPacket)
            curr += subPacket.bitLen
            totalSubPackets -= 1

    # print('LastBit:', curr)

    packetObj.bitLen = curr

    return packetObj


def sum_packet_versions(packet: Packet) -> int:
    if packet.typeId == 4:
        return packet.version

    total = packet.version

    for sp in packet.subPackets:
        total += sum_packet_versions(sp)

    return total


################################################################################


def day16p1():
    packets = get_input(parse1, test=False)

    result = []
    for packet in packets:
        # hex_to_bit_arr(packet, 'Len Original:', len(packet)
        packet = hex_to_bit_arr(packet)
        syntax_tree = parse_packet(packet)
        print("ST:", syntax_tree)
        packetVersionSum = sum_packet_versions(syntax_tree)
        result.append(packetVersionSum)

    return list(map(lambda x: f"Sum: {x}", result))


################################################################################
############################### Start of Part 2 ################################
################################################################################


def parse2(line):
    return parse1(line)


################################################################################
########################## Helper Functions of Part 2 ##########################
################################################################################


OPERATIONS = {
    0: sum,
    1: lambda sps: functools.reduce(operator.mul, sps, 1),
    2: min,
    3: max,
    5: lambda sps: sps[0] > sps[1],
    6: lambda sps: sps[0] < sps[1],
    7: lambda sps: sps[0] == sps[1],
}


def execute_packets(packet: Packet) -> Union[int, bool]:
    typeId = packet.typeId

    if typeId == 4:
        return bit_arr_to_dec(packet.value)

    return OPERATIONS[typeId]([execute_packets(sp) for sp in packet.subPackets])


################################################################################


def day16p2():
    packets = get_input(parse2, test=False)
    results = []
    for packet in packets:
        packet = hex_to_bit_arr(packet)
        st = parse_packet(packet)
        result = execute_packets(st)
        results.append(result)
    return "Results:", results


def main():
    divs = 40
    msg = 15
    n = (divs - msg) // 2
    divs += 1
    print()
    print("-" * (n), "Day 16 - Part 1", "-" * n)
    print("Result =>", day16p1())
    print()
    print("-" * (n), "Day 16 - Part 2", "-" * n)
    print("Result =>", day16p2())
    print()


main()
