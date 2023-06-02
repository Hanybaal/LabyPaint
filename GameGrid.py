from grille import *

class GameGrid(Grille):
    def __init__(self):
        super().__init__()


    def crea_grille(self, fichier):
        self.grille = []
        g = self.getGrille()
        i, j = -1, -1
        for ligne in fichier:
            i += 1
            j = -1
            g.append([])
            for car in ligne:
                j += 1
                if car != '\n':
                    etat = int(car)
                    if (etat == 0):
                        etat += self.randomMur()
                    g[-1].append(GameCell((j, i), etat))

        for l in range(len(g)):
            for c in range(len(g[l])):
                g[l][c].voisins = g[l][c].calculVoisins(self.getGrille())


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
