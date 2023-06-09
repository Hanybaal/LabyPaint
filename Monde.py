from game import *

class Monde():
    def __init__(self, name):
        self.name = name
        self.actualLevel = None
        self.levels = []
        self.loadLevels()



    def loadLevels(self):
        lvs = [f for f in os.listdir(self.getPath())]
        for level in lvs:
            name = level[:-4]
            self.levels.append(Level(n))

    def launchLevel(self, n):
        return self.levels[n](
            self.getPath() + "Level" + str(n) + ".txt")


    def lastLevelPassed(self):
        return (getActualLevel.getNumber() == len(getLevels()))

    def getName(self):
        return self.name

    def getPath(self):
        return ("./levels/" + self.getName() + "/")

    def getLevels(self):
        return self.levels

    def getActualLevel(self):
        return actualLevel

    def getNumberOfLevels(self):
        return len(self.getLevels())



class Level():
    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def launch(self, monde):
        return Game("./levels/" + monde + "/Level" + str(getNumber() + ".txt"), monde + "/").game()
