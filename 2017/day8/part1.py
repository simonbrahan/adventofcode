def parseLine(line):
    import re
    return re.match(r'(\w+) (inc|dec) (-?\d+) if (\w+) ([\!\<\>\=]+) (-?\d+)', line).groups()


for line in open('input.txt'):
    print parseLine(line)
    [register, instr, instr_param, cond_register, cond, cond_param] = parseLine(line)
