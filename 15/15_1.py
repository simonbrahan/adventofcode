import re

def get_cmd(line):
    pattern = re.compile('(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')
    res = re.search(pattern, line)

    return {
        'name': res.group(1),
        'capacity': int(res.group(2)),
        'durability': int(res.group(3)),
        'flavour': int(res.group(4)),
        'texture': int(res.group(5)),
        'calories': int(res.group(6))
    }

ex_input = open('input.txt', 'r')

for line in ex_input:
    print get_cmd(line)
