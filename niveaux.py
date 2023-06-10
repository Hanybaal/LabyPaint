from Monde import *

class Niveaux():
    def __init__(self):
        self.worlds = self.genereWorlds()
        self.numondeActuel = 0
        self.menu = self.initMenu()
        self.selectionNiveaux()

    def selectionNiveaux(self):
        retour = 0
        dansLeJeu = True
        while dansLeJeu:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.fenMenu.rectsMenu["jouer_button"].collidepoint(event.pos):
                        dansLeJeu = False



    #Fonctions d'accès
    def getWorlds(self):
        return self.worlds

    def getActualWorld(self):
        return self.Worlds[self.getNumeroMondeActuel()]

    def getNumeroMondeActuel(self):
        return self.numondeActuel

    def getNbWorlds(self):
        return (len(self.getWorlds()))


    #Fonctions génératrices
    def changeWorld(self, n):
        self.numondeActuel = n

    def nextWorld(self):
        self.changeWorld((self.getNumeroMondeActuel() + 1)%self.getNbWorlds())


    def genereWorlds(self):
        listeDesWorlds = [Monde(m) for m in os.listdir("./levels/")]
        return listeDesWorlds


    #Fonction d'initialisation
    def initMenu(self):
        self.fenMenu = Menu(10)
        self.fenMenu.loadMenu()
        self.fenMenu.scaleMenu()
        self.fenMenu.initRects()
        self.fenMenu.afficheMenu()
        pygame.display.flip()

n = Niveaux()
