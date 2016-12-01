ex_input = open('input.txt', 'r')
distance_between_places = {}
routes = []

for line in ex_input:
    start, ignore, end, ignore, distance = line.split(' ')
    distance = int(distance)

    if start not in distance_between_places:
        distance_between_places[start] = []

    distance_between_places[start].append({ 'loc': end, 'distance': distance })

    if end not in distance_between_places:
        distance_between_places[end] = []

    distance_between_places[end].append({ 'loc': start, 'distance': distance })

for place in distance_between_places:
    distance_between_places[place].sort(key = lambda val: val['distance'])
    distance_between_places[place].reverse()

# Starting from each place in turn, get the longest available route
# by always going to the furthest unvisited node
longest_route = 0
for place in distance_between_places:
    visited = dict.fromkeys(place for place in distance_between_places)
    visited[place] = True
    current_place = place
    current_route = 0

    # While there are unvisited nodes...
    while None in visited.values():
        # For each destination from current place...
        for destination in distance_between_places[current_place]:
            # If destination has not been visited...
            if not visited[destination['loc']]:
                # Move to destination
                # It is known to be the furthest destination due to the sort by distance above
                current_route += destination['distance']
                visited[destination['loc']] = True
                current_place = destination['loc']
                break

    if current_route > longest_route:
        longest_route = current_route

print longest_route
