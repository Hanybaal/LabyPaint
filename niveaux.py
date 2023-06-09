from game import *
from Monde import *

class Niveaux():
    def __init__(self):
        self.path = "./levels/"
        self.niveauActuel = 0
        self.mondes = ["foret/", "volcan/", "lagon/", "street/"]
        self.numondeActuel = 0
        self.loadLevels()
        self.menu = self.initMenu()
        self.selectionNiveaux()

    def selectionNiveaux(self):
        retour = 0
        dansLeJeu = True
        while dansLeJeu:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.fenMenu.rectsMenu["jouer_button"].collidepoint(event.pos):
                        self.adventure()
                        dansLeJeu = False
                        


    def adventure(self):
        retour = self.niveauSuivant()
        if retour == -1:
            return
        self.adventure()
    


    #Fonctions d'accès
    def getPath(self):
        return self.path

    def getMondeActuel(self):
        return self.mondes[self.getNumeroMondeActuel()]

    def getNumeroMondeActuel(self):
        return self.numondeActuel

    def getNiveauActuel(self):
        return self.niveauActuel

    def getNbMondes(self):
        return (len(self.levels.keys()))


    #Fonctions Modificatrices
    def changeMonde(self, n):
        self.numondeActuel = n

    def mondeSuivant(self):
        self.changeMonde((self.getNumeroMondeActuel() + 1)%self.getNbMondes())

    def changeNiveauActuel(self, n):
        self.niveauActuel = n

    def dernierNiveauPasse(self):
        return (self.getNiveauActuel() == self.getNbLevels())

    def niveauSuivant(self):
        if self.dernierNiveauPasse():
            ##A changer pour revenir sur la map du monde
            self.mondeSuivant()
            self.changeNiveauActuel(0)
        self.changeNiveauActuel((self.getNiveauActuel())%self.getNbLevels() + 1)
        return self.launchLevel(self.getNiveauActuel(), self.getMondeActuel())




    #Fonction d'initialisation
    def initMenu(self):
        self.fenMenu = Menu(10)
        self.fenMenu.loadMenu()
        self.fenMenu.scaleMenu()
        self.fenMenu.initRects()
        self.fenMenu.afficheMenu()
        pygame.display.flip()

n = Niveaux()
