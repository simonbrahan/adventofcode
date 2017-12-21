from pathfinder import parse_input, get_group

connections = parse_input(open('input.txt'))

connections_in_group = get_group(0, connections)

print len(connections_in_group)
