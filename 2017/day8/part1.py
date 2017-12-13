from collections import defaultdict

def parse_line(line):
    import re
    groups = re.match(r'(\w+) (inc|dec) (-?\d+) if (\w+) ([\!\<\>\=]+) (-?\d+)', line).groups()
    return [
        groups[0],
        groups[1],
        int(groups[2]),
        groups[3],
        groups[4],
        int(groups[5])
    ]


def accept_cond(val, cond, param):
    ops = {
        '>': lambda left, right: left > right,
        '<': lambda left, right: left < right,
        '>=': lambda left, right: left >= right,
        '<=': lambda left, right: left <= right,
        '==': lambda left, right: left == right,
        '!=': lambda left, right: left != right
    }

    return ops[cond](val, param)


def mod_register(val, op, param):
    ops = {
        'inc': lambda left, right: left + right,
        'dec': lambda left, right: left - right
    }

    return ops[op](val, param)


registers = defaultdict(int)
for line in open('input.txt'):
    [register, instr, instr_param, cond_register, cond, cond_param] = parse_line(line)
    if accept_cond(registers[cond_register], cond, cond_param):
        registers[register] = mod_register(registers[register], instr, instr_param)

print max(registers.values())
