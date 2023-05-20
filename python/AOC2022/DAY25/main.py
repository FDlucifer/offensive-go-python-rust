#!/usr/bin/env python3

import sys


VALS = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
BACKVALS = {3: "=", 4: "-", 5: 0, 6: 1, 7: 2}


def from_SNAFU(s):

    return sum(pow(5, i) * VALS[c] for i, c in enumerate(s[::-1]))


def to_SNAFU(num):

    # convert to base5
    s = []
    while num:
        s.append(num % 5)
        num //= 5

    # convert to SNAFU
    for i in range(len(s)):
        if s[i] >= 3:
            s[i] = BACKVALS[s[i]]
            s[i + 1] += 1

    return "".join(map(str, s[::-1]))


with open(sys.argv[1], "r") as f:
    lines = list(map(str.strip, f.readlines()))

total = to_SNAFU(sum(from_SNAFU(line) for line in lines))
print(f"Answer: {total}")
