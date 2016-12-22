import datetime, itertools

def parse_node(line):
    line_parts = line.split()
    return int(line_parts[2][:-1]), int(line_parts[3][:-1])


start_time = datetime.datetime.now()

nodes = []
for line in open('input','r'):
    nodes.append(parse_node(line))

viable_node_count = 0
for node_a, node_b in itertools.permutations(nodes, 2):
    if node_a[0] > 0 and node_a[0] < node_b[1]:
        viable_node_count += 1

print viable_node_count

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
