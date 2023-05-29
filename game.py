from grille import *
from player import *
from graphisme import *

class Game():
    def __init__(self, path, niveauActuel, g = None):
        self.lecteur = Lecteur(path)
        self.grille = self.init_grille()
        self.player = self.init_player()
        self.graphismes = g
        if g is not None:
            self.graphismes = self.init_graphismes(self.grille.getTaille(), niveauActuel)


    def game(self):
        casesParcourues = []
        pygame.display.flip()
        if self.niveauFini():
            return 1
            
        d = None
        while d is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    d = self.convertIntoDirection(event.key)

        if (d == -1):
            return self.quitter()

        casesParcourues = self.player.deplacement(self.grille, d, [self.player.getCA()])
        self.graphismes.deplaceJoueur(casesParcourues, d)
        return self.game()
        

    def convertIntoDirection(self, entry):
        if (entry == pygame.K_RIGHT):
            return ((1, 0))

        if (entry == pygame.K_LEFT):
            return ((-1, 0))

        if (entry == pygame.K_DOWN):
            return ((0, 1))

        if (entry == pygame.K_UP):
            return ((0, -1))

        
        
        if (entry == pygame.K_ESCAPE):
            return -1

        return ((0, 0))
        
        
    def niveauFini(self):
        return (self.grille.pasDeCaseLibre())
        

    def init_player(self):
        p = Player()
        celluleOrigine = self.grille.getCellule([0, 0])
        p.changeCA(celluleOrigine)
        celluleOrigine.passage()
        return p
        

    def init_grille(self):
        g = Grille()
        fichier = open(self.lecteur.getPath(), "r")
        g.crea_grille(fichier)
        return g
        
    def init_graphismes(self, d, niveauActuel):
        g = Graphismes(d, niveauActuel)
        g.loadTextures(niveauActuel)
        g.scaleTextures((g.getPas(), g.getPas()))
        g.afficheGrille(self.grille.getGrille())
        g.affichePlayer(self.player)
        return g

    def quitter(self):
        pygame.quit()
        return -1

class Lecteur():
    def __init__(self, path):
        self.path = path

    def lecture(self):
        p = self.getPath()
        tab = []
        fichier = open(p, "r")
        
        for ligne in fichier:
            tab.append([])
            for car in ligne:
                if car != '\n':
                    tab[-1].append(car)
        return tab            

    def getPath(self):
        return self.path
