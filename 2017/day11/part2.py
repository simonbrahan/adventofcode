from sys import argv
import hexpath

def get_furthest_distance(path):
    path_steps = [step.strip() for step in path.split(',')]

    pos = [0, 0]
    furthest_distance = 0

    for step in path_steps:
        pos = hexpath.move(pos, step)
        furthest_distance = max(hexpath.get_steps_home(pos), furthest_distance)

    return furthest_distance


print get_furthest_distance(argv[1])
