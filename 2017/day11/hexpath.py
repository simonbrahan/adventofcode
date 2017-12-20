def move(current_pos, move_dir):
    pos_mods = {
        'n': (1, 1),
        'ne': (1, 0),
        'se': (0, -1),
        's': (-1, -1),
        'sw': (-1, 0),
        'nw': (0, 1)
    }

    return [
        current_pos[0] + pos_mods[move_dir][0],
        current_pos[1] + pos_mods[move_dir][1]
    ]


def get_steps_home(pos):
    return max(abs(pos[0]), abs(pos[1]))

