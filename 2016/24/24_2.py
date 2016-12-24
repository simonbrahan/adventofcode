import networkx, itertools, datetime

start_time = datetime.datetime.now()

rows = []
for line in open('input'):
    rows.append(line.strip())

num_rows, num_columns = len(rows), len(rows[0])
hit_locations = {}

#
# Build the maze
# The generator builds a graph of num_rows by num_columns, with each node connected horizintally and vertically to its neighbours
# Any nodes containing '#' (walls in the input) are removed, and any hit locations are recorded
#
maze = networkx.generators.classic.grid_2d_graph(num_rows, num_columns)
for y in xrange(num_rows):
    for x in xrange(num_columns):
        if rows[y][x] == '#':
            maze.remove_node((y, x))

        if rows[y][x].isdigit():
            hit_locations[int(rows[y][x])] = (y, x)

num_locations = len(hit_locations)

#
# Calculate distances between each hit location
# Once this is known, the puzzle is a travelling salesman problem
#
hit_location_distances = {}
for i in xrange(num_locations):
  for j in xrange(num_locations):
    hit_location_distances[i, j] = networkx.shortest_path_length(maze, hit_locations[i], hit_locations[j])
    # Store distance both ways to allow permutations below to try either direction
    hit_location_distances[j, i] = hit_location_distances[i, j]

#
# Iterate through all possible paths, finding length and comparing with previous best
#
best = None
for p in itertools.permutations(range(1, num_locations)):
    hit_location_plan = [0] + list(p) + [0]
    time = sum(
        hit_location_distances[ hit_location_plan[location + 1], hit_location_plan[location] ] for location in xrange(len(hit_location_plan) - 1))

    if best is None or time < best:
        best = time

print best

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
