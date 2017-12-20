from sys import argv
import hexpath

def get_end_pos(path):
    path_steps = [step.strip() for step in path.split(',')]

    pos = [0, 0]

    for step in path_steps:
        pos = hexpath.move(pos, step)

    return pos


final_pos = get_end_pos(argv[1])
print hexpath.get_steps_home(final_pos)
