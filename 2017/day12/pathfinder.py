def parse_input(input_file):
    connections = {}

    for line in input_file:
        line_parts = map(lambda x: x.strip(','), line.split())
        connections[int(line_parts[0])] = map(int, line_parts[2:])

    return connections


def get_group(root_id, connections):
    connections_in_group = set()
    connections_to_follow = [root_id]

    while len(connections_to_follow) > 0:
        follow_connection = connections_to_follow.pop(0)
        new_connections = [
            con for con in connections[follow_connection]
            if con not in connections_in_group
        ]

        connections_to_follow += new_connections
        connections_in_group.update(new_connections)

    return connections_in_group

def get_groups(connections):
    groups = []
    found_programs = set()

    for connection in connections.keys():
        if connection in found_programs:
            continue

        connection_group = get_group(connection, connections)
        groups.append(connection_group)
        found_programs.update(connection_group)

    return groups
