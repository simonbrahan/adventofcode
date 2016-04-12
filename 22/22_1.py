import copy

class Spell:
    def __init__(self, name):
        self.name = name
        self.cost = 0
        self.damage = 0
        self.heal = 0


class State:
    def __init__(self, boss_health, boss_damage, my_health, my_mana, mana_spent):
        self.boss_health = boss_health
        self.boss_damage = boss_damage
        self.my_health = my_health
        self.my_mana = my_mana
        self.mana_spent = mana_spent


class Node:
    def __init__(self, spell, state):
        self.spell = spell
        self.state = state


missile = Spell('Missile')
missile.cost = 53
missile.damage = 10

drain = Spell('Drain')
drain.cost = 73
drain.damage = 5
drain.heal = 5

spells = [missile, drain]

start_state = State(58, 9, 50, 500, 0)

queue = [Node(spell, start_state) for spell in spells]

while len(queue) > 0:
    node = queue.pop(0)
    print 'casting', node.spell.name
    node.state.boss_health -= node.spell.damage
    node.state.my_health += node.spell.heal
    node.state.my_mana -= node.spell.cost
    node.state.mana_spent += node.spell.cost

    print 'boss now at', node.state.boss_health, 'hp'
    print 'I\'m now at', node.state.my_health, 'hp'
    print 'I have', node.state.my_mana, 'mana'
    print 'I\'ve spent', node.state.mana_spent, 'mana'

    if node.state.my_health <= 0:
        print 'I died'
        continue

    if node.state.my_mana <= 0:
        print 'I ran out of mana'
        continue

    if node.state.boss_health <= 0:
        print 'The boss died for ', node.state.mana_spent, 'spent'
        continue

    for spell in spells:
        queue.append(Node(spell, copy.copy(node.state)))
