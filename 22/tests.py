from local_lib import *
import unittest

class TestNodeChecked(unittest.TestCase):
    def test_compare_empty_states(self):
        state = State()
        other_state = State()
        spell = Spell('spell')
        other_spell = Spell('other spell')

        self.assertFalse(node_checked(Node(spell, state)))

        self.assertTrue(node_checked(Node(spell, other_state)))

        self.assertFalse(node_checked(Node(other_spell, state)))


    def test_compare_empty_states_with_history(self):
        state = State()
        state.history.append('spell')

        other_state = State()
        other_state.history.append('other spell')

        spell = Spell('spell')

        self.assertFalse(node_checked(Node(spell, state)))

        self.assertTrue(node_checked(Node(spell, other_state)))


    def test_compare_states(self):
        boss_health = 28
        boss_damage = 14
        my_health = 16
        my_mana = 876
        my_armour = 5
        poison_effect_ticks = 3
        poison_effect_damage = 2
        shield_effect_ticks = 1
        shield_effect_armour = 4
        recharge_effect_ticks = 6
        recharge_effect_mana = 9
        mana_spent = 200

        state = State()
        state.boss_health = boss_health
        state.boss_damage = boss_damage
        state.my_health = my_health
        state.my_mana = my_mana
        state.my_armour = my_armour
        state.poison_effect_ticks = poison_effect_ticks
        state.poison_effect_damage = poison_effect_damage
        state.shield_effect_ticks = shield_effect_ticks
        state.shield_effect_armour = shield_effect_armour
        state.recharge_effect_ticks = recharge_effect_ticks
        state.recharge_effect_mana = recharge_effect_mana
        state.mana_spent = mana_spent
        state.history.append('spell')

        other_state = State()
        other_state.boss_health = boss_health
        other_state.boss_damage = boss_damage
        other_state.my_health = my_health
        other_state.my_mana = my_mana
        other_state.my_armour = my_armour
        other_state.poison_effect_ticks = poison_effect_ticks
        other_state.poison_effect_damage = poison_effect_damage
        other_state.shield_effect_ticks = shield_effect_ticks
        other_state.shield_effect_armour = shield_effect_armour
        other_state.recharge_effect_ticks = recharge_effect_ticks
        other_state.recharge_effect_mana = recharge_effect_mana
        other_state.mana_spent = mana_spent
        other_state.history.append('other spell')

        spell = Spell('spell')

        self.assertFalse(node_checked(Node(spell, state)))

        self.assertTrue(node_checked(Node(spell, other_state)))


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


if __name__ == '__main__':
    unittest.main()
