def parse_instruction(line):
    parts = line.split()

    if parts[0] == 'cpy':
        output = ['cpy']

        if parts[1].isdigit():
            output.append(int(parts[1]))
        else:
            output.append(parts[1])

        output.append(parts[2])
    elif parts[0] in [ 'inc', 'dec' ]:
        output = [ parts[0], parts[1] ]
    elif parts[0] == 'jnz':
        output = ['jnz']

        if parts[1].isdigit():
            output.append(int(parts[1]))
        else:
            output.append(parts[1])

        output.append(int(parts[2]))

    return output


def do_cpy(val, register):
    global state

    if type(val) is int:
        state[register] = val
    else:
        state[register] = state[val]


def do_inc(register):
    global state

    state[register] += 1


def do_dec(register):
    global state

    state[register] -= 1


def do_jnz(val, jump):
    global state

    if type(val) is int:
        check = val
    else:
        check = state[val]

    if check != 0:
        state['pointer'] += jump
    else:
        state['pointer'] += 1


instructions = []
for line in open('input', 'r'):
    instructions.append(parse_instruction(line.strip()))

state = {
    'pointer': 0,
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

while state['pointer'] < len(instructions):
    instr = instructions[state['pointer']]
    if instr[0] == 'cpy':
        do_cpy(instr[1], instr[2])
    elif instr[0] == 'inc':
        do_inc(instr[1])
    elif instr[0] == 'dec':
        do_dec(instr[1])
    elif instr[0] == 'jnz':
        do_jnz(instr[1], instr[2])
        # jnz already moves pointer, so no need to increment it afterwards
        continue

    state['pointer'] += 1

print state
