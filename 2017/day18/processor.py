from collections import defaultdict
import re

class Processor:
    def __init__(self, instrs, procid):
        self.procid = procid
        self.instrs = instrs
        self.registers = defaultdict(int)
        self.registers['p'] = procid
        self.rcv_queue = []
        self.instr_pos = 0
        self.sent_val_count = 0
        self.finished = False
        self.mul_count = 0

    def register_partner(self, other_processor):
        self.partner = other_processor

    def rcv(self, val):
        self.rcv_queue.append(val)

    def stopped(self):
        return self.finished or len(self.rcv_queue) is 0

    def broadcast_sent_val_count(self):
        print 'proc ' + str(self.procid) + ' sent ' + str(self.sent_val_count) + ' values\n'

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
                self.sent_val_count += 1
            if instr == 'set':
                self.registers[x] = resolve(y)
            if instr == 'add':
                self.registers[x] += resolve(y)
            if instr == 'sub':
                self.registers[x] -= resolve(y)
            if instr == 'mul':
                self.mul_count += 1
                self.registers[x] *= resolve(y)
            if instr == 'mod':
                self.registers[x] %= resolve(y)
            if instr == 'rcv':
                """
                    This is a nasty conditional
                    Ordinarily it would be formatted:

                    if self.rcv_queue:
                    elif self.partner.stopped():
                    else:

                    but this produces a race condition
                    as it's possible for the partner to "look" stopped
                    before its last value has arrived
                """
                if self.partner.stopped() and not self.rcv_queue:
                    self.broadcast_sent_val_count()
                    break
                elif self.rcv_queue:
                    self.registers[x] = self.rcv_queue.pop(0)
                else:
                    continue

            if instr == 'jgz' and resolve(x) > 0:
                self.instr_pos += resolve(y)
                continue
            if instr == 'jnz' and resolve(x) is not 0:
                self.instr_pos += resolve(y)
                continue

            self.instr_pos += 1

        self.finished = True


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

    return instr_parts[:3]
