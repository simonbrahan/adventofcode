from collections import defaultdict

def show_grid(grid):
    grid_bounds = get_grid_bounds(grid)

    chars = { 0: '.', 1: 'W', 2: '#', 3: 'F' }

    for y in range(grid_bounds[0][1], grid_bounds[1][1] + 1):
        for x in range(grid_bounds[0][0], grid_bounds[1][0] + 1):
            print chars[grid[(x,y)]],

        print '\n',


def get_grid_bounds(grid):
    xvals, yvals = zip(*grid.keys())

    return (min(xvals), min(yvals)), (max(xvals), max(yvals))


def turn_right(direction):
    return turn(direction, 1)


def turn_left(direction):
    return turn(direction, -1)


def turn(direction, turn_dir):
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    dir_idx = directions.index(direction)
    new_dir_idx = (dir_idx - turn_dir) % len(directions)

    return directions[new_dir_idx]


grid = defaultdict(int)
with open('input.txt') as input_file:
    for row_idx, row in enumerate(input_file):
        for col_idx, cell in enumerate(row.strip()):
            grid[(col_idx, row_idx)] = 2 if cell is '#' else 0

grid_bounds = get_grid_bounds(grid)
pos = (grid_bounds[1][0] / 2, grid_bounds[1][1] / 2)
direction = (0, -1)
infect_count = 0

for i in range(10000000):
    transforms = {
        0: lambda direction: turn_left(direction),
        1: lambda direction: direction,
        2: lambda direction: turn_right(direction),
        3: lambda direction: turn_left(turn_left(direction))
    }

    direction = transforms[grid[pos]](direction)

    grid[pos] = (grid[pos] + 1) % 4

    if grid[pos] is 2:
        infect_count += 1

    pos = (pos[0] + direction[0], pos[1] + direction[1])

print infect_count
