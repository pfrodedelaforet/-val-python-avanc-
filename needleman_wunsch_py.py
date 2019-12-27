import numpy as np

from colorama import Fore, Style
alphabet = {'a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'q', 's',
                'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'w', 'x', 'c', 'v', 'b', 'n'}
class Ruler:
    
    defaultmat = {lettre2: {lettre: 1 for lettre in alphabet}
                         for lettre2 in alphabet}
    for lettre in defaultmat.keys():
        defaultmat[lettre][lettre] = 0
        
    def __init__(self, chaine1: str, chaine2: str, d = 1, M = defaultmat):
        self.size = max(len(chaine1), len(chaine2))
        self.M = M
        self.d = d
        self.chaine1 = chaine1
        self.chaine2 = chaine2
        self.dist = None

    def compute(self):
        """"ici le calcul de distance que
        l'utilisateur doit explicitement lancer"""
        chaine1 = self.chaine1.lower()
        chaine2 = self.chaine2.lower() # on considère la différence entre majuscule et minuscule négligeable
        d = self.d
        F = np.array([[None for j in range(len(chaine2)+1)]for i in range(len(chaine1)+1)])  # le +1 sert à caser les pénalités initiales de trou en 0
        for i in range(len(chaine1) + 1):
            F[i, 0] = self.d * i
        for j in range(len(chaine2) + 1):
            F[0, j] = self.d * j
        for n in range(2, len(chaine1) + len(chaine2) + 1):  # n correspond à la valeur de i+j
            for i in range(1, min(len(chaine1)+1, n)):  # attention, à cause des cases précédentes, i va de 1 à n-1 et j aussi
                j = n - i
                if (j <= len(chaine2)):  # cas classique où on peut utiliser la matrice de passage
                    trouchaine1 = F[i, j-1] + d
                    trouchaine2 = F[i-1, j] + d
                    pastrou = F[i-1, j-1] + self.M[chaine1[i-1]][chaine2[j-1]]  # en réalité, il s'agit du passage de i à j, mais ceux-ci sont décalés
                    F[i, j] = min(trouchaine1, trouchaine2, pastrou)
        self.F = F
        self.dist = F[len(chaine1), len(chaine2)]

    def report(self):
        chaine1 = self.chaine1.lower()
        chaine2 = self.chaine2.lower()
        d = self.d
        i = len(chaine1)
        j = len(chaine2)
        newc1 = ""
        newc2 = ""
        egal = "="
        while i > 1 and j > 1:
            if self.F[i, j] == self.F[i-1, j-1] + self.M[chaine1[i-1]][chaine2[j-1]]:
                if chaine1[i-1] != chaine2[j-1] : 
                    newc1 = f"{Fore.RED}{chaine1[i-1]}{Style.RESET_ALL}" + newc1
                    newc2 = f"{Fore.RED}{chaine2[j-1]}{Style.RESET_ALL}" + newc2
                else : 
                    newc1 = chaine1[i-1] + newc1
                    newc2 = chaine2[j-1] + newc2
                i = i-1
                j = j-1
                continue
            if self.F[i, j] == self.F[i-1, j] + d:# on est forcément sur une lettre différente ou un espace
                newc1 = chaine1[i-1] + newc1
                newc2 = f"{Fore.RED}{egal}{Style.RESET_ALL}" + newc2
                i -= 1
            else:
                newc2 = chaine2[j-1] + newc2
                newc1 = f"{Fore.RED}{egal}{Style.RESET_ALL}" + newc1
                j -= 1
        if (i == 1 and j == 1):  # cas particulier à traiter : si la première lettre est identique
            if chaine1[i-1] != chaine2[j-1] : 
                    newc1 = f"{Fore.RED}{chaine1[i-1]}{Style.RESET_ALL}" + newc1
                    newc2 = f"{Fore.RED}{chaine2[j-1]}{Style.RESET_ALL}" + newc2
            else : 
                newc1 = chaine1[i-1] + newc1
                newc2 = chaine2[j-1] + newc2
            return (newc1, newc2)
        while j >= 1:
            newc2 = chaine2[j-1] + newc2
            newc1 = f"{Fore.RED}{egal}{Style.RESET_ALL}" + newc1
            j -= 1
        while i >= 1:
            newc1 = chaine1[i-1] + newc1
            newc2 = f"{Fore.RED}{egal}{Style.RESET_ALL}" + newc2
            i -= 1
        return (newc1, newc2)
    @property
    def distance(self):
        return self.dist

    @property
    def chaine1(self):
        return self._chaine1

    @chaine1.setter
    def chaine1(self, c1: str):
        self._chaine1 = c1

    @property
    def chaine2(self):
        return self._chaine2

    @chaine2.setter
    def chaine2(self, c2: str):
        self._chaine2 = c2

    @property
    def F(self):
        return self._F

    @F.setter
    def F(self, M):
        self._F = M

