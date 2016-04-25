from local_lib import *
import unittest

class TestNodeChecked(unittest.TestCase):
    def test_compare_empty_states(self):
        # Test node_checked
        state = State()
        other_state = State()
        spell = Spell('spell')

        self.assertFalse(node_checked(Node(spell, state)))

        self.assertTrue(node_checked(Node(spell, other_state)))


if __name__ == '__main__':
    unittest.main()
