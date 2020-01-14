import numpy as np 
from colorama import Fore, Style

from needleman_wunsch_py import Ruler, alphabet
import sys
""" si on a créé un fichier .py pour pouvoir importer needleman, c'est uniquement pour pouvoir importer les objets de ce
programme (ca ne fonctionnait pas sous forme ipynb)"""
with open(sys.argv[1], 'r') as monfichier : 
    contenu = monfichier.read()
    exemples = contenu.split('\n')
    exemples.remove('') #là, exemples est une liste contenant toutes les chaines de caractère
    for i in range(len(exemples)//2):
        ruler = Ruler(exemples[2 * i], exemples[2 * i + 1])
        ruler.compute()
        (top, bottom) = ruler.report()
        print(f"====== example # {i+1} - distance = {ruler.distance} \n {top} \n {bottom}")
        
