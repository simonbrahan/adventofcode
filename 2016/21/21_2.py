import datetime, itertools, re

def swap_pos(password, swap_pos, with_pos):
    password_list = list(password)
    swap_char = password_list[swap_pos]

    password_list[swap_pos] = password_list[with_pos]
    password_list[with_pos] = swap_char

    return ''.join(password_list)


def swap_char(password, swap_char, with_char):
    password = password.replace(swap_char, '[SWAP_PLACEHOLDER]')
    password = password.replace(with_char, swap_char)
    password = password.replace('[SWAP_PLACEHOLDER]', with_char)

    return password


def reverse_section(password, from_pos, to_pos):
    left_part = password[:from_pos] if from_pos > 0 else ''
    middle_part = ''.join(reversed(password[from_pos:to_pos + 1]))
    right_part = password[to_pos + 1:]

    return left_part + middle_part + right_part


def rotate(password, direction, num_steps):
    num_steps = num_steps % len(password)

    if direction == 'left':
        return password[num_steps:] + password[:num_steps]
    else:
        return password[-num_steps:] + password[0:-num_steps]


def move_pos_to(password, from_pos, to_pos):
    password_list = list(password)
    move_char = password_list.pop(from_pos)
    password_list.insert(to_pos, move_char)
    return ''.join(password_list)


def rotate_from_char(password, char):
    idx = password.index(char)
    num_steps = 1 + idx
    if idx >= 4:
        num_steps += 1

    return rotate(password, 'right', num_steps)


start_time = datetime.datetime.now()

match_hash = 'fbgdceah'

instrs = [ line.strip() for line in open('input', 'r') ]

for password in itertools.permutations(match_hash):
    password = start_password = ''.join(password)
    for instr in instrs:
        match = re.match('swap position (\d+) with position (\d+)', instr)
        if match:
            password = swap_pos(password, int(match.group(1)), int(match.group(2)))

        match = re.match('swap letter (\w) with letter (\w)', instr)
        if match:
            password = swap_char(password, match.group(1), match.group(2))

        match = re.match('reverse positions (\d+) through (\d+)', instr)
        if match:
            password = reverse_section(password, int(match.group(1)), int(match.group(2)))

        match = re.match('rotate (left|right) (\d+) steps*', instr)
        if match:
            password = rotate(password, match.group(1), int(match.group(2)))

        match = re.match('move position (\d+) to position (\d+)', instr)
        if match:
            password = move_pos_to(password, int(match.group(1)), int(match.group(2)))

        match = re.match('rotate based on position of letter (\w)', instr)
        if match:
            password = rotate_from_char(password, match.group(1))

    if password == match_hash:
        print start_password

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
