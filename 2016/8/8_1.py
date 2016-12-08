def do_instruction(instr, screen):
    if instr.startswith('rect'):
        return add_rect(instr, screen)
    else:
        return do_rotate(instr, screen)


def add_rect(instr, screen):
    import re
    fill_x, fill_y = [int(i) for i in re.findall('\d+', instr)]

    for x in range(fill_x):
        for y in range(fill_y):
            screen[y][x] = True


def do_rotate(instr, screen):
    import re
    matches = re.search('rotate (row|column) \w\=(\d+) by (\d+)', instr)
    direction, position, distance =  matches.group(1), int(matches.group(2)), int(matches.group(3))

    if direction == 'row':
        do_rotate_row(position, distance, screen)
    else:
        do_rotate_column(position, distance, screen)


def do_rotate_row(position, distance, screen):
    screen[position] = rotate(screen[position], distance)


def do_rotate_column(position, distance, screen):
    column = [ row[position] for row in screen ]
    column = rotate(column, distance)

    for row, pixel in enumerate(column):
        screen[row][position] = pixel


def rotate(target, distance):
    return target[-distance:] + target[:-distance]


screen = [
    [ False for i in range(50)]
    for j in range(6)
]

for line in open('input', 'r'):
    do_instruction(line.strip(), screen)

print sum(row.count(True) for row in screen)
