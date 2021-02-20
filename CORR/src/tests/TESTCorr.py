#Matt Person
#Rosalind Problem: CORR
#unit tests

import unittest

from ..CORR import CORR

class TestCORR(unittest.TestCase):
    def setUp(self):
        self.corr = CORR('src\\test.txt')

    def test_get_reads_with_one_count(self):
        print(self.corr.reads_count)
        self.assertEqual(self.corr.get_reads_with_one_count(),['TTCAT','GAGGA','TTTCC'])

    def test_get_hamming_distance_one_read(self):
        self.assertEqual(self.corr.get_hamming_distance_one_read('TTCAT'),'TTGAT')

    def test_is_hamming_distance_one(self):
        a = 'GACT'
        b = 'GCCT'
        self.assertTrue(self.corr.is_hamming_distance_one(a,b))

    def test_get_corrected_reads(self):
        self.assertEqual(self.corr.get_corrected_reads(),[('TTCAT','TTGAT'),
            ('GAGGA','GATGA'), ('TTTCC','TTTCA')])