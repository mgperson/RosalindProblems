import unittest

from ..RosalindUtilities import RosalindUtilities

class TestRosalindUtilities(unittest.TestCase):
    def setUp(self):
        self.utilities = RosalindUtilities()
        self.utilities.load_amino_acid_codes_for_codons()

    def test_get_amino_acid_code_for_codon(self):
        self.assertEqual(self.utilities.get_amino_acid_code_for_codon('UUC'),'F')
        self.assertEqual(self.utilities.get_amino_acid_code_for_codon('AAA'), 'K')
        self.assertIsNone(self.utilities.get_amino_acid_code_for_codon('TRE'))