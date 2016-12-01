from local_lib import *
import unittest

class TestHandleMana(unittest.TestCase):
    def test_handle_mana_cannot_cast(self):
        state = State()
        state.my_mana = 10
        state.mana_spent = 13

        spell = Spell('spell')
        spell.cost = 11

        self.assertFalse(handle_mana(spell, state))

        self.assertEqual(10, state.my_mana)
        self.assertEqual(13, state.mana_spent)


    def test_handle_mana_can_cast(self):
        state = State()
        state.my_mana = 10
        state.mana_spent = 13

        spell = Spell('spell')
        spell.cost = 10

        self.assertTrue(handle_mana(spell, state))

        self.assertEqual(0, state.my_mana)
        self.assertEqual(23, state.mana_spent)


class TestHandleDamage(unittest.TestCase):
    def test_handle_damage(self):
        state = State()
        state.boss_health = 10

        spell = Spell('spell')
        spell.damage = 3

        handle_damage(spell, state)

        self.assertEqual(7, state.boss_health)


    def test_handle_killing_damage(self):
        state = State()
        state.boss_health = 10

        spell = Spell('spell')
        spell.damage = 11

        handle_damage(spell, state)

        self.assertEqual(-1, state.boss_health)


class TestHandleHeal(unittest.TestCase):
    def test_handle_heal(self):
        state = State()
        state.my_health = 10

        spell = Spell('spell')
        spell.heal = 3

        handle_heal(spell, state)

        self.assertEqual(13, state.my_health)


class TestHandleEffectActivation(unittest.TestCase):
    def test_nothing_activated(self):
        state = State()
        spell = Spell('spell')

        self.assertTrue(handle_effect_activation(spell, state))

        self.assertEqual(0, state.poison_effect_ticks)
        self.assertEqual(0, state.poison_effect_damage)
        self.assertEqual(0, state.shield_effect_ticks)
        self.assertEqual(0, state.shield_effect_armour)
        self.assertEqual(0, state.recharge_effect_ticks)
        self.assertEqual(0, state.recharge_effect_mana)


    def test_poison_activated(self):
        state = State()

        spell = Spell('spell')
        spell.poison_effect_damage = 5
        spell.poison_effect_ticks = 3

        self.assertTrue(handle_effect_activation(spell, state))

        self.assertEqual(3, state.poison_effect_ticks)
        self.assertEqual(5, state.poison_effect_damage)
        self.assertEqual(0, state.shield_effect_ticks)
        self.assertEqual(0, state.shield_effect_armour)
        self.assertEqual(0, state.recharge_effect_ticks)
        self.assertEqual(0, state.recharge_effect_mana)


    def test_poison_already_activated(self):
        state = State()
        state.poison_effect_damage = 1
        state.poison_effect_ticks = 1

        spell = Spell('spell')
        spell.poison_effect_damage = 5
        spell.poison_effect_ticks = 3

        self.assertFalse(handle_effect_activation(spell, state))

        self.assertEqual(1, state.poison_effect_ticks)
        self.assertEqual(1, state.poison_effect_damage)
        self.assertEqual(0, state.shield_effect_ticks)
        self.assertEqual(0, state.shield_effect_armour)
        self.assertEqual(0, state.recharge_effect_ticks)
        self.assertEqual(0, state.recharge_effect_mana)


    def test_recharge_activated(self):
        state = State()

        spell = Spell('spell')
        spell.recharge_effect_mana = 5
        spell.recharge_effect_ticks = 3

        self.assertTrue(handle_effect_activation(spell, state))

        self.assertEqual(0, state.poison_effect_ticks)
        self.assertEqual(0, state.poison_effect_damage)
        self.assertEqual(0, state.shield_effect_ticks)
        self.assertEqual(0, state.shield_effect_armour)
        self.assertEqual(3, state.recharge_effect_ticks)
        self.assertEqual(5, state.recharge_effect_mana)


    def test_recharge_already_activated(self):
        state = State()
        state.recharge_effect_mana = 1
        state.recharge_effect_ticks = 1

        spell = Spell('spell')
        spell.recharge_effect_mana = 5
        spell.recharge_effect_ticks = 3

        self.assertFalse(handle_effect_activation(spell, state))

        self.assertEqual(0, state.poison_effect_ticks)
        self.assertEqual(0, state.poison_effect_damage)
        self.assertEqual(0, state.shield_effect_ticks)
        self.assertEqual(0, state.shield_effect_armour)
        self.assertEqual(1, state.recharge_effect_ticks)
        self.assertEqual(1, state.recharge_effect_mana)


    def test_shield_activated(self):
        state = State()

        spell = Spell('spell')
        spell.shield_effect_armour = 5
        spell.shield_effect_ticks = 3

        self.assertTrue(handle_effect_activation(spell, state))

        self.assertEqual(0, state.poison_effect_ticks)
        self.assertEqual(0, state.poison_effect_damage)
        self.assertEqual(3, state.shield_effect_ticks)
        self.assertEqual(5, state.shield_effect_armour)
        self.assertEqual(0, state.recharge_effect_ticks)
        self.assertEqual(0, state.recharge_effect_mana)


    def test_shield_already_activated(self):
        state = State()
        state.shield_effect_armour = 1
        state.shield_effect_ticks = 1

        spell = Spell('spell')
        spell.shield_effect_armour = 5
        spell.shield_effect_ticks = 3

        self.assertFalse(handle_effect_activation(spell, state))

        self.assertEqual(0, state.poison_effect_ticks)
        self.assertEqual(0, state.poison_effect_damage)
        self.assertEqual(1, state.shield_effect_ticks)
        self.assertEqual(1, state.shield_effect_armour)
        self.assertEqual(0, state.recharge_effect_ticks)
        self.assertEqual(0, state.recharge_effect_mana)

if __name__ == '__main__':
    unittest.main()
