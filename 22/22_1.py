import copy
import datetime
from local_lib import *
start_time = datetime.datetime.now()

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

spells = [poison, recharge, missile, drain, shield]

start_state = State()
start_state.boss_health = 58
start_state.boss_damage = 9
start_state.my_health = 50
start_state.my_mana = 500

queue = [Node(spell, copy.deepcopy(start_state)) for spell in spells]

while len(queue) > 0:
    node = queue.pop(0)

    # If game state does not last another turn, ignore
    if not play_tick(node.state, node.spell):
        continue

    # If game can continue, queue next options
    for spell in spells:
        queue.append(Node(spell, copy.deepcopy(node.state)))

print 'Cheapest kill:', get_minimum_spent()
print 'Script took', datetime.datetime.now() - start_time
