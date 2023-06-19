from game import *

class Monde():
    def __init__(self, name):
        self.name = name
        self.levels = []
        self.loadLevels()
        self.actualLevel = self.levels[0]


    def adventure(self):
        retour = self.launchLevel(self.getActualLevel().getNumber() - 1)
        if (retour == -1):
            return retour

        if (self.lastLevelPassed()):
            return 1
        
        self.nextLevel()
        return self.adventure()

    def nextLevel(self):
        numberNextLevel = self.getActualLevel().getNumber()
        self.actualLevel = self.getLevels()[numberNextLevel]
        
        
    def launchLevel(self, n):
        return self.levels[n].launch()


    #Fonctions booléennes
    def lastLevelPassed(self):
        return (self.getActualLevel().getNumber() == self.getNumberOfLevels())

    
    #Fonctions d'accès
    def getName(self):
        return self.name

    def getPath(self):
        return ("./levels/" + self.getName() + "/")

    def getLevels(self):
        return self.levels

    def getActualLevel(self):
        return self.actualLevel

    def getNumberOfLevels(self):
        return len(self.getLevels())

    #Fonctions génératrices
    def loadLevels(self):
        lvs = [f for f in os.listdir(self.getPath())]
        n = 1
        for level in lvs:
            name = level[:-4]
            self.levels.append(Level(n, self.getName()))
            n += 1



class Level():
    def __init__(self, number, world):
        self.number = number
        self.world = world

    ##Fonctions get
    def getNumber(self):
        return self.number

    def getWorld(self):
        return self.world


    def launch(self):
        return Game("./levels/" + self.getWorld() + "/Level" + str(self.getNumber()) + "/",
                    self.getWorld() + "/").game()

    
