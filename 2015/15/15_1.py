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


def get_recipe_score(ingredients, recipe):
    capacity = 0
    durability = 0
    flavour = 0
    texture = 0
    calories = 0

    for label, quantity in recipe.items():
        capacity += quantity * ingredients[label]['capacity']
        durability += quantity * ingredients[label]['durability']
        flavour += quantity * ingredients[label]['flavour']
        texture += quantity * ingredients[label]['texture']
        calories += quantity * ingredients[label]['calories']

    return {
        'score': max(capacity, 0) * max(durability, 0) * max(flavour, 0) * max(texture, 0),
        'cals': calories
    }


ex_input = open('input.txt', 'r')

ingredients = {}
for line in ex_input:
    ingredient = get_cmd(line)
    ingredients[ingredient['name']] = ingredient

high_score = 0
spoonfuls = 100
for i in range(spoonfuls + 1):
    recipe = { 'Frosting': i }
    for j in range(spoonfuls - i + 1):
        recipe['Candy'] = j
        for k in range(spoonfuls - i - j + 1):
            recipe['Butterscotch'] = k
            recipe['Sugar'] = spoonfuls - i - j - k
            recipe_stats = get_recipe_score(ingredients, recipe)

            if recipe_stats['cals'] == 500:
                high_score = max(recipe_stats['score'], high_score)

print high_score
