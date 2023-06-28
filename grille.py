from random import randint

class Grille():
    def __init__(self):
        self.grille = []

    def __repr__(self):
        for ligne in self.getGrille():
            print(ligne)
        return ""

##    def crea_grille(self, fichier):
##        self.grille = []
##        i, j = -1, -1
##        for ligne in fichier:
##            i += 1
##            j = -1
##            self.grille.append([])
##            for car in ligne:
##                j += 1
##                if car != '\n':
##                    etat = int(car)
##                    if (etat == 0):
##                        etat += self.randomWall()
##                    self.grille[-1].append(Cellule(etat, (j, i)))
##
##        for l in range(len(self.grille)):
##            for c in range(len(self.grille[l])):
##                self.grille[l][c].voisins = self.grille[l][c].getSides(self.getGrille())

    
    ##Fonctions get
    def getGrille(self):
        return self.grille

    def getProfundCopyGrille(self):
        return [list(l) for l in self.getGrille()]

    def getCellule(self, coords):
        return (self.getGrille()[coords[1]][coords[0]])

    def getTailleY(self):
        return len(self.getGrille())

    def getTailleX(self):
        return len(self.getGrille()[0])


    def sortie(self, coords):
        return (coords[0] >= self.getTailleY()
                or coords[0] < 0
                or coords[1] >= self.getTailleX()
                or coords[1] < 0)
    

class Cellule():
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]


    def __repr__(self):
        return str((self.getX(), self.getY()))            

    def getSides(self, grille):
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

    def getVoisins(self, grille):
        return self.getSides(grille)


    def moreDown(self, cellule):
        return (self.getY() > cellule.getY())

    def moreUp(self, cellule):
        return (self.getY() < cellule.getY())

    def moreLeft(self, cellule):
        return (self.getX() < cellule.getX())

    def moreRight(self, cellule):
        return (self.getX() > cellule.getX())


    def isTop(self):
        return (self.getY() == 0)

    def isRight(self, g):
        return (self.getX() > len(g[0]) - 1)
    
    def isDown(self, g):
        return (self.getY() > len(g) - 1)

    def isLeft(self):
        return (self.getX() == 0)
