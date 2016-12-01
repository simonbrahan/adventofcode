import re

def get_cmd(line):
    pattern = re.compile('Sue (\d+): (\w+): (\d+), (\w+): (\d+), (\w+): (\d+)')
    res = re.search(pattern, line)

    return {
        'suerial': int(res.group(1)),
        'things': {
            res.group(2): int(res.group(3)),
            res.group(4): int(res.group(5)),
            res.group(6): int(res.group(7))
        }
    }

def sue_matches(sue, match):
    for label, count in sue['things'].items():
        if label in ('cats', 'trees'):
            if count <= match[label]:
                return False
        elif label in ('pomeranians', 'goldfish'):
            if count >= match[label]:
                return False
        elif match[label] != count:
            return False

    return True

match = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

ex_input = open('input.txt', 'r')

for line in ex_input:
    sue_things = get_cmd(line)
    if sue_matches(sue_things, match):
        print sue_things['suerial']
