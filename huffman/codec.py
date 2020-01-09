import numpy as np
class Node : 
	
    def __init__(self, label = None, right_nb = None, left_nb = None, cardi = 0, linked = True) :
        self.right_nb = right_nb
        self.left_nb  = left_nb
        self.label = label
        self.cardi = cardi
        self.linked = linked
    def __eq__(self, node2):
        return self.label == node2.label
    @property 
    def linked(self):
        return self._linked
    @linked.setter
    def linked(self, other):
        if type(other) != bool : 
            raise ValueError('un booleen imbecile')
        self._linked = other 
    def __repr__(self):
        return f"{self.label}, {self.cardi}"
class BinaryTree:
	"""Docstring"""
	def __init__(self, root_node = None, ends = list()):
		self.root = root_node
		self.ends = ends

	def find_way(self, label):
		node = self.root
		way = ''
		while node.label != label:#tant qu'on n'est pas arrivé à label (on va de racine à bout)
			if label in node.right_neigh.label:
				node = node.right_neigh
				way += '1'
			else:
				node = node.left_neigh
				way += '0'
		return way


"""        
sort(L : list, coefs : dict):
    on choisit une adaptation du tri par insertion car les listes 
    ne peuvent pas être très longues (au maximum autant que de lettres 
    de l'alphabet, de nombres, et de ponctuation), la complexité de ce programme a donc peu d'importance
    for i in range(len(L)):
        x = L[i]
        j = i
        while j > 0 and coefs[L[j-1]] > coefs[L[i]] : 
            L[j] = L[j-1] 
            coefs[L[j]] = coefs[L[j-1]]
            j -= 1
            
        L[j] = x

"""    



class TreeBuilder : 
    def __init__(self, text):
        self.text = text
    def tree(self):
        """ truc"""
        text = self.text
        ends = list(set(text)) #il s'agit de la lise de tous les caractères distincts
        def card(character):
            i = 0
            for k in text : 
                if k == character : 
                    i += 1
            return i
        ends.sort(key = card)
        ends.reverse()
        nodeslist = [Node(x, None, None, card(x), False) for x in ends]
        node_ends = np.copy(nodeslist)
        old_card = nodeslist[-1].cardi
        while len(nodeslist[0].label) < len(ends) : 
            j = len(nodeslist) - 1
            print([x.label for x in nodeslist])
            x = nodeslist.pop()
            y = nodeslist.pop()
            nodecardi = x.cardi + y.cardi
            nodelabel = x.label + y.label
            i = len(nodeslist) - 1 
            while i > 0 and nodeslist[i].cardi > nodecardi: 
                i -= 1
            nodeslist.insert(i, Node(nodelabel, x.label, y.label,  nodecardi))
        print(nodeslist)
        return BinaryTree(nodeslist[0],  node_ends)



tb = TreeBuilder('nique ta daronne')
tb.tree()


chaine = "abc"
L = ["x", "y", "z", "a"]
def cle(x):
    return 1 if x == "a" else 0
L.sort(key = cle)
print(L)
