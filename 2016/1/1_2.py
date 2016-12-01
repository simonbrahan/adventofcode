def change_direction(current_direction, turn):
    directions = ['north', 'east', 'south', 'west']
    current_direction_idx = directions.index(current_direction)

    if turn is 'L':
        direction_mod = -1
    else:
        direction_mod = 1

    new_direction_idx = (current_direction_idx + direction_mod) % 4

    return directions[new_direction_idx]


def move_to_new_position(num_blocks):
    import copy

    global position
    global direction
    global prev_positions

    for i in range(num_blocks):
        if direction is 'north':
            position['y'] += 1

        if direction is 'east':
            position['x'] += 1

        if direction is 'south':
            position['y'] -= 1

        if direction is 'west':
            position['x'] -= 1

        if position in prev_positions:
            return True
        else:
            prev_positions.append(copy.deepcopy(position))

    return False

input_str = open('input', 'r').read().strip()

input_arr = input_str.split(', ')

position = { 'x': 0, 'y': 0 }

direction = 'north'

prev_positions = []

for instr in input_arr:
    turn = instr[0]
    num_blocks = int(instr[1:])

    direction = change_direction(direction, turn)

    if move_to_new_position(num_blocks):
        break

print 'final position:', position, abs(position['x']) + abs(position['y']), 'blocks from start point'
