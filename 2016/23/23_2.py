import datetime

def parse_instruction(line):
    parts = line.split()

    if parts[0] == 'cpy':
        output = ['cpy']

        try:
            val = int(parts[1])
        except:
            val = parts[1]

        output.append(val)

        output.append(parts[2])
    elif parts[0] in [ 'inc', 'dec' ]:
        output = [ parts[0], parts[1] ]
    elif parts[0] == 'jnz':
        output = ['jnz']

        for i in range(1, 3):
            try:
                val = int(parts[i])
            except:
                val = parts[i]

            output.append(val)

    elif parts[0] == 'tgl':
        output = ['tgl']

        try:
            val = int(parts[1])
        except:
            val = parts[1]

        output.append(val)

    elif parts[0] == 'mul':
        output = ['mul']

        for i in range(1, 3):
            try:
                val = int(parts[i])
            except:
                val = parts[i]

            output.append(val)

        output.append(parts[3])

    return output


def do_cpy(val, register):
    global state

    if type(register) is int:
        return

    if type(val) is int:
        state[register] = val
    else:
        state[register] = state[val]


def do_inc(register):
    global state

    if type(register) is int:
        return

    state[register] += 1


def do_dec(register):
    global state

    if type(register) is int:
        return

    state[register] -= 1


def do_jnz(val, jump):
    global state

    if type(val) is int:
        check = val
    else:
        check = state[val]

    if not type(jump) is int:
        jump = state[jump]

    if check != 0:
        state['pointer'] += jump
    else:
        state['pointer'] += 1

def do_tgl(val):
    global state
    global instructions

    if not type(val) is int:
        val = state[val]

    val += state['pointer']

    if val >= len(instructions):
        return

    instr = instructions[val][0]

    if instr in ['tgl', 'dec']:
        instructions[val][0] = 'inc'
    elif instr == 'inc':
        instructions[val][0] = 'dec'
    elif instr == 'cpy':
        instructions[val][0] = 'jnz'
    elif instr == 'jnz':
        instructions[val][0] = 'cpy'


def do_mul(a, b, register):
    global state

    if not type(a) is int:
        a = state[a]

    if not type(b) is int:

        b = state[b]

    state[register] = a * b


instructions = []
for line in open('input', 'r'):
    instructions.append(parse_instruction(line.strip()))

state = {
    'pointer': 0,
    'a': 12,
    'b': 0,
    'c': 0,
    'd': 0
}

start_time = datetime.datetime.now()

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
    elif instr[0] == 'tgl':
        do_tgl(instr[1])
    elif instr[0] == 'mul':
        do_mul(instr[1], instr[2], instr[3])

    state['pointer'] += 1

print state

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
