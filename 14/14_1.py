import re

def get_cmd(line):
    pattern = re.compile('(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.')
    res = re.search(pattern, line)

    return {
        'name': res.group(1),
        'speed': int(res.group(2)),
        'uptime': int(res.group(3)),
        'downtime': int(res.group(4))
    }

ex_input = open('input.txt', 'r')

time = 2503
distances = {}
for line in ex_input:
    distance_travelled = 0
    stats = get_cmd(line)
    cycle_distance = stats['speed'] * stats['uptime']
    cycle_time = stats['uptime'] + stats['downtime']
    full_cycles = int(time / cycle_time)
    distance_travelled += cycle_distance * full_cycles
    last_cycle_uptime = max(time % cycle_time, stats['uptime'])
    distance_travelled += stats['speed'] * last_cycle_uptime
    distances[stats['name']] = distance_travelled

print distances
