import heapq
import sys
import itertools
import more_itertools
from collections import defaultdict, Counter, deque
import re
from queue import PriorityQueue

import numpy as np
from more_itertools import sliding_window
from networkx import Graph

import binascii

hex2bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

bin2hex = {v: k for k, v in hex2bin.items()}


def parse_hex(s):
    """
    >>> parse_hex('D2FE28')
    '110100101111111000101000'
    """
    x = "".join([hex2bin[c] for c in s])
    return x


def bits2char(bits):
    """
    >>> bits2char('110')
    '6'
    >>> bits2char('100')
    '4'
    """
    x = bits
    while len(x) < 4:
        x = "0" + x
    return bin2hex[x]


def binary2literal(binary_string):
    """
    >>> binary2literal('011111100101')
    2021
    """
    ret_val = 0
    x = 1
    for c in binary_string[::-1]:
        if c == "1":
            ret_val += x
        x *= 2
    return ret_val


class Buffer:
    """
    >>> b = Buffer('D2FE28')
    >>> b.buffer
    '110100101111111000101000'
    >>> b.pos
    0
    >>> v = b.read_int(3)
    >>> v
    6
    >>> t = b.read_int(3)
    >>> t
    4
    """

    def __init__(self, hex_string):
        self.buffer = parse_hex(hex_string)
        self.pos = 0

    def read_int(self, bits):
        return int(bits2char(self.read_next(bits)))

    def read_next(self, bits):
        s = self.buffer[self.pos : self.pos + bits]
        self.pos += bits
        return s

    def set_pos(self, pos):
        self.pos = pos

    def peek_next(self, bits):
        return self.buffer[self.pos : self.pos + bits]

    def read_literal_int(self, chunk_size):
        """
        >>> b = Buffer('D2FE28')
        >>> b.set_pos(6)
        >>> x = b.read_literal_int(5)
        >>> x
        2021
        >>> b.pos
        21
        >>> b.peek_next(10)
        '000'
        """

        s = ""
        while True:
            c = self.read_next(chunk_size)
            s += c[1:chunk_size]
            if c[0] == "0":
                break

        return int(binary2literal(s))

    def next_packet(self):
        """
        >>> b = Buffer('D2FE28')
        >>> p = b.next_packet()
        >>> p
        {'version': 6, 'typeid': 4, 'value': 2021}
        >>> b = Buffer('38006F45291200')
        >>> p = b.next_packet()
        >>> p
        {'version': 1, 'typeid': 6, 'packets': [{'version': 6, 'typeid': 4, 'value': 10}, {'version': 2, 'typeid': 4, 'value': 20}]}
        >>> b = Buffer('EE00D40C823060')
        >>> p = b.next_packet()
        >>> p
        {'version': 7, 'typeid': 3, 'packets': [{'version': 2, 'typeid': 4, 'value': 1}, {'version': 4, 'typeid': 4, 'value': 2}, {'version': 1, 'typeid': 4, 'value': 3}]}
        >>> b = Buffer('8A004A801A8002F478')
        >>> p = b.next_packet()
        >>> p
        {'version': 4, 'typeid': 2, 'packets': [{'version': 1, 'typeid': 2, 'packets': [{'version': 5, 'typeid': 2, 'packets': [{'version': 6, 'typeid': 4, 'value': 15}]}]}]}
        """
        # read the version
        version = self.read_int(3)
        type_id = self.read_int(3)

        if type_id == 4:
            literal = self.read_literal_int(5)
            # print(f"literal: {literal}")
            return {"version": version, "typeid": type_id, "value": literal}
        else:
            length_type_id = self.read_int(1)
            if length_type_id == 0:
                total_length = binary2literal(self.read_next(15))
                stop_pos = self.pos + total_length
                subpackets = []
                while self.pos < stop_pos:
                    p = self.next_packet()
                    subpackets.append(p)

                return {"version": version, "typeid": type_id, "packets": subpackets}
            else:
                num_sub_packets = binary2literal(self.read_next(11))
                subpackets = []
                for i in range(0, num_sub_packets):
                    subpackets.append(self.next_packet())
                return {"version": version, "typeid": type_id, "packets": subpackets}


def version_sum(packet):
    if "value" in packet:
        return packet["version"]
    else:
        x = packet["version"]
        for sp in packet["packets"]:
            x += version_sum(sp)
        return x


def evaluate_packet(packet):
    """
    >>> evaluate_packet(Buffer('C200B40A82').next_packet())
    3
    >>> evaluate_packet(Buffer('04005AC33890').next_packet())
    54
    >>> evaluate_packet(Buffer('880086C3E88112').next_packet())
    7
    >>> evaluate_packet(Buffer('CE00C43D881120').next_packet())
    9
    >>> evaluate_packet(Buffer('D8005AC2A8F0').next_packet())
    1
    >>> evaluate_packet(Buffer('F600BC2D8F').next_packet())
    0
    >>> evaluate_packet(Buffer('9C005AC2F8F0').next_packet())
    0
    >>> evaluate_packet(Buffer('9C0141080250320F1802104A08').next_packet())
    1
    """
    ret_val = None
    if packet["typeid"] == 0:
        # sum packet
        values = [evaluate_packet(p) for p in packet["packets"]]
        ret_val = sum(values)
    elif packet["typeid"] == 1:
        # product  packet, note that you need to use np.ulonglong to prevent
        # integer overflow
        ret_val = np.prod(
            [evaluate_packet(p) for p in packet["packets"]], dtype=np.ulonglong
        )
    elif packet["typeid"] == 2:
        ret_val = np.min([evaluate_packet(p) for p in packet["packets"]])
    elif packet["typeid"] == 3:
        ret_val = np.max([evaluate_packet(p) for p in packet["packets"]])
    elif packet["typeid"] == 4:
        ret_val = packet["value"]
    elif packet["typeid"] == 5:
        ret_val = evaluate_packet(packet["packets"][0]) > evaluate_packet(
            packet["packets"][1]
        )
    elif packet["typeid"] == 6:
        ret_val = evaluate_packet(packet["packets"][0]) < evaluate_packet(
            packet["packets"][1]
        )
    elif packet["typeid"] == 7:
        ret_val = evaluate_packet(packet["packets"][0]) == evaluate_packet(
            packet["packets"][1]
        )

    if ret_val < 0:
        raise "possible multiplication overflow"

    return ret_val


def part_1(hex_str):
    """
    >>> part_1('8A004A801A8002F478')
    16
    >>> part_1('620080001611562C8802118E34')
    12
    >>> part_1('C0015000016115A2E0802F182340')
    23
    >>> part_1('A0016C880162017C3686B18A3D4780')
    31
    """
    b = Buffer(hex_str)
    p = b.next_packet()
    x = version_sum(p)
    return x


def process_file(filename):
    with open(filename) as f:
        txt = f.readlines()

    sum = part_1(txt[0])
    print(f"version sum of {filename} = {sum}")
    value = evaluate_packet(Buffer(txt[0]).next_packet())
    print(f"value of {filename} = {value}")


process_file("input.txt")
