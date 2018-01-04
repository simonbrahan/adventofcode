from collections import defaultdict
import re

def str_is_num(string):
    return re.search('^-?\d+$', string) is not None


def parse_instr(instr):
    instr_parts = instr.strip().split(' ')

    if str_is_num(instr_parts[1]):
        instr_parts[1] = int(instr_parts[1])

    if len(instr_parts) < 3:
        instr_parts.append(None)
    elif str_is_num(instr_parts[2]):
        instr_parts[2] = int(instr_parts[2])

    return instr_parts


def resolve(param, registers):
    if type(param) is int:
        return param
    else:
        return registers[param]


with open('input.txt') as input_file:
    instrs = [parse_instr(line) for line in input_file]

registers = defaultdict(int)
last_played_sound = None
pos = 0

while pos < len(instrs) and pos > -1:
    instr, x, y = instrs[pos]

    if instr == 'snd':
        last_played_sound = resolve(x, registers)
    if instr == 'set':
        registers[x] = resolve(y, registers)
    if instr == 'add':
        registers[x] += resolve(y, registers)
    if instr == 'mul':
        registers[x] *= resolve(y, registers)
    if instr == 'mod':
        registers[x] %= resolve(y, registers)
    if instr == 'rcv' and resolve(x, registers) is not 0:
        print last_played_sound
        break
    if instr == 'jgz' and resolve(x, registers) > 0:
        pos += resolve(y, registers)
        continue

    pos += 1
