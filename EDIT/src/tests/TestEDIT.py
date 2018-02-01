import unittest

from ..EDIT import EDIT

class TestEDIT(unittest.TestCase):
    def setUp(self):
        a = 'MEANLY'
        b = 'PLEASANTLY'
        self.edit = EDIT(a,b)

    def test_get_edit_distance(self):
        self.assertEqual(self.edit.answer, 5)