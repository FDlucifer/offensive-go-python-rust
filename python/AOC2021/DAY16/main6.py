import sys
import operator
from functools import reduce

digit_to_binary = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
    }

def load(filename):
    with open(filename) as f:
        return ''.join([digit_to_binary[d] for d in f.read().strip()])

bits = load(sys.argv[1])
#bits = '110100101111111000101000'
#bits = '00111000000000000110111101000101001010010001001000000000'
#bits = '11101110000000001101010000001100100000100011000001100000'
print(bits)

class Parser(object):
    def __init__(self, bits):
        self.bits = bits
        self.i = 0
        self.sum_versions = 0

    def read(self, n):
        v = 0
        for i in range(n):
            v <<= 1
            if self.i < len(self.bits):
                if self.bits[self.i] == '1':
                    v |= 1
                self.i += 1
        return v

    def parse(self):
        pkt_version = self.read(3)
        pkt_type = self.read(3)
        self.sum_versions += pkt_version
        if pkt_type == 4:
            return self.parse_literal()
        else:
            if pkt_type == 0:
                op = sum
            elif pkt_type == 1:
                op = lambda v: reduce(operator.mul, v, 1)
            elif pkt_type == 2:
                op = min
            elif pkt_type == 3:
                op = max
            elif pkt_type == 5:
                op = lambda v: 1 if v[0] > v[1] else 0
            elif pkt_type == 6:
                op = lambda v: 1 if v[0] < v[1] else 0
            elif pkt_type == 7:
                op = lambda v: 1 if v[0] == v[1] else 0
            return self.parse_operator(op)

    def parse_literal(self):
        v = 0
        while True:
            b = self.read(1)
            d = self.read(4)
            v = (v << 4) | d
            if b == 0:
                return v

    def parse_operator(self, op):
        if self.read(1) == 0:
            return self.parse_subpackets(op, total_length=p.read(15))
        else:
            return self.parse_subpackets(op, num_packets=p.read(11))

    def parse_subpackets(self, op, total_length=None, num_packets=None):
        if total_length is not None:
            j = self.i + total_length
            v = []
            while self.i < j:
                v.append(self.parse())
        elif num_packets is not None:
            v = [self.parse() for _ in range(num_packets)]
        return op(v)

p = Parser(bits)
v = p.parse()

print(f'Answer [part 1]: {p.sum_versions}')
print(f'Answer [part 2]: {v}')
