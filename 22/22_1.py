boss_start_hp = 59
boss_damage = 9

my_start_hp = 50
my_mana = 500
my_start_armour = 0

class Spell:
    cost = 0
    damage = 0
    heal = 0
    armour = 0
    mana = 0


class DurationSpell(Spell):
    tick = 0

    def activate(self):
        self.tick = 1

    def is_active(self):
        return self.tick > 0

    def turn_done(self):
        if self.tick is 0:
            return

        if self.tick > max_ticks:
            self.tick = 0
            return

        self.tick += 1


class Missile(Spell):
    cost = 53
    damage = 4


class Drain(Spell):
    cost = 73
    damage = 2
    heal = 2


class Shield(DurationSpell):
    cost = 113
    armour = 7
    num_ticks = 6


class Poison(DurationSpell):
    cost = 173
    damage = 3
    num_ticks = 6


class Recharge(DurationSpell):
    cost = 229
    mana = 101
    num_ticks = 5


class SpellBook:
    spells = []
    recharge = None

    def __init__(self, spells):
        self.spells = spells

    def get_castable(self, available_mana):
        output = []
        for spell in self.spells:
            if isinstance(spell, DurationSpell):
                if spell.cost <= available_mana and not spell.is_active():
                    output.append(spell)
            elif isinstance(spell, Spell) and spell.cost <= available_mana:
                output.append(spell)

        return output


book = SpellBook([Missile(), Drain(), Shield(), Poison(), Recharge()])

print book.get_castable(500)
