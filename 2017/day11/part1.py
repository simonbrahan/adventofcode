from sys import argv

def get_pos(path):
    path_steps = [step.strip() for step in path.split(',')]

    pos = [0, 0]

    pos_mods = {
        'n': (1, 1),
        'ne': (1, 0),
        'se': (0, -1),
        's': (-1, -1),
        'sw': (-1, 0),
        'nw': (0, 1)
    }

    for step in path_steps:
        pos_mod = pos_mods[step]
        pos[0] += pos_mod[0]
        pos[1] += pos_mod[1]

    return pos


def get_steps_home(pos):
    return max(abs(final_pos[0]), abs(final_pos[1]))


final_pos = get_pos(argv[1])

print final_pos

print get_steps_home(final_pos)
