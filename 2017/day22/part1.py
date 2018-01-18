from collections import defaultdict

def show_grid(grid):
    grid_bounds = get_grid_bounds(grid)

    for y in range(grid_bounds[0][1], grid_bounds[1][1] + 1):
        for x in range(grid_bounds[0][0], grid_bounds[1][0] + 1):
            if grid[(x,y)]:
                print '#',
            else:
                print '.',

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


grid = defaultdict(bool)
with open('input.txt') as input_file:
    for row_idx, row in enumerate(input_file):
        for col_idx, cell in enumerate(row.strip()):
            grid[(col_idx, row_idx)] = cell is '#'

grid_bounds = get_grid_bounds(grid)
pos = (grid_bounds[1][0] / 2, grid_bounds[1][1] / 2)
direction = (0, -1)
infect_count = 0

for i in range(10000):
    if grid[pos]:
        direction = turn_right(direction)
    else:
        direction = turn_left(direction)
        infect_count += 1

    grid[pos] = not grid[pos]

    pos = (pos[0] + direction[0], pos[1] + direction[1])

show_grid(grid)
print infect_count
