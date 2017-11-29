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

        self.load_tree()
        self.distance_between_nodes = self.get_distance_between_nodes(xk,yk)

    def load_tree(self):
        next_token = self.__get_next_token()
        while next_token != ';':
            if next_token == '(':
                self.__create_edges_at_level()
                next_token = self.__get_next_token()

    def get_distance_between_nodes(self, node_a, node_b):
        # BFS of edges
        queue = [(node_a, 0)]
        visited = set()

        while len(queue) > 0:
            node = queue.pop()
            visited.add(node[0])
            if node[0] == node_b:
                return node[1]
            for adjacent_node in self.edges[node[0]]:
                if adjacent_node not in visited:
                    queue.insert(0, (adjacent_node, node[1] + 1))
        return -1

    def __get_next_token(self):
        start_pos = self.index_of_tree_string
        end_pos = start_pos + 1

        if start_pos >= len(self.nwck_tree_string):
            return ''

        if self.__is_special(self.nwck_tree_string[start_pos]):
            self.index_of_tree_string = end_pos
            return self.nwck_tree_string[start_pos]

        while not self.__is_special(self.nwck_tree_string[end_pos]):
                end_pos += 1
        self.index_of_tree_string = end_pos

        return  self.nwck_tree_string[start_pos:end_pos]

    def __get_next_internal_node_number(self):
        self.current_internal_node_number += 1
        return self.current_internal_node_number

    def __create_edges_at_level(self):
        nodes_at_level = []
        token = self.__get_next_token()

        while token != ')' and token != ';':
            if token == '(':
                nodes_at_level.append(self.__create_edges_at_level())
            elif token not in '(,':
                nodes_at_level.append(token)
            token = self.__get_next_token()

        token = self.__get_next_token()

        if self.__is_special(token):
            node = self.__get_next_internal_node_number()
            self.index_of_tree_string -= 1
        else:
            node = token

        self.__create_edges_for_root_node(nodes_at_level, node)
        return node

    def __create_edges_for_root_node(self, nodes, root_node):
        for node in nodes:
            self.edges[node] = self.edges.get(node,[]) + [root_node]
            self.edges[root_node] = self.edges.get(root_node, []) + [node]



    def __is_special(self, character):
        return character in '(),;'


def Main():
    result = []
    with open('input.txt') as input_data:
        lines = input_data.readlines()
        for i in range(0,len(lines)//3,+3):
            start_node,end_node = lines[i+1].split()
            nwck = NWCK(lines[i],start_node,end_node)
            #print(nwck.edges)
            result.append(nwck.distance_between_nodes)
    print(*result)
    nwck = NWCK('(C,D,(A,B));','C','B')
    #print(nwck.edges)
    #print(nwck.distance_between_nodes)

if __name__ == '__main__':
    Main()