#Matt Person
#Rosalind Problem: NWCK
#source
'''Given: A collection of n trees (n≤40) in Newick format, with each tree containing at most 200 nodes;
each tree Tk is followed by a pair of nodes xk and yk in Tk.
Return: A collection of n positive integers, for which the kth integer represents the distance between xk and yk in Tk.'''

#Note: Might go back and use rosalind utilities Newick tree for this...
import sys
sys.path.insert(0,'C:\\Users\\Matthew\\Desktop\\Python Projects\\Rosalind\\')

from RUtils.src.RosalindUtilities import RosalindUtilities


class NWCK:
    def __init__(self, Tk, xk, yk):
        self.nwck_tree_string = Tk

        self.edges = {}
        self.current_internal_node_number = 0
        self.index_of_tree_string = 0

        self.load_all_edges()
        self.distance_between_nodes = self.get_distance_between_nodes(xk,yk)

    def load_all_edges(self):
        next_token = self.get_next_token()
        while next_token != ';':
            if next_token == '(':
                self.load_edges()
                next_token = self.get_next_token()

    def get_next_token(self):
        start_pos = self.index_of_tree_string
        if start_pos >= len(self.nwck_tree_string):
            return ''
        end_pos = start_pos + 1
        if self.is_special(self.nwck_tree_string[start_pos]):
            self.index_of_tree_string = end_pos
            return self.nwck_tree_string[start_pos]
        while not self.is_special(self.nwck_tree_string[end_pos]):
                end_pos +=1
        self.index_of_tree_string = end_pos
        return ''.join([self.nwck_tree_string[i] for i in range(start_pos, end_pos)])

    def __get_next_internal_node_number(self):
        self.current_internal_node_number += 1
        return self.current_internal_node_number

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
        if self.is_special(next_token):
            node = self.__get_next_internal_node_number()
            self.index_of_tree_string -= 1
        else:
            node = next_token
        self.add_edges(nodes_at_level,node)
        return node

    def add_edges(self,nodes,root_node):
        for node in nodes:
            self.edges[node] = self.edges.get(node,[]) + [root_node]
            self.edges[root_node] = self.edges.get(root_node, []) + [node]

    def get_distance_between_nodes(self,node_a,node_b):
        #BFS of edges
        queue = [(node_a,0)]
        visited = set()

        while len(queue) > 0:
            node = queue.pop()
            visited.add(node[0])
            if node[0] == node_b:
                return node[1]
            for adjacent_node in self.edges[node[0]]:
                if adjacent_node not in visited:
                    queue.insert(0,(adjacent_node,node[1]+1))
        return -1


    def is_special(self, character):
        return character in '(),;'


def Main():
    result = []
    with open('input.txt') as input_data:
        lines = input_data.readlines()
        for i in range(0,len(lines)//3,+3):
            start_node,end_node = lines[i+1].split()
            nwck = NWCK(lines[i],start_node,end_node)
            result.append(nwck.distance_between_nodes)
    print(*result)

if __name__ == '__main__':
    Main()