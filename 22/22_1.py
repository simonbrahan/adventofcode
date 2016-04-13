import copy

class Spell:
    def __init__(self, name):
        self.name = name
        self.cost = 0

        self.damage = 0
        self.heal = 0

        self.poison_effect_ticks = 0
        self.poison_effect_damage = 0

        self.shield_effect_ticks = 0
        self.shield_effect_armour = 0

        self.recharge_effect_ticks = 0
        self.recharge_effect_mana = 0


class State:
    def __init__(self):
        self.boss_health = 0
        self.boss_damage = 0
        self.my_health = 0
        self.my_mana = 0
        self.my_armour = 0

        self.poison_effect_ticks = 0
        self.poison_effect_damage = 0

        self.shield_effect_ticks = 0
        self.shield_effect_armour = 0

        self.recharge_effect_ticks = 0
        self.recharge_effect_mana = 0

        self.mana_spent = 0

        self.history = []


class Node:
    def __init__(self, spell, state):
        self.spell = spell
        self.state = state

def handle_mana(spell, state):
    if state.my_mana < spell.cost:
        return False

    state.my_mana -= spell.cost
    state.mana_spent += spell.cost

    return True


def handle_damage(spell, state):
    state.boss_health -= spell.damage


def handle_heal(spell, state):
    state.my_health += spell.heal


def handle_effect_activation(spell, state):
    if state.poison_effect_ticks is 0:
        state.poison_effect_ticks = spell.poison_effect_ticks
        state.poison_effect_damage = spell.poison_effect_damage
    elif spell.name is 'Poison':
        return False

    if state.recharge_effect_ticks is 0:
        state.recharge_effect_ticks = spell.recharge_effect_ticks
        state.recharge_effect_mana = spell.recharge_effect_mana
    elif spell.name is 'Recharge':
        return False

    return True

def handle_active_effects(state):
    if state.poison_effect_ticks > 0:
        state.boss_health -= spell.poison_effect_damage
        state.poison_effect_ticks -= 1

    if state.recharge_effect_ticks > 0:
        state.my_mana += state.recharge_effect_mana
        state.recharge_effect_ticks -= 1


missile = Spell('Missile')
missile.cost = 53
missile.damage = 4

drain = Spell('Drain')
drain.cost = 73
drain.damage = 2
drain.heal = 2

poison = Spell('Poison')
poison.cost = 173
poison.poison_effect_ticks = 6
poison.poison_effect_damage = 3

recharge = Spell('Recharge')
recharge.cost = 229
recharge.recharge_effect_ticks = 5
recharge.recharge_effect_mana = 101

spells = [poison, recharge, drain]

start_state = State()
start_state.boss_health = 18
start_state.boss_damage = 9
start_state.my_health = 50
start_state.my_mana = 500

queue = [Node(spell, start_state) for spell in spells]

while len(queue) > 0:
    node = queue.pop(0)

    handle_active_effects(node.state)

    if node.state.boss_health <= 0:
        print 'The boss died for ', node.state.mana_spent, 'spent'
        print 'History:', node.state.history
        continue

    if not handle_mana(node.spell, node.state):
        continue

    if not handle_effect_activation(node.spell, node.state):
        continue

    node.state.history.append(node.spell.name)

    handle_damage(node.spell, node.state)
    handle_heal(node.spell, node.state)

    for spell in spells:
        queue.append(Node(spell, copy.deepcopy(node.state)))
