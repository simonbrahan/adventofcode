import datetime

designers_favourite_number = 1364

start_time = datetime.datetime.now()

explored_points = {}
def point_explored(x, y):
    global explored_points

    content_hash = str([x, y])

    if content_hash in explored_points:
        return True

    explored_points[content_hash] = True

    return False


def position_is_valid(x, y):
    global designers_favourite_number

    if x < 0 or y < 0:
        return False

    hash_num = x*x + 3*x + 2*x*y + y + y*y + designers_favourite_number

    return "{0:b}".format(hash_num).count('1') % 2 == 0


def get_adjacent_points(x, y):
    return (
        (x, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x, y + 1)
    )


queue = [(1, 1, 0)]
while len(queue) > 0:
    x, y, num_turns = queue.pop(0)
    if num_turns > 50:
        continue

    if not position_is_valid(x, y):
        continue

    if point_explored(x, y):
        continue

    for next_x, next_y in get_adjacent_points(x, y):
        queue.append((next_x, next_y, num_turns + 1))

print len(explored_points)

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
