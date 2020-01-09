import numpy as np 
from colorama import Fore, Style

from needleman_wunsch_py import Ruler, alphabet
import sys
with open(sys.argv[1], 'r') as monfichier : 
    contenu = monfichier.read()
    exemples = contenu.split('\n')
    exemples.remove('')
    for i in range(len(exemples)//2):
        ruler = Ruler(exemples[2 * i], exemples[2 * i + 1])
        ruler.compute()
        (top, bottom) = ruler.report()
        print(f"====== example # {i+1} - distance = {ruler.distance} \n {top} \n {bottom}")
        
