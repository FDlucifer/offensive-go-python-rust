with open('input.txt') as fd:
    code = fd.read().splitlines()

class BunnyInterpreter:

    def __init__(self, instructions, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.instructions = instructions
        self.pointer = 0

    def grab(self, x):
        if x in 'abcd':
            return getattr(self, x)
        return int(x)

    def cpy(self, source, dest):
        setattr(self, dest, self.grab(source))

    def inc(self, register):
        temp = getattr(self, register)
        setattr(self, register, temp+1)

    def dec(self, register):
        temp = getattr(self, register)
        setattr(self, register, temp-1)

    def jnz(self, c, dist):
        if self.grab(c) != 0:
            self.pointer += int(dist)
        else:
            self.pointer += 1

    def parse(self, ins):
        op, *args = ins.split()
        getattr(self, op)(*args)
        if op != 'jnz':
            self.pointer += 1

    def run(self):
        while self.pointer < len(self.instructions):
            self.parse(self.instructions[self.pointer])

b = BunnyInterpreter(code)
c = BunnyInterpreter(code, c=1)
b.run()
c.run()
print('star one: {}'.format(b.a))
print('star two: {}'.format(c.a))
