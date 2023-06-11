from game import *

class Monde():
    def __init__(self, name):
        self.name = name
        self.levels = []
        self.loadLevels()
        self.actualLevel = self.levels[0]


    def adventure(self):
        retour = self.launchLevel(self.getActualLevel().getNumber() - 1)
        if (retour == -1 or self.lastLevelPassed()):
            return retour
        
        self.nextLevel()
        return self.adventure()

    def nextLevel(self):
        numberNextLevel = self.getActualLevel().getNumber()
        self.actualLevel = self.getLevels()[numberNextlevel]
        
        
    def launchLevel(self, n):
        return self.levels[n].launch(self.getName())


    #Fonctions booléennes
    def lastLevelPassed(self):
        return (self.getActualLevel().getNumber() == (len(self.getLevels()) - 1))

    
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
        n = 0
        for level in lvs:
            name = level[:-4]
            self.levels.append(Level(n))
            n += 1



class Level():
    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def launch(self, monde):
        return Game("./levels/" + monde + "/Level" + str(self.getNumber()) + ".txt",
                    monde + "/").game()
