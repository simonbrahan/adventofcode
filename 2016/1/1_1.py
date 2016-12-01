input_str = open('input', 'r').read().strip()

input_arr = input_str.split(', ')

position = { 'x': 0, 'y': 0 }

current_direction= 'north'

def change_direction(current_direction, turn):
    directions = ['north', 'east', 'south', 'west']
    current_direction_idx = directions.index(current_direction)

    if turn is 'L':
        direction_mod = -1
    else:
        direction_mod = 1

    new_direction_idx = current_direction_idx + direction_mod

    if new_direction_idx < 0:
        new_direction_idx = len(directions) - 1

    if new_direction_idx >= len(directions):
        new_direction_idx = 0

    return directions[new_direction_idx]


def change_position(position, direction, num_blocks):
    if direction is 'north':
        position['y'] += num_blocks

    if direction is 'east':
        position['x'] += num_blocks

    if direction is 'south':
        position['y'] -= num_blocks

    if direction is 'west':
        position['x'] -= num_blocks

    return position


for instr in input_arr:
    turn = instr[0]
    num_blocks = int(instr[1:])

    current_direction = change_direction(current_direction, turn)
    position = change_position(position, current_direction, num_blocks)


print 'final position:', abs(position['x']) + abs(position['y']), 'blocks from start point'
