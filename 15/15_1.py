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

ingredients = {}
for line in ex_input:
    ingredient = get_cmd(line)
    ingredients[ingredient['name']] = ingredient

highest_score = 0
spoonfuls = 100
for i in range(spoonfuls + 1):
    for j in range(spoonfuls - i + 1):
        for k in range(spoonfuls - i - j + 1):
            l = spoonfuls - i - j - k
