with open('input.txt') as input:
    program_connections = {}
    for line in input:
        line_parts = map(lambda x: x.strip(','), line.split())
        program_connections[int(line_parts[0])] = map(int, line_parts[2:])

connections_in_group = set()
connections_to_follow = [0]

while len(connections_to_follow) > 0:
    follow_connection = connections_to_follow.pop(0)
    new_connections = [
        con for con in program_connections[follow_connection]
        if con not in connections_in_group
    ]

    connections_to_follow += new_connections
    connections_in_group.update(new_connections)

print len(connections_in_group)
