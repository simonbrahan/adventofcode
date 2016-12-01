import re

def get_cmd(line):
    pattern = re.compile('(.+?) \-\> (\w+)')
    res = re.search(pattern, line)
    cmd = res.group(1)

    return { 'cmd': cmd, 'wire': res.group(2) }


def parse_wire(wire, cmds):
    res = re.search('(\w+) AND (\w+)', cmds[wire])
    if res:
        return get_value(res.group(1), cmds) & get_value(res.group(2), cmds)

    res = re.search('(\w+) OR (\w+)', cmds[wire])
    if res:
        return get_value(res.group(1), cmds) | get_value(res.group(2), cmds)

    res = re.search('(\w+) LSHIFT (\w+)', cmds[wire])
    if res:
        return get_value(res.group(1), cmds) << get_value(res.group(2), cmds)

    res = re.search('(\w+) RSHIFT (\w+)', cmds[wire])
    if res:
        return get_value(res.group(1), cmds) >> get_value(res.group(2), cmds)

    res = re.search('NOT (\w+)', cmds[wire])
    if res:
        return ~ get_value(res.group(1), cmds)

    return get_value(cmds[wire], cmds)

def get_value(wire, cmds):
    if type(wire) is int or wire.isdigit():
        return int(wire)

    if type(cmds[wire]) is int or cmds[wire].isdigit():
        return int(cmds[wire])

    cmds[wire] = parse_wire(wire, cmds)

    return cmds[wire]


ex_input = open('input.txt', 'r')

cmds = {}
for line in ex_input:
    cmd  = get_cmd(line)
    cmds[cmd['wire']] = cmd['cmd']

print get_value('a', cmds)
