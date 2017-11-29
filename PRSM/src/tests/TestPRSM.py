import unittest

from ..PRSM import PRSM

class TestPRSM(unittest.TestCase):
    def setUp(self):
        n = 4
        strings = '''GSDMQS
VWICN
IASWMQS
PVSMGAD'''.split('\n')
        R = list(map(float,'''445.17838
115.02694
186.07931
314.13789
317.1198
215.09061'''.split('\n')))
        self.prsm = PRSM(n,strings,R)

    def test_get_multiplicty_of_string(self):
        s = 'IASWMQS'
        self.assertEqual(self.prsm.__get_multiplicity_of_string(s), 3)
        s = 'GSDMQS'
        self.assertEqual(self.prsm.__get_multiplicity_of_string(s), 3)

    def test_get_maximum_multiplicity(self):
        self.assertEqual(self.prsm.max_multiplicity_count,3)
        self.assertEqual(self.prsm.max_multiplicity_string, 'GSDMQS')