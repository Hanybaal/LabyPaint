from grille import *

class GameGrid(Grille):
    def __init__(self):
        super().__init__()
        self.metaData = {}


    def crea_grille(self, fichier):
        self.grille = []
        g = self.getGrille()
        i, j = -1, -1
        for ligne in fichier:
            i += 1
            j = -1
            g.append([])
            rligne = ligne.split(',')
            for car in rligne:
                j += 1
                if car != '\n':
                    etat = int(car)
                    if (etat == 0):
                        etat += self.randomWall()
                    g[-1].append(GameCell((j, i), etat))

        for l in range(len(g)):
            for c in range(len(g[l])):
                g[l][c].voisins = g[l][c].getSides(self.getGrille())

    def creaMetaData(self, fichier):
        for ligne in fichier:
            cleValeur = ligne.split("-->")
            self.metaData[cleValeur[0]] = cleValeur[1]



    ##Fonctions booléennes
    def noFreeCase(self):
        for ligne in self.getGrille():
            for cel in ligne:
                if (cel.estPeinte()):
                    return False                
        return True


    def randomWall(self):
        alea = randint(0, 100)
        if alea <= 50:
            return 0

        if alea <= 85:
            return -1

        return -2

    def isBloqued(self, coords):
        return (self.sortie(coords) or not (self.getCellule(coords).estLibre()))

    ##Fonctions get propres à la GameGrid
    def getOrigineCell(self):
        return self.getCellule(list(map(int, self.metaData["depart"].split(','))))

    def getName(self):
        return self.metaData["nom"]

    def getOptimalNbSteps(self):
        return self.metaData["nco"]

    def nbCasesLibres(self):
        n = 0
        for ligne in self.getGrille():
            for cel in ligne:
                if (cel.estPeinte()):
                    n += 1
        return n
    

class GameCell(Cellule):
    def __init__(self, coords, etat):
        super().__init__(coords)
        self.etat = etat
        self.visitee = False


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
        self.changeEtat(2)

    def getInformations(self, grille):
        infos = ["0", "0", "0", "0"]
        voisins = self.getVoisins(grille)
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
