import re, itertools, copy

def make_move(floor_contents, current_floor, floor_below, move_items):
    return True


def explore_moves(floor_contents, current_floor, num_moves):
    floor_below = current_floor - 1
    floor_above = current_floor + 1
    possible_moves = itertools.combinations(floor_contents[current_floor] + [None], 2)

    if floor_below in floor_contents.keys():
        for move_items in possible_moves:
            make_move(floor_contents, current_floor, floor_below, move_items)


floor_contents = [ [], [], [], [] ]
for idx, line in enumerate(open('input', 'r')):
    floor_contents[idx] = re.findall('(\w+-compatible microchip)', line) + re.findall('(\w+ generator)', line)

