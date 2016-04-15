import copy

import datetime

start_time = datetime.datetime.now()

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


'''
Is passed node equal to any node in passed list
Return true if equivalent node is in list, false otherwise
'''
def node_checked(candidate_node, node_list):
    for node in node_list:
        if node.spell is candidate_node.spell:
            node_state_dict = copy.copy(node.state.__dict__)
            node_state_dict['history'] = []

            candidate_node_state_dict = copy.copy(candidate_node.state.__dict__)
            candidate_node_state_dict['history'] = []

            if candidate_node_state_dict == node_state_dict:
                return True

    return False


'''
Check that spell can be cast and update mana totals in passed state
Returns true if spell can be cast, false otherwise
'''
def handle_mana(spell, state):
    if state.my_mana < spell.cost:
        return False

    state.my_mana -= spell.cost
    state.mana_spent += spell.cost

    return True

'''
Deal any damage caused by the passed spell to the boss in the passed state
'''
def handle_damage(spell, state):
    state.boss_health -= spell.damage

'''
Handle any healing caused by the passed spell to the player in the passed state
'''
def handle_heal(spell, state):
    state.my_health += spell.heal


'''
Update passed state to show activation of passed spell, if it has any effects
Returns false if an already active spell cannot be cast, true otherwise
'''
def handle_effect_activation(spell, state):
    if spell.poison_effect_ticks > 0:
        if state.poison_effect_ticks is 0:
            state.poison_effect_ticks = spell.poison_effect_ticks
            state.poison_effect_damage = spell.poison_effect_damage
        else:
            return False

    if spell.recharge_effect_ticks > 0:
        if state.recharge_effect_ticks is 0:
            state.recharge_effect_ticks = spell.recharge_effect_ticks
            state.recharge_effect_mana = spell.recharge_effect_mana
        else:
            return False

    if spell.shield_effect_ticks > 0:
        if state.shield_effect_ticks is 0:
            state.shield_effect_ticks = spell.shield_effect_ticks
            state.shield_effect_armour = spell.shield_effect_armour
        else:
            return False

    return True


'''
Carry out any changes to the passed state from active effects
'''
def handle_active_effects(state):
    if state.poison_effect_ticks > 0:
        state.boss_health -= spell.poison_effect_damage
        state.poison_effect_ticks -= 1

    if state.recharge_effect_ticks > 0:
        state.my_mana += state.recharge_effect_mana
        state.recharge_effect_ticks -= 1

    if state.shield_effect_ticks > 0:
        state.my_armour = state.shield_effect_armour
        state.shield_effect_ticks -= 1
    else:
        state.my_armour = 0


'''
Deal damage from boss according to passed state
Return true if player is still alive, false otherwise
'''
def handle_boss_damage(state):
    boss_damage = max(state.boss_damage - state.my_armour, 1)

    state.my_health -= boss_damage

    return state.my_health > 0


missile = Spell('Missile')
missile.cost = 53
missile.damage = 4

drain = Spell('Drain')
drain.cost = 73
drain.damage = 2
drain.heal = 2

shield = Spell('Shield')
shield.cost = 113
shield.shield_effect_ticks = 6
shield.shield_effect_armour = 7

poison = Spell('Poison')
poison.cost = 173
poison.poison_effect_ticks = 6
poison.poison_effect_damage = 3

recharge = Spell('Recharge')
recharge.cost = 229
recharge.recharge_effect_ticks = 5
recharge.recharge_effect_mana = 101

spells = [missile, drain, shield, poison, recharge]

start_state = State()
start_state.boss_health = 58
start_state.boss_damage = 9
start_state.my_health = 50
start_state.my_mana = 500

queue = [Node(spell, start_state) for spell in spells]

minimum_spent = None
checked_nodes = []

while len(queue) > 0:
    node = queue.pop(0)

    ## If game state has been visited before, no need to continue
    if node_checked(node, checked_nodes):
        continue

    checked_nodes.append(node)

    # If game is more expensive than current minimum, no need to continue checking
    if not minimum_spent is None and node.state.mana_spent >= minimum_spent:
        continue

    # Effects happen at the start of player's and boss's turns
    handle_active_effects(node.state)

    # If boss is dead following effects, player wins
    if node.state.boss_health <= 0:
        print 'The boss died for ', node.state.mana_spent, 'spent'
        print 'History:', node.state.history

        if minimum_spent is None or node.state.mana_spent < minimum_spent:
            minimum_spent = node.state.mana_spent

        continue

    if not handle_mana(node.spell, node.state):
        continue

    if not handle_effect_activation(node.spell, node.state):
        continue

    node.state.history.append(node.spell.name)

    handle_damage(node.spell, node.state)
    handle_heal(node.spell, node.state)

    # Boss's turn

    # Effects happen at the start of player's and boss's turns
    handle_active_effects(node.state)

    # If boss is dead following effects, player wins
    if node.state.boss_health <= 0:
        print 'The boss died for ', node.state.mana_spent, 'spent'
        print 'History:', node.state.history

        if minimum_spent is None or node.state.mana_spent < minimum_spent:
            minimum_spent = node.state.mana_spent

        continue

    if not handle_boss_damage(node.state):
        continue

    for spell in spells:
        queue.append(Node(spell, copy.deepcopy(node.state)))

print 'Cheapest kill:', minimum_spent
print 'Script took', datetime.datetime.now() - start_time
