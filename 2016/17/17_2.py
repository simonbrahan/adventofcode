import collections, hashlib, datetime

def get_available_paths(passcode, current_path):
    base = passcode + ''.join(current_path)
    direction_opts = hashlib.md5(base).hexdigest()

    output = []
    for idx, direction in enumerate(['U', 'D', 'L', 'R']):
        candidate_path = current_path[:] + [direction]
        if direction_opts[idx] in 'bcdef':
            output.append(candidate_path)

    return output

def get_direction_counts(path):
    direction_counts = collections.defaultdict(int)

    for direction in path:
        direction_counts[direction] += 1

    x = direction_counts['R'] - direction_counts['L']
    y = direction_counts['D'] - direction_counts['U']

    return x, y


def is_valid_path(path):
    x, y = get_direction_counts(path)

    return 0 <= x <= 3 and 0 <= y <= 3


def reaches_finish(path):
    x, y = get_direction_counts(path)

    return x == 3 and y == 3


passcode = 'udskfozm'

start_time = datetime.datetime.now()

queue = [[]]

successful_paths = []

while len(queue) > 0:
    path = queue.pop(0)

    if not is_valid_path(path):
        continue

    if reaches_finish(path):
        successful_paths.append(''.join(path))
        continue

    for new_path in get_available_paths(passcode, path):
        queue.append(new_path)


print len(max(successful_paths, key=len))

print 'Script took', datetime.datetime.now() - start_time, 'seconds'
