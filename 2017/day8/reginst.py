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
    from operator import gt, lt, ge, le, ne, eq

    ops = {'>': gt, '<': lt, '>=': ge, '<=': le, '==': eq, '!=': ne}

    return ops[cond](val, param)


def mod_register(val, op, param):
    from operator import add, sub

    ops = {'inc': add, 'dec': sub}

    return ops[op](val, param)
