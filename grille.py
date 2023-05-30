from random import randint

class Grille():
    def __init__(self):
        self.grille = []
        self.taille = 0

    def __repr__(self):
        for ligne in self.getGrille():
            print(ligne)
        return ""

    def crea_grille(self, fichier):
        self.grille = []
        i, j = -1, -1
        for ligne in fichier:
            i += 1
            j = -1
            self.grille.append([])
            for car in ligne:
                j += 1
                if car != '\n':
                    etat = int(car)
                    if (etat == 0):
                        etat += self.randomMur()
                    self.grille[-1].append(Cellule(etat, (j, i)))

        for l in range(len(self.grille)):
            for c in range(len(self.grille[l])):
                self.grille[l][c].voisins = self.grille[l][c].calculVoisins(self.grille)
        self.setTaille(len(self.getGrille()))

    def randomMur(self):
        alea = randint(0, 100)
        if alea <= 50:
            return 0

        if alea <= 85:
            return -1

        return -2
    
    def pasDeCaseLibre(self):
        for ligne in self.getGrille():
            for cel in ligne:
                if (cel.estPeinte()):
                    return False                
        return True

    def nbCasesLibres(self):
        n = 0
        for ligne in self.getGrille():
            for cel in ligne:
                if (cel.estPeinte()):
                    n += 1
        return n

    def getGrille(self):
        return self.grille

    def getCellule(self, coords):
        return (self.getGrille()[coords[1]][coords[0]])

    def getTaille(self):
        return self.taille

    def setTaille(self, t):
        self.taille = t

    def sortie(self, coords):
        return (coords[0] >= self.getTaille()
                or coords[0] < 0
                or coords[1] >= self.getTaille()
                or coords[1] < 0)
    
    def blocage(self, coords):
        return (self.sortie(coords) or not (self.getCellule(coords).estLibre()))


class Cellule():
    def __init__(self, etat, coords):
        self.etat = etat
        self.x = coords[0]
        self.y = coords[1]
        self.voisins = []
        self.joueur = None
        self.visitee = False

    def __repr__(self):
        return str((self.getEtat(), (self.getX(), self.getY())))

    def getEtat(self):
        return self.etat

    def changeEtat(self, valeur):
        self.etat = valeur

    def estUnMur(self):
        return (self.getEtat() <= 0)

    def estLibre(self):
        return (not self.estUnMur())

    def estPeinte(self):
        return (self.getEtat() == 1)

    def passage(self, difficile = False):
        self.visitee = True
        if not difficile:
            self.changeEtat(2)

        else:
            self.changeEtat(0)


    def getInformations(self):
        infos = ["0", "0", "0", "0"]
        voisins = self.voisins
        for v in range(len(voisins)):
            c = voisins[v]
            if self.cIsPlusBas(c):
                if c.estLibre():
                    infos[0] = "2"

                else:
                    infos[0] = "1"

            elif self.cIsPlusGauche(c):
                if c.estLibre():
                    infos[1] = "2"

                else:
                    infos[1] = "1"

            elif self.cIsPlusHaut(c):
                if c.estLibre():
                    infos[2] = "2"

                else:
                    infos[2] = "1"

            elif self.cIsPlusDroite(c):
                if c.estLibre():
                    infos[3] = "2"

                else:
                    infos[3] = "1"

        return infos
            

    def calculVoisins(self, grille):
        #Haut - Droite - Bas - Gauche
        v = []

        if self.getY() > 0:
            v.append(grille[self.getY() - 1][self.getX()])


        if self.getX() < len(grille[0]) - 1:
            v.append(grille[self.getY()][self.getX() + 1])


        if self.getY() < len(grille) - 1:
            v.append(grille[self.getY() + 1][self.getX()])


        if self.getX() > 0:
            v.append(grille[self.getY()][self.getX() - 1])

        return v

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getVoisins(self):
        return self.voisins


    def cIsPlusBas(self, cellule):
        return (self.getY() > cellule.getY())

    def cIsPlusHaut(self, cellule):
        return (self.getY() < cellule.getY())

    def cIsPlusGauche(self, cellule):
        return (self.getX() < cellule.getX())

    def cIsPlusDroite(self, cellule):
        return (self.getX() > cellule.getX())


    def estEnHaut(self):
        return (self.getY() == 0)

    def estADroite(self, g):
        return (self.getX() > len(g[0]) - 1)
    
    def estEnHaut(self, g):
        return (self.getY() > len(g) - 1)

    def estEnHaut(self):
        return (self.getX() == 0)
