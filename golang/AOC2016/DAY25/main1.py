import re

HEIGHT = 6
WIDTH = 50

PARSER = re.compile("(inc|dec|cpy|jnz|tgl|out) (-?\d+|[a-d]) ?(-?\d+|[a-d])?$")


def parse_input(input_seq):
    for cmd in input_seq:
        op, a, b = PARSER.match(cmd).groups()
        if not a.isalpha():
            a = int(a)
        if b is not None:
            if not b.isalpha():
                b = int(b)
            yield(op, (a, b))
        else:
            yield(op, (a,))


def tgl(code, registers, value):
    value = registers["ip"] + registers.get(value, value)
    if value < len(code) and value != registers["ip"]:
        instr = code[value]
        if instr[0] == "inc":
            instr = tuple(["dec"] + list(instr[1:]))
        elif instr[0] in ("dec", "tgl"):
            instr = tuple(["inc"] + list(instr[1:]))
        elif instr[0] == "jnz":
            if instr[1][1] in ("a", "b", "c", "d"):
                instr = tuple(["cpy"] + list(instr[1:]))
        elif instr[0] == "cpy":
            instr = tuple(["jnz"] + list(instr[1:]))
        code[value] = instr
    registers["ip"] += 1


def inc(code, registers, reg):
    registers[reg] += 1
    registers["ip"] += 1


def dec(code, registers, reg):
    registers[reg] -= 1
    registers["ip"] += 1


def cpy(code, registers, value, reg):
    registers[reg] = registers.get(value, value)
    registers["ip"] += 1


def jnz(code, registers, value, offset):
    if registers.get(value, value) != 0:
        registers["ip"] += registers.get(offset, offset)
    else:
        registers["ip"] += 1


class BunnyException(Exception):
    pass


def out(code, registers, value):
    val = registers.get(value, value)
    if val not in (1, 0) or val == registers["out"][-1]:
        raise BunnyException
    registers["out"] += [val]
    registers["ip"] += 1


OP = {
    "jnz": jnz,
    "inc": inc,
    "dec": dec,
    "cpy": cpy,
    "tgl": tgl,
    "out": out
}


def execute(code, stop, **kwargs):
    registers = {"a": 0, "b": 0, "c": 0, "d": 0, "ip": 0, "out": [0]}
    registers.update(kwargs)
    c = 0
    while registers["ip"] < len(code) and c < stop:
        c += 1
        cmd, args = code[registers["ip"]]
        OP[cmd](code, registers, *args)

    return registers


def main():
    with open("input.txt") as inp:
        inp_seq = list(inp)
        parsed_input = list(parse_input(inp_seq))
        for i in range(1000000):
            try:
                print(i)
                registers = execute(parsed_input, 1000000, a=i, out=[1])
                print(i)
                print(registers["out"])
                return
            except BunnyException:
                pass


if __name__ == '__main__':
    main()
