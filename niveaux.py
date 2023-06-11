from Monde import *

class Niveaux():
    def __init__(self):
        self.worlds = self.genereWorlds()
        self.actualNumberWorld = 0
        self.menu = self.initMenu()
        self.selectionNiveaux()

    def selectionNiveaux(self):
        retour = 0
        dansLeJeu = True
        dansMenu = True
        while dansMenu:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.fenMenu.rectsMenu["jouer_button"].collidepoint(event.pos):
                        dansMenu = False

        while dansLeJeu:
            w = self.getActualWorld()
            retour = w.adventure()
            if (retour == 1):
                self.nextWorld()
                if (lastWorldPassed()):
                    pass


    def lastWorldPassed(self):
        return (self.getActualNumberWorld() == 0)


    #Fonctions d'accès
    def getWorlds(self):
        return self.worlds

    def getActualWorld(self):
        return self.getWorlds()[self.getActualNumberWorld()]

    def getActualNumberWorld(self):
        return self.actualNumberWorld

    def getNbWorlds(self):
        return (len(self.getWorlds()))

    #Fonctions génératrices
    def changeWorld(self, n):
        self.numondeActuel = n

    def nextWorld(self):
        self.changeWorld((self.getActualNumberWorld() + 1)%self.getNbWorlds())


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
