#Matt Person
#Rosalind Problem: NWCK
#unit tests

import unittest

from ..NWCK import NWCK

class TestNWCK(unittest.TestCase):
    def setUp(self):
        NWCK_tree = '(C,D,(A,B));'
        node_a = 'C'
        node_b = 'A'
        self.nwck = NWCK(NWCK_tree,node_a,node_b)
        NWCK_tree_2 = '(cat)dog;'
        node_a = 'dog'
        node_b = 'cat'
        self.nwck_2 = NWCK(NWCK_tree_2,node_a,node_b)
        NWCK_tree_3 = '((A,B),C,D);'
        node_a = 'C'
        node_b = 'A'
        self.nwck_3 = NWCK(NWCK_tree_3,node_a,node_b)

    def test_get_next_internal_node_number(self):
        current_internal_node_number = self.nwck.current_internal_node_number
        self.assertEqual(self.nwck._NWCK__get_next_internal_node_number(), current_internal_node_number + 1)

    def test_get_difference_between_nodes(self):
        self.assertEqual(self.nwck.distance_between_nodes, 3)
        self.assertEqual(self.nwck_2.distance_between_nodes,1)
        self.assertEqual(self.nwck_3.distance_between_nodes, 3)

    def test_is_special_character(self):
        self.assertTrue(self.nwck.__is_special(')'))
        self.assertFalse(self.nwck.__is_special('apple'))