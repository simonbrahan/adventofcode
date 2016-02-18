import re

def get_cmd(line):
    pattern = re.compile('(turn on|turn off|toggle) (\d{1,3}),(\d{1,3}) through (\d{1,3}),(\d{1,3})')
    res = re.search(pattern, line)

    return {
        'cmd': res.group(1),
        'start_x': int(res.group(2)),
        'start_y': int(res.group(3)),
        'end_x': int(res.group(4)),
        'end_y': int(res.group(5))
    }

def turn_on(val):
    return val + 1

def turn_off(val):
    if val == 0:
        return 0

    return val - 1

def toggle(val):
    return val + 2

grid = [[0 for i in range(1000)] for j in range(1000)]

ex_input = open('input.txt', 'r')

opts = {
    'turn off': turn_off,
    'turn on': turn_on,
    'toggle': toggle
}

for line in ex_input:
    cmd = get_cmd(line)
    for i in range(cmd['start_x'], cmd['end_x']+1):
        for j in range(cmd['start_y'], cmd['end_y']+1):
            grid[i][j] = opts[cmd['cmd']](grid[i][j])

print sum(sum(row) for row in grid)
