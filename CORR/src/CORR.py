#Matt Person
#Rosalind Problem: CORR
#source
'''Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read ss in the dataset, one of the following applies:
s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)'''

import sys
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities

class CORR():
    def __init__(self,file):
        self.ru = RosalindUtilities()
        self.reads = [value[1] for value in self.ru.read_input_file(file)]
        self.reads_count = {}
        self.load_reads_by_count_with_rev_comp()
        self.corrected_reads = self.get_corrected_reads()

    def __str__(self):
        return '\n'.join([correction[0] + '->' + correction[1] for correction in self.corrected_reads])

    def load_reads_by_count_with_rev_comp(self):
        for read in self.reads:
            if read in self.reads_count:
                self.reads_count[read] = self.reads_count[read] + 1
            else:
                rev_comp = self.ru.get_reverse_complement(read)
                if rev_comp in self.reads_count:
                    self.reads_count[rev_comp] = self.reads_count[rev_comp] + 1
                else:
                    self.reads_count[read] = 1

    def get_reads_with_one_count(self):
        return [read for read in self.reads_count if self.reads_count[read] == 1]

    def is_hamming_distance_one(self,a,b):
        if len(a) != len(b):
            return False
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
            if diff > 1:
                return False
        return diff == 1

    def get_hamming_distance_one_read(self,read):
        for read_to_check in self.reads_count:
            if self.reads_count[read_to_check] != 1:
                if self.is_hamming_distance_one(read,read_to_check):
                    return read_to_check
                rev_comp = self.ru.get_reverse_complement(read_to_check)
                if self.is_hamming_distance_one(read,rev_comp):
                    return rev_comp

    def get_corrected_reads(self):
        return [(read,self.get_hamming_distance_one_read(read)) for read in self.get_reads_with_one_count()]

def Main():
    solver = CORR('sample.txt')
    print(solver)

if __name__ == '__main__':
    Main()