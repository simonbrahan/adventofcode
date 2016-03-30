import itertools
import math

weapons = (
    { 'name': 'Dagger', 'damage': 4, 'cost': 8 },
    { 'name': 'Shortsword', 'damage': 5, 'cost': 10 },
    { 'name': 'Warhammer', 'damage': 6, 'cost': 25 },
    { 'name': 'Longsword', 'damage': 7, 'cost': 40 },
    { 'name': 'Greataxe', 'damage': 8, 'cost': 74 }
)

armours = (
    { 'name': 'None', 'armour': 0, 'cost': 0 },
    { 'name': 'Leather', 'armour': 1, 'cost': 13 },
    { 'name': 'Chainmail', 'armour': 2, 'cost': 31 },
    { 'name': 'Splintmail', 'armour': 3, 'cost': 53 },
    { 'name': 'Bandedmail', 'armour': 4, 'cost': 75 },
    { 'name': 'Platemail', 'armour': 5, 'cost': 102 }
)

rings = (
    { 'name': 'None', 'cost': 0 },
    { 'name': 'Damage +1', 'cost': 25, 'damage': 1 },
    { 'name': 'Damage +2', 'cost': 50, 'damage': 2 },
    { 'name': 'Damage +3', 'cost': 100, 'damage': 3 },
    { 'name': 'Defense +1', 'cost': 20, 'armour': 1 },
    { 'name': 'Defense +2', 'cost': 40, 'armour': 2 },
    { 'name': 'Defense +3', 'cost': 80, 'armour': 3 }
)

# All combinations of two ringswith no duplicates, plus the empty handed option
ring_combos = itertools.chain(
    [[rings[0], rings[0]]],
    itertools.combinations(rings, 2)
)

boss_start_hp = 104
boss_damage = 8
boss_armour = 1
my_start_hp = 100

losing_cost = 0
for left_ring, right_ring in ring_combos:
    for weapon in weapons:
        for armour in armours:
            my_armour = armour['armour'] + left_ring.get('armour', 0) + right_ring.get('armour', 0)
            my_damage = weapon['damage'] + left_ring.get('damage', 0) + right_ring.get('damage', 0)
            cost = armour['cost'] + weapon['cost'] + left_ring['cost'] + right_ring['cost']

            boss_dpt = max(1, boss_damage - my_armour)
            my_dpt = max(1, my_damage - boss_armour)

            boss_ttk = int(math.ceil(my_start_hp / float(boss_dpt)))
            my_ttk = int(math.ceil(boss_start_hp / float(my_dpt)))

            if my_ttk > boss_ttk and cost > losing_cost:
                losing_cost = cost

print losing_cost
