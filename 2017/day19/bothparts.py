def in_maze(pos):
    return -1 < pos[1] < len(maze) and -1 < pos[0] < len(maze[pos[1]])


def on_path(pos):
    return in_maze(pos) and maze[pos[1]][pos[0]] is not ' '


def get_next(pos, orientation):
    find_next = {
        'north': lambda pos: (pos[0], pos[1] - 1),
        'east': lambda pos: (pos[0] + 1, pos[1]),
        'south': lambda pos: (pos[0], pos[1] + 1),
        'west': lambda pos: (pos[0] - 1, pos[1])
    }

    candidate_orientations = [orientation] + get_turns(orientation)

    for new_orientation in candidate_orientations:
        new_pos = find_next[new_orientation](pos)
        if on_path(new_pos):
            return new_pos, new_orientation

    return False, orientation


def get_turns(orientation):
    dirs = ('north', 'east', 'south', 'west')
    turn_dirs = (-1, 1)

    return [dirs[(dirs.index(orientation) + turn_dir) % 4] for turn_dir in turn_dirs]


with open('input.txt') as input_file:
    maze = [list(line.rstrip()) for line in input_file]

pos = (maze[0].index('|'), 0)
orientation = 'south'
chars = []
path_count = 0

while pos:
    path_count += 1
    char_at_pos = maze[pos[1]][pos[0]]

    if char_at_pos.isalpha():
        chars.append(char_at_pos)

    pos, orientation = get_next(pos, orientation)

print ''.join(chars)
print 'path is', path_count, 'steps'
