from collections import defaultdict
from reginst import parse_line, accept_cond, mod_register

registers = defaultdict(int)
for line in open('input.txt'):
    [register, instr, instr_param, cond_register, cond, cond_param] = parse_line(line)
    if accept_cond(registers[cond_register], cond, cond_param):
        registers[register] = mod_register(registers[register], instr, instr_param)

print max(registers.values())
