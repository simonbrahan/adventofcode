import datetime

def is_trap(idx, last_row):
    trap_above = last_row[idx]

    if idx == 0:
        trap_left = False
    else:
        trap_left = last_row[idx-1]

    if idx == len(last_row) - 1:
        trap_right = False
    else:
        trap_right = last_row[idx+1]

    if trap_left and trap_above and not trap_right:
        return True

    if not trap_left and trap_above and trap_right:
        return True

    if trap_left and not trap_above and not trap_right:
        return True

    if not trap_left and not trap_above and trap_right:
        return True

    return False


input_str = '^^.^..^.....^..^..^^...^^.^....^^^.^.^^....^.^^^...^^^^.^^^^.^..^^^^.^^.^.^.^.^.^^...^^..^^^..^.^^^^'
room_length = 40

start_time = datetime.datetime.now()

room_width = len(input_str)
tiles = [[ char == '^' for char in input_str ]]

previous_row = tiles[0]
while len(tiles) < room_length:
    next_row = []
    for i in range(room_width):
        next_row.append(is_trap(i, previous_row))

    tiles.append(next_row)
    previous_row = next_row

print sum([ row.count(False) for row in tiles ])

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
