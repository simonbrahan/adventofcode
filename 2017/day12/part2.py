from pathfinder import parse_input, get_groups

connections = parse_input(open('input.txt'))

groups = get_groups(connections)

print len(groups)
