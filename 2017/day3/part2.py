from sys import argv
from collections import defaultdict
from ulamcoords import find_ulam_coords

def sum_adjacent(matrix, coords):
    return sum([
        matrix[coords[0] - 1].get(coords[1] - 1, 0),
        matrix[coords[0] - 1].get(coords[1], 0),
        matrix[coords[0] - 1].get(coords[1] + 1, 0),
        matrix[coords[0]].get(coords[1] - 1, 0),
        matrix[coords[0]].get(coords[1] + 1, 0),
        matrix[coords[0] + 1].get(coords[1] - 1, 0),
        matrix[coords[0] + 1].get(coords[1], 0),
        matrix[coords[0] + 1].get(coords[1] + 1, 0)
    ])


input = int(argv[1])

latest_val = 1
matrix = defaultdict(dict)
matrix[0] = {0: 1}
position_num = 2
while latest_val < input:
    coords = find_ulam_coords(position_num)
    next_val = sum_adjacent(matrix, coords)
    matrix[coords[0]][coords[1]] = next_val
    latest_val = next_val
    position_num += 1

print latest_val
