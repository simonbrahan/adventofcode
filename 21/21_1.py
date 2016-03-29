import itertools

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

for left_ring, right_ring in ring_combos:
    for weapon in weapons:
        for armour in armours:
            my_armour = armour['armour'] + left_ring.get('armour', 0) + left_ring.get('armour', 0)
            my_damage = weapon['damage'] + left_ring.get('damage', 0) + left_ring.get('damage', 0)
            cost = armour['cost'] + weapon['cost'] + left_ring['cost'] + right_ring['cost']
            print 'weapon:', weapon['name'], 'armour:', armour['name']
            print 'left:', left_ring['name'], 'right:', right_ring['name']
            print 'damage:', my_damage, 'armour:', my_armour, 'cost:', cost

boss_hp = 104
boss_damage = 8
boss_armour = 1

my_hp = 100
