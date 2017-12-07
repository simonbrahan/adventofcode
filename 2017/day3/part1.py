from sys import argv
from ulamcoords import find_ulam_coords

ulam_coords = find_ulam_coords(int(argv[1]))
manhattan_distance = abs(ulam_coords[0]) + abs(ulam_coords[1])

print 'coords', ulam_coords, 'manhattan distance', manhattan_distance
