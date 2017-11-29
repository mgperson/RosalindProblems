import os
import sys,difflib
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities
from collections import Counter

class PRSM():
    def __init__(self,n,strings,R):
        self.n = n
        self.strings = strings
        self.R = R

        self.ru = RosalindUtilities()
        self.max_multiplicity_count, self.max_multiplicity_string = self.get_max_multiplicity_string()

    def __str__(self):
        return str(self.max_multiplicity_count) + '\n' + self.max_multiplicity_string

    def get_max_multiplicity_string(self):
        max_multiplicity = 0
        max_multiplicity_string = ''

        for string in self.strings:
            multiplicity = self.__get_multiplicity_of_string(string)
            if multiplicity > max_multiplicity:
                max_multiplicity = multiplicity
                max_multiplicity_string = string

        return (max_multiplicity,max_multiplicity_string)

    def __get_multiplicity_of_string(self, s):
        mink_diff = []
        weights = self.__get_weights_of_prefixes_and_suffixes(s)

        for weight in weights:
            for r_value in self.R:
                mink_diff.append(round(r_value - weight,4))

        return Counter(mink_diff).most_common(1)[0][1]

    def __get_weights_of_prefixes_and_suffixes(self, s):
        weights = []

        for i in range(0,len(s)):
            prefix = s[:i]
            suffix = s[i:]
            prefix_weight = sum([self.ru.monoisotropic_mass_by_aa_code[aa] for aa in prefix])
            suffix_weight = sum([self.ru.monoisotropic_mass_by_aa_code[aa] for aa in suffix])
            weights.append(prefix_weight)
            weights.append(suffix_weight)

        return weights




def Main():
    with open('input.txt') as input_data:
        lines = input_data.readlines()

        n = int(lines[0])
        strings = [line.strip('\n') for line in lines[1:n+1]]
        R = list(map(float,[line.strip('\n') for line in lines[n+1:]]))

        prsm = PRSM(n,strings,R)
        print(prsm)

if __name__ == '__main__':
    Main()