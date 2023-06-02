#!/usr/bin/env python3
import math
from functools import reduce

class Bitstream:
    def __init__(self, hexstream):
        self.bitstream = []
        for c in hexstream:
            self.bitstream.extend(bin(int(c, 16))[2:].zfill(4))
        # number of bits read overall
        self.read = 0
        # sum of all versions
        self.versionsum = 0

    def get_bits(self, n):
        self.read += n
        bits = self.bitstream[:n]
        self.bitstream = self.bitstream[n:]
        return bits

    def decode_bits(self, x):
        return int("".join([str(b) for b in x]), 2)

    def get_literal(self):
        number = []
        while True:
            last = self.decode_bits(self.get_bits(1)) == 0
            number.extend(self.get_bits(4))
            if last:
                break
        return self.decode_bits(number)

    def decode_packet(self):
        version = self.decode_bits(self.get_bits(3))
        id = self.decode_bits(self.get_bits(3))
        self.versionsum += version

        if id == 4: # literal packet
            value = self.get_literal()
        else: # operator packet
            lengthtype = self.decode_bits(self.get_bits(1))
            v = [] # collect all literals
            if lengthtype == 0: # bit length
                length = self.decode_bits(self.get_bits(15))
                pos = self.read
                while pos + length > self.read:
                    v.append(self.decode_packet())
            elif lengthtype == 1: # number of subpackets
                subpackets = self.decode_bits(self.get_bits(11))
                for _ in range(subpackets):
                    v.append(self.decode_packet())
            else:
                raise ValueError(f"Unknown lengthtype: {lengthtype}")

            if id == 0: # +
                value = sum(v)
            elif id == 1: # *
                value = reduce(lambda x,y: x*y, v)
            elif id == 2: # min
                value = min(v)
            elif id == 3: # max
                value = max(v)
            elif id == 5: # >
                value = int(v[0] > v[1])
            elif id == 6: # <
                value = int(v[0] < v[1])
            elif id == 7: # ==
                value = int(v[0] == v[1])
            else:
                raise ValueError(f"Unknown operator: {id}")
        return value

if __name__ == "__main__":
    with open("input.txt") as fh:
        for line in fh:
            message = line.strip()

    bs = Bitstream(message)
    result = bs.decode_packet()
    print(f"Part 1: sum of all version numbers: {bs.versionsum}")
    print(f"Part 2: evaluated expresion: {result}")
