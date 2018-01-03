class DanceGroup:
    def __init__(self, dancers):
        self.dancers = list(dancers)

    def spin(self, num):
        self.dancers = self.dancers[-num:] + self.dancers[:-num]

    def exchange(self, a, b):
        self.dancers[a], self.dancers[b] = self.dancers[b], self.dancers[a]

    def partner(self, a, b):
        self.exchange(self.dancers.index(a), self.dancers.index(b))


def do_dance(dg, instrs):
    for instr in instrs:
        if instr[0] is 's':
            dg.spin(int(instr[1:]))
        if instr[0] is 'x':
            a, b = [int(num) for num in instr[1:].split('/')]
            dg.exchange(a, b)
        if instr[0] is 'p':
            a, b = [actor for actor in instr[1:].split('/')]
            dg.partner(a, b)
