keypad = (
    (' ', ' ', '1', ' ', ' '),
    (' ', '2', '3', '4', ' '),
    ('5', '6', '7', '8', '9'),
    (' ', 'A', 'B', 'C', ' '),
    (' ', ' ', 'D', ' ', ' ')
)

position = { 'x': 0, 'y': 2 }

def is_valid_position(position):
    global keypad

    if position['y'] < 0 or position['y'] >= len(keypad):
        return False

    if position['x'] < 0 or position['x'] >= len(keypad[position['y']]):
        return False

    if keypad[position['y']][position['x']] is ' ':
        return False

    return True


def get_new_position(position, input_line):
    dirs = {
        'U': { 'x': 0, 'y': -1 },
        'R': { 'x': 1, 'y': 0 },
        'D': { 'x': 0, 'y': 1 },
        'L': { 'x': -1, 'y': 0 }
    }

    for char in input_line:
        new_position = {
            'x': position['x'] + dirs[char]['x'],
            'y': position['y'] + dirs[char]['y']
        }

        if is_valid_position(new_position):
            position = new_position

    return position

code = ''
for line in open('input', 'r'):
    position = get_new_position(position, line.strip())
    code += keypad[position['y']][position['x']]

print code
