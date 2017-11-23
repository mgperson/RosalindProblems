import urllib.request

class RosalindUtilities():
    def __init__(self):
        self.amino_acid_codes_for_codons = {}
        self.load_amino_acid_codes_for_codons()
        self.codons_for_amino_acid_codes = {}
        self.load_codons_for_amino_acid_codes()
        self.monoisotropic_mass_by_aa_code = {}
        self.aa_code_by_monoisotropic_mass = {}
        self.load_monoisotropic_masses()
        self.Newick_edges = {}
        self.GUID = 0

    def is_special_character(self,char):
        return char in '(),;'

    def get_GUID(self):
        self.GUID += 1
        return self.GUID

    def get_next_token(self):
        start_pos = self.i
        if start_pos >= len(self.nwck_tree):
            return ''
        end_pos = start_pos + 1
        if self.is_special_character(self.nwck_tree[start_pos]):
            self.i = end_pos
            return self.nwck_tree[start_pos]
        while not self.is_special_character(self.nwck_tree[end_pos]):
                end_pos +=1
        self.i = end_pos
        return ''.join([self.nwck_tree[i] for i in range(start_pos,end_pos)])

    def load_edges_of_newick_tree(self,newick_tree):
        self.i = 0
        self.nwck_tree = newick_tree
        self.load_edges()

    def load_edges(self):
        nodes_at_level = []
        next_token = self.get_next_token()
        while next_token != ')' and next_token != ';':
            if next_token == '(':
                nodes_at_level.append(self.load_edges())
            elif next_token not in '(,':
                nodes_at_level.append(next_token)
            next_token = self.get_next_token()
        next_token = self.get_next_token()
        root_node_weight = ''
        if self.is_special_character(next_token.split(':')[0]):
            next_token_values = next_token.split(':')
            node = str(self.get_GUID())
            if len(next_token_values) > 1:
                root_node_weight = ':' + next_token_values[1]
            else:
                self.i -= 1
        else:
            node = next_token
        #print(node)
        self.add_edges(nodes_at_level,node)
        return node + root_node_weight

    def add_edges(self,nodes,root_node):
        for node in nodes:
            node_values = node.split(':')
            node_name = node_values[0]
            edge_weight = int(node_values[1]) if len(node_values) > 1 else 1
            #self.edges[node_name] = self.edges.get(node_name,[]) + [root_node]
            #self.edges[root_node] = self.edges.get(root_node, []) + [node_name]
            self.Newick_edges[node_name] = self.Newick_edges.get(node_name, []) + [(root_node,edge_weight)]
            self.Newick_edges[root_node] = self.Newick_edges.get(root_node, []) + [(node_name,edge_weight)]

    def load_monoisotropic_masses(self):
        values = [('A',71.03711),('C',103.00919),('D',115.02694),('E',129.04259),('F',147.06841),
                  ('G',57.02146),('H',137.05891),('I',113.08406),('K',128.09496),('L',113.08406),
                  ('M',131.04049),('N',114.04293),('P',97.05276),('Q',128.05858),('R',156.10111),
                  ('S',87.03203),('T',101.04768),('V',99.06841),('W',186.07931),('Y',163.06333) ]
        for val in values:
            self.monoisotropic_mass_by_aa_code[val[0]] = val[1]
            self.aa_code_by_monoisotropic_mass[round(val[1],4)] = val[0]

    def load_codons_for_amino_acid_codes(self):
        values = [('I',('ATT', 'ATC', 'ATA')),('L',('CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG')),
                  ('V',('GTT', 'GTC', 'GTA', 'GTG')), ('F',('TTT', 'TTC')), ('M',('ATG',)),
                  ('C',('TGT', 'TGC')),('A',('GCT', 'GCC', 'GCA', 'GCG')),('G',('GGT', 'GGC', 'GGA', 'GGG')),
                  ('P', ('CCT', 'CCC', 'CCA', 'CCG')), ('T', ('ACT', 'ACC', 'ACA', 'ACG')), ('S', ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC')),
                  ('Y', ('TAT', 'TAC')), ('W', ('TGG',)),('Q', ('CAA', 'CAG')),
                  ('N', ('AAT', 'AAC')), ('H', ('CAT','CAC')), ('E', ('GAA', 'GAG')),
                  ('D', ('GAT', 'GAC')), ('K', ('AAA', 'AAG')), ('R', ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG')),
                  ('Stop',('TAA', 'TAG', 'TGA'))]

        for val in values:
            self.codons_for_amino_acid_codes[val[0]] = val[1]

    def load_amino_acid_codes_for_codons(self):
        values = [('UUU', 'F'), ('UUC', 'F'),('UUA', 'L'), ('UUG', 'L'),
                  ('UCU', 'S'), ('UCC', 'S'), ('UCA', 'S'), ('UCG', 'S'),
                  ('UAU', 'Y'), ('UAC', 'Y'), ('UAA', 'Stop'), ('UAG', 'Stop'),
                  ('UGU', 'C'), ('UGC', 'C'), ('UGA', 'Stop'), ('UGG', 'W'),

                  ('CUU', 'L'), ('CUC', 'L'), ('CUA', 'L'), ('CUG', 'L'),
                  ('CCU', 'P'), ('CCC', 'P'), ('CCA', 'P'), ('CCG', 'P'),
                  ('CAU', 'H'), ('CAC', 'H'), ('CAA', 'Q'), ('CAG', 'Q'),
                  ('CGU', 'R'), ('CGC', 'R'), ('CGA', 'R'), ('CGG', 'R'),

                  ('AUU', 'I'), ('AUC', 'I'), ('AUA', 'I'), ('AUG', 'M'),
                  ('ACU', 'T'), ('ACC', 'T'), ('ACA', 'T'), ('ACG', 'T'),
                  ('AAU', 'N'), ('AAC', 'N'), ('AAA', 'K'), ('AAG', 'K'),
                  ('AGU', 'S'), ('AGC', 'S'), ('AGA', 'R'), ('AGG', 'R'),

                  ('GUU', 'V'), ('GUC', 'V'), ('GUA', 'V'), ('GUG', 'V'),
                  ('GCU', 'A'), ('GCC', 'A'), ('GCA', 'A'), ('GCG', 'A'),
                  ('GAU', 'D'), ('GAC', 'D'), ('GAA', 'E'), ('GAG', 'E'),
                  ('GGU', 'G'), ('GGC', 'G'), ('GGA', 'G'), ('GGG', 'G')]

        for val in values:
            self.amino_acid_codes_for_codons[val[0]] = val[1]

    #returns -1 if aa not found
    def get_aa_by_monoisotopic_mass(self,monoisotopic_mass):
        if round(monoisotopic_mass,4) not in self.aa_code_by_monoisotropic_mass.keys():
            return '-1'
        return self.aa_code_by_monoisotropic_mass[round(monoisotopic_mass,4)]

    def swap_two_chars_in_string(self,inputString,charOne,charTwo):
        # X used as temp placer
        inputString = inputString.replace(charOne, 'X')
        inputString = inputString.replace(charTwo, charOne)
        inputString = inputString.replace('X',charTwo)
        return inputString

    def get_reverse_complement(self, inputString):
        return self.get_complement(inputString[::-1])

    def get_RNA_equiv_of_DNA(self,inputString):
        '''Used to swap T of DNA with U ONLY'''
        return inputString.replace('T','U')

    def get_aa_from_DNA_codon(self,DNACodon):
        RNA_equiv = self.get_RNA_equiv_of_DNA(DNACodon)
        #return self.amino_acid_codes_for_codons.get(RNA_equiv) if RNA_equiv in self.amino_acid_codes_for_codons else 'a'
        return self.amino_acid_codes_for_codons.get(self.get_RNA_equiv_of_DNA(DNACodon))

    def get_complement(self,inputString):
        inputString = self.swap_two_chars_in_string(inputString,'A','T')
        inputString = self.swap_two_chars_in_string(inputString, 'C', 'G')
        return inputString

    def get_amino_acid_code_for_codon(self,codon):
        return self.amino_acid_codes_for_codons.get(codon)

    def read_input_file(self,file):
        values = []
        with open(file) as input_data:
            current_line = ''
            label = ''
            for line in input_data:
                if line[0] == '>':
                    if not current_line == '':
                        values.append((label,current_line))
                    label = line[1:].rstrip('\n')
                    current_line = ''
                else:
                    current_line += line.rstrip('\n')
            values.append((label,current_line))
        return values

    def get_from_url(self,url):
        result = urllib.request.urlopen(url)
        return result.read()

