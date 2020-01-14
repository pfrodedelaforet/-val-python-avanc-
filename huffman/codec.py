import numpy as np
class Node : 
    """ on créé la classe Node, qu'on utilisera ensuite recursivement pour créer la classe BinaryTree"""
    def __init__(self, label = None, right_nb = None, left_nb = None, cardi = 0) :
        self.right_nb = right_nb
        self.left_nb  = left_nb
        self.label = label
        self.cardi = cardi
    def __eq__(self, node2):
        return self.label == node2.label
    def __repr__(self):
        return f"{self.label}, {self.cardi}"
class BinaryTree:
    """Cette classe BinaryTree permettra de créer l'arbre qui codera le message
     uniquement en mettant en entrée le noeud racine et les noeuds de bout, et de pouvoir
     coder en binaire un chemin entre deux noeuds"""
    def __init__(self, root_node = None, ends = list()):
        self.root = root_node
        self.ends = ends
    
    def find_way(self, label):
        node = self.root
        way = ''
        while node.label != label:#tant qu'on n'est pas arrivé à label (on va de racine à bout)
            if label in node.right_nb.label:
                node = node.right_nb
                way += '1'
            else:
                node = node.left_nb
                way += '0'
        return way                
    def find_char(self, bincode):
        node = self.root
        for x in bincode : 
            if x == '1' : 
                node = node.right_nb
            if x == '0' : 
                node = node.left_nb
        return node.label


class TreeBuilder : 
    def __init__(self, text):
        self.text = text
    def tree(self):
        """ l'idée ici, c'est de partir des noeuds du bout, qui sont les caractères isolés,
        d'initier une liste de ces noeuds, rangés par cardinal décroissant, et de les fusionner 2 à 2
        par ordre croissant de cardinal. On garde ainsi à chaque itération une liste triée des noeuds qu'il reste
        à fusionner, et on s'arête lorsqu'il ne reste qu'un noeud"""
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
        nodeslist = [Node(x, None, None, card(x)) for x in ends]
        node_ends = np.copy(nodeslist)
        while len(nodeslist) > 1 : 
            print([x.label for x in nodeslist])
            x = nodeslist.pop()
            y = nodeslist.pop()
            nodecardi = x.cardi + y.cardi
            nodelabel = x.label + y.label
            i = len(nodeslist) - 1 
            while i > 0 and nodeslist[i].cardi > nodecardi: 
                i -= 1
            nodeslist.insert(i, Node(nodelabel, x, y,  nodecardi))
        print(nodeslist)
        return BinaryTree(nodeslist[0],  node_ends)

class Codec : 
    def __init__(self, tree : BinaryTree):
        self.tree = tree 
    def encode(self, text) : 
        arbre = self.tree
        binarychain = ''
        for s in text : 
            binarychain += arbre.find_way(s)
        return binarychain
    def decode(self, encoded):
        chaine = ''
        arbre = self.tree
        bin_provis = ''
        for x in encoded : 
            bin_provis += x
            char = arbre.find_char(bin_provis)
            if len(char) == 1 :
                chaine += char
                bin_provis = ''
        return chaine

texte = "a dead dad ceded a bad babe a beaded abaca bed"           
builder = TreeBuilder("a dead dad ceded a bad babe a beaded abaca bed")
tr = builder.tree()
codec = Codec(tr)
print(codec.encode("a dead dad ceded a bad babe a beaded abaca bed"))
print(codec.decode(codec.encode("a dead dad ceded a bad babe a beaded abaca bed")))
decoded = codec.decode(codec.encode("a dead dad ceded a bad babe a beaded abaca bed"))
print(texte == decoded)
