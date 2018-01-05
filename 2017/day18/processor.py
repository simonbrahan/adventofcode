from collections import defaultdict
import re

class Processor:
    def __init__(self, instrs):
        self.instrs = instrs
        self.registers = defaultdict(int)
        self.rcv_queue = []
        self.instr_pos = 0
        self.waiting = False

    def register_partner(self, other_processor):
        self.partner = other_processor

    def rcv(self, val):
        self.rcv_queue.append(val)

    def run(self):
        def resolve(param):
            if type(param) is int:
                return param
            else:
                return self.registers[param]

        while -1 < self.instr_pos < len(self.instrs):
            instr, x, y = self.instrs[self.instr_pos]

            if instr == 'snd':
                self.partner.rcv(resolve(x))
            if instr == 'set':
                self.registers[x] = resolve(y)
            if instr == 'add':
                self.registers[x] += resolve(y)
            if instr == 'mul':
                self.registers[x] *= resolve(y)
            if instr == 'mod':
                self.registers[x] %= resolve(y)
            if instr == 'rcv':
                if not self.rcv_queue:
                    self.waiting = True
                    break
                else:
                    self.registers[x] = self.rcv_queue.pop(0)
            if instr == 'jgz' and resolve(x) > 0:
                self.instr_pos += resolve(y)
                continue

            self.instr_pos += 1

        print self.registers.items()



def parse_instr(instr):
    def str_is_num(string):
        return re.search('^-?\d+$', string) is not None

    instr_parts = instr.strip().split(' ')

    if str_is_num(instr_parts[1]):
        instr_parts[1] = int(instr_parts[1])

    if len(instr_parts) < 3:
        instr_parts.append(None)
    elif str_is_num(instr_parts[2]):
        instr_parts[2] = int(instr_parts[2])

    return instr_parts
