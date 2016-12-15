import re

explored_states = {}
def state_explored(floor_contents):
    global explored_states

    content_hash = ':'.join([ ''.join(sorted(floor)) for floor in floor_contents])

    if content_hash in explored_states:
        return True

    explored_states[content_hash] = True

    return False


def make_move(floor_contents, current_floor, next_floor, move_items):
    import copy
    new_floor_contents = copy.deepcopy(floor_contents)

    new_floor_contents[current_floor] = list(set(new_floor_contents[current_floor]) - set(move_items))

    new_floor_contents[next_floor] += move_items

    return new_floor_contents


def valid_floor_contents(floor_contents):
    import re

    for floor in floor_contents:
        # Only floors with a generator can cause problems
        if not any([ item for item in floor if ' generator' in item ]):
            continue

        for item in floor:
            is_chip = re.match('(\w+)-compatible microchip', item)
            if not is_chip:
                continue

            chip_type = is_chip.group(1)

            # floor contains at least one generator, but no generator for this chip
            if chip_type + ' generator' not in floor:
                return False

    return True


def explore_moves(floor_contents, current_floor, num_moves):
    import itertools

    if state_explored(floor_contents):
        return

    # If first, second and third floor are empty, everything is on floor 4 and we've won
    if floor_contents[0] == floor_contents[1] == floor_contents[2] == []:
        print num_moves
        return True

    floor_below = current_floor - 1
    floor_above = current_floor + 1
    possible_moves = itertools.combinations(floor_contents[current_floor] + [None], 2)

    if floor_above < len(floor_contents):
        for move_items in possible_moves:
            new_floor_contents = make_move(
                floor_contents,
                current_floor,
                floor_above,
                filter(None, move_items)
            )

            if valid_floor_contents(new_floor_contents):
                explore_moves(new_floor_contents, floor_above, num_moves + 1)

    if floor_below >= 0:
        for move_items in possible_moves:
            new_floor_contents = make_move(
                floor_contents,
                current_floor,
                floor_below,
                filter(None, move_items)
            )

            if valid_floor_contents(new_floor_contents):
                explore_moves(new_floor_contents, floor_below, num_moves + 1)


floor_contents = [ [], [], [], [] ]
for idx, line in enumerate(open('input', 'r')):
    floor_contents[idx] = re.findall('(\w+-compatible microchip)', line) + re.findall('(\w+ generator)', line)

explore_moves(floor_contents, 0, 0)
